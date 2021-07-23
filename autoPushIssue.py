import requests
import json
import os
import argparse


def push_issue(username, repo, token, title, content=None, labels=None, milestone=None, gitPlatfom=None):
    """
    Push issues to github
    :param username: the github username
    :param repo: the github repository to push issues
    :param token: the github token with repo scope ( to get one : https://github.com/settings/tokens/new)
    :param title: the issue title
    :param content: the issue body
    :param labels: the issue labels
    :param milestone: the milstone
    :param gitPlatfom: String "github" or "gitlab". Platform to push issue
    :return: the http response of push requests
    """
    if not gitPlatfom:
        return

    url = f"https://api.github.com/repos/{username}/{repo}/issues" if gitPlatfom == "github" else \
        f"https://gitlab.com/api/v4/projects/{username.replace('/', '%2F')}%2F{repo}/issues"

    payload = {
        'title': title,
        'body' if gitPlatfom == "github" else 'description': content,
        'labels': labels,
        'milestone' if gitPlatfom == "github" else 'milestone_id': milestone
    }
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response


def get_issues(username, repo, token, gitPlatform=None):
    """
    Getting all opened and closed issues of the repo
    :param username: the github username
    :param repo: the github repository to get issues
    :param token: the github token with repo scope ( to get one : https://github.com/settings/tokens/new)
    :param gitPlatform: String "github" or "gitlab". Platform to push issue
    :return: list of all issues title from the repo
    """
    url = f"https://api.github.com/repos/{username}/{repo}/issues?state=all" if gitPlatform == "github" else \
        f"https://gitlab.com/api/v4/projects/{username.replace('/', '%2F')}%2F{repo}/issues?scope=all"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)
    return [jsonIssue["title"] for jsonIssue in jsonResponse]


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
    "comments": "X"
    }
    :return: The formatted md data
    """
    title = dict_data["title"]
    author = dict_data["author"]
    users = dict_data["users"]
    description = dict_data["description"]
    tests = dict_data["tests"]
    try:
        comments = dict_data["comments"]
    except KeyError:
        comments = ""
    return f"# {title}  \n" \
           f"#### author : {author}  \n" \
           f"### Scope : {userToBadge(users)}  \n" \
           f"## Description  \n" \
           f"{description}  \n" \
           f"## Test  \n" \
           f"{testsToMDList(tests)}  \n" \
           f"{'## Comments' if comments != '' else ''}   \n" \
           f"{comments}"


def testsToMDList(tests):
    """
    Formatting list test to MD issue check items
    :param tests: list of string
    :return: the formatted MD
    """
    return '\n'.join([f" - [ ] {test}" for test in tests])


def userToBadge(users):
    """
    Formatting user list in badges
    :param users: list of string
    :return: the formatted MD
    """
    return ' '.join([f"``{user}``" for user in users])


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
    "comments": "X"
    }
    ```
    :return: tuple with (issueTitle, allValueInDict, issuePriority)
    """
    with open(mdfile, "r") as f:
        file = f.read()
    items = file[file.index("<!-- start  DO NOT DELETE THIS COMMENT -->"):]
    items = items.split("```json")[1:]
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
    parser.add_argument("user", help="the github username or the gitlab username / "
                                     "groups (ex: 24-heures-insa/overbookd)")
    parser.add_argument("repo", help="the github repository to push issues or the gitlab project")
    parser.add_argument("--ghtoken", help="the github token with repo scope "
                                          "( to get one : https://github.com/settings/tokens/new)"
                                          "You can set a envirenement variable GH_TOKEN to avoid this parameter")
    parser.add_argument("--gltoken", help="the gitlab token with api scope "
                                          "( to get one : https://gitlab.com/-/profile/personal_access_tokens)"
                                          "You can set a envirenement variable GL_TOKEN to avoid this parameter")
    parser.add_argument("--milestone", help="Number of associate milestone", type=int)
    parser.add_argument("--json", "-j", help="Push issue from json file", action='store_true')
    parser.add_argument("--markdown", "-m", help="Push issue from markdown file", action='store_true')
    parser.add_argument("file", help="the file with issue")
    parser.add_argument("gitplatform", help="Push to github with 'github' and 'gitlab' for gitlab")
    args = parser.parse_args()

    if args.gitplatform == "github":
        if args.ghtoken:
            TOKEN = args.ghtoken
        else:
            TOKEN = os.getenv('GH_TOKEN')

    if args.gitplatform == "gitlab":
        if args.gltoken:
            TOKEN = args.gltoken
        else:
            TOKEN = os.getenv('GL_TOKEN')

    if args.milestone:
        MILESTONE = args.milestone
    else:
        MILESTONE = None

    if args.json:
        data = dataFromJson(args.file)
    elif args.markdown:
        data = dataFromMD(args.file)
    else:
        data = None
        print("no format specify. Please specify one")
        exit(1)

    for issue in data:
        currentIssues = get_issues(args.user, args.repo, TOKEN, args.gitplatform)
        # print(currentIssues)
        if issue[0] not in currentIssues:
            code = push_issue(username=args.user,
                              repo=args.repo,
                              token=TOKEN,
                              title=issue[0],
                              content=toMD(issue[1]),
                              labels=["enhancement", issue[2]] if issue[2] != "" else ["enhancement"],
                              milestone=MILESTONE,
                              gitPlatfom=args.gitplatform
                              )
            print(f"{issue[0]} : {'✔️' if code.status_code == 201 else '❌ | return code : ' + code.text}")
        else:
            print(f"{issue[0]} : Already exists")
