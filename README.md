# upgrade-messages-test-action

For published Sublime Text plugins Package Control will look at the file `messages.json` for upgrade or install messages shown to the user.  

This simple GitHub action ensures this file is correct and points to actual files in the repo.

The usage is as simple as possible: 

```
jobs:
  check-messages:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: kaste/upgrade-messages-test-action@v1

```

