# Auto push issue from json or md

Script to push issue from json or Markdown file.  
By default, use an env var named ``GH_TOKEN`` or ``GL_TOKEN`` for github or gitlab platform

```
usage: autoPushIssue.py [-h] [--ghtoken GHTOKEN] [--gltoken GLTOKEN]
                        [--milestone MILESTONE] [--json] [--markdown]
                        user repo file gitplatform

positional arguments:
  user                  the github username or the gitlab username / groups
                        (ex: 24-heures-insa/overbookd)
  repo                  the github repository to push issues or the gitlab
                        project
  file                  the file with issue
  gitplatform           Push to github with 'github' and 'gitlab' for gitlab

optional arguments:
  -h, --help            show this help message and exit
  --ghtoken GHTOKEN     the github token with repo scope ( to get one :
                        https://github.com/settings/tokens/new)You can set a
                        envirenement variable GH_TOKEN to avoid this parameter
  --gltoken GLTOKEN     the gitlab token with api scope ( to get one : https:/
                        /gitlab.com/-/profile/personal_access_tokens)You can
                        set a envirenement variable GL_TOKEN to avoid this
                        parameter
  --milestone MILESTONE
                        Number of associate milestone
  --json, -j            Push issue from json file
  --markdown, -m        Push issue from markdown file
```

For exemple: 
 - I want to push issues on gitlab presonnal repo with json file:
   ``--gltoken <GitLab TOKEN> -j <Username> <repo> data.json gitlab`` 
   
 - I want to push issues on gitlab subgroup repo with json file:
   ``--gltoken  <GitLab TOKEN> -j <Group/SubGroup> <repo> data.json gitlab``
   
 - I want to push issues on github personnal / organisation repo with json file:
   ``--ghtoken <GitHub TOKEN> -j <Username or organisation name> <repo> data.json github``

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