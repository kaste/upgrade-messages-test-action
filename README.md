# upgrade-messages-test-action

For published Sublime Text plugins Package Control will look at the file `messages.json` for upgrade or install messages shown to the user.  

This simple GitHub action ensures this file is correct and points to actual files in the repo.

The usage is as simple as possible: 

```
steps:
- uses: actions/checkout
- uses: kaste/upgrade-messages-test-action
```

