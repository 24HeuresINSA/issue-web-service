# Auto push issue from json or md

```
usage: autoPushIssue.py [-h] [--token TOKEN] [--json] [--markdonw]
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
  --json, -j            Push issue from json file
  --markdonw, -m        Push issue from markdown file
```