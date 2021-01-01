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