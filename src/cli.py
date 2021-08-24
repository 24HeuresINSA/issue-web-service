from Issue import Issue
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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

    newIssue = Issue(repo=args.repo,
                     token=TOKEN,
                     milestone=MILESTONE,
                     git_platform=args.gitplatform)

    if args.json:
        newIssue.loadDataFromJson(args.file)
    elif args.markdown:
        newIssue.loadDataFromMD(args.file)
    else:
        data = None
        print("no format specify. Please specify one")
        exit(1)

    newIssue.pushIssues()
