import flask
import os
from functools import wraps
from Issue import Issue
import json

app = flask.Flask(__name__)

key = os.getenv("KEY")
GL_TOKEN = os.getenv("GL_TOKEN")
GH_TOKEN = os.getenv("GH_TOKEN")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
FEATURE = "feature"
BUG = "bug"


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


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


@app.route("/<string:issueType>", methods=["POST"])
def bugIssue(issueType):
    if issueType not in [BUG, FEATURE]:
        return "Request should be bug or feature", 400

    if 'file' not in flask.request.files:
        return 'No file field', 400
    file = flask.request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    bug_issue = json.loads(flask.request.form.to_dict()['json'])
    checkCommonKey(bug_issue)
    if issueType == BUG:
        checkKey(bug_issue, "steps")
    if issueType == FEATURE:
        checkKey(bug_issue, "tests")

    bug_issue["tags"].append("TODO")
    bug_issue["tags"].append(issueType)

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

    if file and allowed_file(file.filename):
        issue.uploadImage(file)
    else:
        return f"Only {ALLOWED_EXTENSIONS} files authorized"
    issue.generateMDIssue()
    return_statement = issue.pushIssue()
    if isinstance(return_statement, str):
        return return_statement
    else:
        return return_statement.text, return_statement.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0')
