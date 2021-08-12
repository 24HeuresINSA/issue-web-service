import flask
import os
from functools import wraps
from Issue import Issue

app = flask.Flask(__name__)

key = os.getenv("KEY")
GL_TOKEN = os.getenv("GL_TOKEN")
GH_TOKEN = os.getenv("GH_TOKEN")


def checkKey(issue_dict, issue_key):
    try:
        issue_dict[issue_key]
    except KeyError:
        flask.abort(400, f"{issue_key} key is needed")


def checkCommonKey(issue_to_test):
    checkKey(issue_to_test, "repo")
    checkKey(issue_to_test, "git_platform")
    checkKey(issue_to_test, "title")
    checkKey(issue_to_test, "scope")
    checkKey(issue_to_test, "author")
    checkKey(issue_to_test, "description")


def requireApiKey(view_function):
    """
    Decorator for API key
    """
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if flask.request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            flask.abort(401)
    return decorated_function


@app.route("/version", methods=["GET"])
def version():
    with open("version", "r") as versionNumber:
        return versionNumber.read()


@app.route("/bug", methods=["POST"])
def bugIssue():
    bug_issue = flask.request.json
    checkCommonKey(bug_issue)
    checkKey(bug_issue, "steps")

    for tag in ["bug", "TODO"]:
        bug_issue["tags"].append(tag)

    try:
        milestone = bug_issue["milestone"]
    except KeyError:
        milestone = None
        pass

    issue = Issue(
        repo=bug_issue["repo"],
        git_platform=bug_issue["git_platform"],
        token=GL_TOKEN if bug_issue["git_platform"] == "gitlab" else GH_TOKEN,
        data=bug_issue,
        milestone=milestone
    )

    issue.generateMDIssue()
    return_statement = issue.pushIssue()
    if isinstance(return_statement, str):
        return return_statement
    else:
        return return_statement.text, return_statement.status_code


@app.route("/feature", methods=["POST"])
def featureIssue():
    feature_issue = flask.request.json
    checkCommonKey(feature_issue)
    checkKey(feature_issue, "tests")

    for tag in ["feature", "TODO"]:
        feature_issue["tags"].append(tag)

    try:
        milestone = feature_issue["milestone"]
    except KeyError:
        milestone = None
        pass

    issue = Issue(
        repo=feature_issue["repo"],
        git_platform=feature_issue["git_platform"],
        token=GL_TOKEN if feature_issue["git_platform"] == "gitlab" else GH_TOKEN,
        data=feature_issue,
        milestone=milestone
    )

    issue.generateMDIssue()
    return_statement = issue.pushIssue()
    if isinstance(return_statement, str):
        return return_statement
    else:
        return return_statement.text, return_statement.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0')
