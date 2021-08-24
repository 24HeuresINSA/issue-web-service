# Auto push issue from json or md

Script to push issue from json or Markdown file.  
By default, use an env var named ``GH_TOKEN`` or ``GL_TOKEN`` for github or gitlab platform

```
usage: autoPushIssue.py [-h] [--ghtoken GHTOKEN] [--gltoken GLTOKEN]
                        [--milestone MILESTONE] [--json] [--markdown]
                        repo file gitplatform

positional arguments:
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
   ``--gltoken <GitLab TOKEN> -j <Username/repo> data.json gitlab`` 
   
 - I want to push issues on gitlab subgroup repo with json file:
   ``--gltoken  <GitLab TOKEN> -j <Group/SubGroup/repo> data.json gitlab``
   
 - I want to push issues on github personnal / organisation repo with json file:
   ``--ghtoken <GitHub TOKEN> -j <Username or organisation name/repo> data.json github``

## Data structure
### Json

see doc folder for the json structure

### Markdown

~~~markdown
<!-- start  DO NOT DELETE THIS COMMENT -->

```json
put here the same structure as json (see doc folder for more details)
```
~~~