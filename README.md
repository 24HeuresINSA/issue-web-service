# Auto push issue from json or md

Script to push issue from json or Markdown file.  
By default, use an env var named ``GH_TOKEN``

```
usage: autoPushIssue.py [-h] [--token TOKEN] [--milestone MILESTONE] [--json]
                        [--markdown]
                        user repo file

positional arguments:
  user                  the github username
  repo                  the github repository to push issues
  file                  the file with issue

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN, -t TOKEN
                        the github token with repo scope ( to get one :
                        https://github.com/settings/tokens/new)
  --milestone MILESTONE
                        Number of associate milestone
  --json, -j            Push issue from json file
  --markdown, -m        Push issue from markdown file
```

## Data structure
### Json

```json
{
    "title": "The card title",
    "author": "Your name in case we need to ask you questions",
    "priority": "", //LEAVE AS IT IS
    "users" : [
        "GUEST",
        "ADMIN"
    ], // FILL THE LIST
    "description": "What you can do",
    "tests":[
        "test 1",
        "test 2"
    ], // FILL THE LIST
    "comments": "Explain your pain" // NOT MANDATORY
}
```

### Markdown

~~~markdown
<!-- start  DO NOT DELETE THIS COMMENT -->

```json
{
    "title": "Account creation",
    "author": "comSA",
    "priority": "p1", //LEAVE AS IT IS
    "users" : [
        "GUEST"
    ], // FILL THE LIST
    "description": "create an account",
    "tests":[
        "There is account creation form.",
        "The account creation is secure.",
        "The database is filled.",
        "Form have ALL the options described in the specifications."
    ], // FILL THE LIST
    "comments": "Do we accept all the new users? Or do you need an access link ?"
}
```
~~~