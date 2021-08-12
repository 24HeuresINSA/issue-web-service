import requests
import json
import datetime


class Issue:
    def __init__(self, repo, token, data=None, milestone=None, git_platform=None):
        """
        :param repo: the github repository to push issues with format username|organisation/project for github
        and username|organisation/[subproject]/project for gitlab
        :param token: the github token with repo scope ( to get one : https://github.com/settings/tokens/new)
        :param data: the json structure of the issue
        :param git_platform: String "github" or "gitlab". Platform to push issue
        """

        self.repo = repo
        self.token = token
        self.data = data
        self.body = None  # Need to call one md generator
        self.milestone = milestone
        if not git_platform:
            raise ValueError("git_platform not define")
        elif git_platform not in ["github", "gitlab"]:
            raise ValueError("git_platform should be github or gitlab")
        else:
            self.git_platform = git_platform

    def pushIssue(self):
        """
       Push one issue to github or gitlab
       :return: the http response of push requests
       """

        if not self.body:
            raise ValueError("body not define, call MD generator first")

        if isinstance(self.data, list):
            raise TypeError("Use pushIssues for multiple issues")

        if self.checkDuplicateTitle():
            return "Issue already exists"

        url = f"https://api.github.com/repos/{self.repo}/issues" if self.git_platform == "github" else \
            f"https://gitlab.com/api/v4/projects/{self.repo.replace('/', '%2F')}/issues"

        payload = {
            'title': self.data["title"],
            'body' if self.git_platform == "github" else 'description': self.body,
            'labels': self.data["tags"],
            'milestone' if self.git_platform == "github" else 'milestone_id': self.milestone
        }
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        return response

    def pushIssues(self):
        issueList = self.data.copy()
        for issue in issueList:
            self.data = issue
            if not self.checkDuplicateTitle():
                self.generateMDIssue()
                self.pushIssue()

    def getIssues(self):
        """
       Get issues to github or gitlab
       :return: the list of github or gitlab issues
       """

        url = f"https://api.github.com/repos/{self.repo}/issues?state=all" if self.git_platform == "github" else \
            f"https://gitlab.com/api/v4/projects/{self.repo.replace('/', '%2F')}/issues?scope=all"

        payload = {}
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        jsonResponse = json.loads(response.text)
        return [jsonIssue["title"] for jsonIssue in jsonResponse]

    def checkDuplicateTitle(self):
        """
        Check if one issue title already exists in github or gitlab
        :return: boolean
        """
        return self.data["title"] in self.getIssues()

    def MDTestList(self):
        """
        :return: string of md test list format
        """
        return '\n'.join([f" - [ ] {test}" for test in self.data["tests"]])

    def MDUserBadge(self):
        """
        :return: string of md "badge"
        """
        return ' '.join([f"``{user}``" for user in self.data["scope"]])

    def MDNumberList(self):
        """
        :return: string of md number list
        """
        return '\n'.join(f"1. {step}" for step in self.data['steps'])

    def loadDataFromMD(self, mdfile):
        """
        Parse MD file to get json user story format
        :param mdfile: list of user story like this
        ```json
        {
        "title": "X",
        "author": "X",
        }
        ```
        :return: json object
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
            items[i] = db
        self.data = items

    def loadDataFromJson(self, jsonfile):
        """
        :param jsonfile: path to the json file
        :return: load json object in self.data
        """
        with open(jsonfile, "r") as file:
            self.data = json.load(file)

    def descriptionSwitcher(self):
        """
        :return: string for type of issue
        """
        if "bug" in self.data['tags']:
            return "Bug"
        elif "feature" in self.data['tags']:
            return "Feature"
        else:
            return "Issue"

    def generateMDIssue(self):
        """
        :return: string of md structure for bug issue
        """

        try:
            comments = self.data["comments"]
        except KeyError:
            comments = ""

        try:
            _ = self.data["steps"]
            bugsSteps = self.MDNumberList()
        except KeyError:
            bugsSteps = ""

        try:
            _ = self.data["tests"]
            testsSteps = self.MDTestList()
        except KeyError:
            testsSteps = ""

        try:
            _ = self.data["url"]
            url = self.MDTestList()
        except KeyError:
            url = ""

        self.body = f"# Date {datetime.date.today().strftime('%d/%m/%Y')}\n\n" \
                    f"#{'URL' if url != '' else ''} {url} \n\n" \
                    f"# Author {self.data['author']} \n\n" \
                    f"# Scope : {self.MDUserBadge()} \n\n" \
                    f"# {self.descriptionSwitcher()} description \n\n" \
                    f"{self.data['description']} \n\n" \
                    f"{'# Etapes de validation' if testsSteps != '' else ''} \n" \
                    f"{testsSteps}" \
                    f"{'# Etapes pour reproduire le bug' if bugsSteps != '' else ''} \n" \
                    f"{bugsSteps}" \
                    f"{'## Comments' if comments != '' else ''}   \n" \
                    f"{comments}"
