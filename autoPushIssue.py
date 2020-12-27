import requests
import json
import os
import argparse


def push_issue(username, repo, token, title, content=None, labels=None, milestone=None):
    """
    Push issues to github
    :param username: the github username
    :param repo: the github repository to push issues
    :param token: the github token with repo scope ( to get one : https://github.com/settings/tokens/new)
    :param title: the issue title
    :param content: the issue body
    :param labels: the issue labels
    :param milestone: the milstone
    :return: the http response of push requests
    """
    url = f"https://api.github.com/repos/{username}/{repo}/issues"

    payload = {
        'title': title,
        'body': content,
        'labels': labels,
        'milestone': milestone
    }
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response


def toMD(dict_data):
    """
    Convert json user story in MD for the issue
    :param dict_data: json with
    {
    "title": "X",
    "author": "X",
    "priority": "p1",
    "users" : ["USER1",
               "USER2"],
    "description": "X",
    "tests":["test 1",
            "test2."],
    "commments": "X"
    }
    :return: The formated md data
    """
    title = dict_data["title"]
    author = dict_data["author"]
    users = dict_data["users"]
    description = dict_data["description"]
    tests = dict_data["tests"]
    try:
        comments = dict_data["commments"]
    except KeyError:
        comments = ""
    return f"""
# {title}
#### author : {author}  
### Scope : {userToBadge(users)}
## Descriptiton  
{description}
## Test  
{testsToMDList(tests)}
{"## Comments" if comments != "" else ""}  
{comments}
"""


def testsToMDList(tests):
    """
    Formating list test to MD issue check items
    :param tests: list of string
    :return: the formated MD
    """
    formating = ""
    for test in tests:
        formating += f" - [ ] {test}  \n"
    return formating


def userToBadge(users):
    """
    Formating user list in badges
    :param users: list of string
    :return: the formated MD
    """
    formating = ""
    for user in users:
        formating += f"``{user}`` "
    return formating


def dataFromJson(jsonfile):
    """
    List of tuple to use data
    :param jsonfile: dict_data: json with
    {
    "title": "X",
    "author": "X",
    "priority": "p1",
    "users" : ["USER1",
               "USER2"],
    "description": "X",
    "tests":["test 1",
            "test2."],
    "commments": "X"
    }
    :return: tuple with (issueTitle, allValueInDict, issuePriority)
    """
    with open(jsonfile, "r") as file:
        dbjson = json.load(file)
    return [(db["title"], db, db["priority"]) for db in dbjson]


def dataFromMD(mdfile):
    """
    Parse MD file to get json user story format
    :param mdfile: lis of user story like this
    ```json
    dict_data: json with
    {
    "title": "X",
    "author": "X",
    "priority": "p1",
    "users" : ["USER1",
               "USER2"],
    "description": "X",
    "tests":["test 1",
            "test2."],
    "commments": "X"
    }
    ```
    :return: tuple with (issueTitle, allValueInDict, issuePriority)
    """
    with open(mdfile, "r") as file:
        items = file.read().split("```json")[2:]
        for i in range(len(items)):
            items[i] = items[i].replace("//LEAVE AS IT IS", "")
            items[i] = items[i].replace("// FILL THE LIST", "")
            items[i] = items[i].replace("```", "")
            items[i] = items[i].replace("\n", "")
            items[i] = items[i].strip()
            db = json.loads(items[i])
            items[i] = (db["title"], db, db["priority"])
    return items


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="the github username")
    parser.add_argument("repo", help="the github repository to push issues")
    parser.add_argument("--token", "-t", help="the github token with repo scope "
                                              "( to get one : https://github.com/settings/tokens/new)")
    parser.add_argument("--milestone", help="Number of associate milestone", type=int)
    parser.add_argument("--json", "-j", help="Push issue from json file", action='store_true')
    parser.add_argument("--markdown", "-m", help="Push issue from markdown file", action='store_true')
    parser.add_argument("file", help="the file with issue")
    args = parser.parse_args()

    if args.token:
        TOKEN = args.token
    else:
        TOKEN = os.getenv('GH_TOKEN')

    if args.milestone:
        MILESTONE = args.milestone
    else:
        MILESTONE = None

    if args.json:
        data = dataFromJson(args.file)
    elif args.markdown:
        data = dataFromMD(args.file)
    else:
        print("no format specify. Please specify one")

    for issue in data:
        code = push_issue(args.user,
                          args.repo,
                          TOKEN,
                          issue[0],
                          toMD(issue[1]),
                          ["enhancement", issue[2]] if issue[2] != "" else ["enhancement"],
                          MILESTONE
                          )
        print(f"{issue[0]} : {'✔️' if code.status_code == 201 else '❌ | return code : ' + code.text}")
