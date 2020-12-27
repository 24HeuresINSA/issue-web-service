import re
import json
import os

from github import Github

RAW_FILE = "README.md"
TOKEN = os.getenv("TOKEN")
TARGET_REPO = "Azmah-Bad/userStories-sandbox"  # TODO :: change this to the actual target repo


def getUserStories():
    with open(RAW_FILE, "r") as f:
        file = f.read()
    List = file[file.index("<!-- start  DO NOT DELETE THIS COMMENT -->"):]
    Jsons = List.split("```json")[1:]
    FormattedJsons = []
    for rawJson in Jsons:
        try:
            FormattedJsons.append(toJson(rawJson))
        except json.decoder.JSONDecodeError as e:
            print(e)
            print("Error while parsing :", rawJson)
    return FormattedJsons


def toJson(rawJson: str):
    uncommented = re.sub("//.*\n", "", rawJson)
    stripped = uncommented[uncommented.index("{"): uncommented.index("}") + 1]
    Json = json.loads(stripped)
    return Json


def createIssue(userStories):
    g = Github(TOKEN)
    repo = g.get_repo(TARGET_REPO)
    for userStory in userStories:
        mTests = ""
        for test in userStory['tests']:
            mTests += f"- [ ] {test}\n"

        mUsers = ""
        for user in userStory['users']:
            mUsers += f"- {user}\n"

        mBody = f"## Description : \n" \
                f"{userStory['description']}\n" \
                f"## Users\n" \
                f"{mUsers}\n" \
                f"## Tests\n" \
                f"{mTests}\n\n" \
                f"Author : _{userStory['author']}_" \
                f"\n\n added by userStories bot 🤖"

        mLabel = getLabel(repo, userStory['priority'])
        repo.create_issue(title=userStory["title"], body=mBody, labels=[mLabel])


def getLabel(repo, name):
    labels = repo.get_labels()
    for label in labels:
        if label.name == name or label.name == name.upper():
            return label
    return None


if __name__ == '__main__':
    OneUserStory = [getUserStories()[0]]
    createIssue(OneUserStory)
