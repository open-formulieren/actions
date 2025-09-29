# Open Formulieren Github Actions

A set of re-usable Github actions to support the CI pipelines of projects and libraries.

## Usage

**Check message extraction**

Validates that all localization strings have been extracted from the source code (and
compiled, if the compilation result is in version control).

```yaml
jobs:

  i18n-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5
      - uses: open-formulieren/actions/check-message-extraction@v1
        with:
          paths: i18n/{compiled,messages}  # the default
          extraction-command: ./bin/makemessages.sh  # the default
          compilation-command: npm run compilemessages  # the default
```

**Check for missing translations**

Scans the translations for missing translations, as part of the release process.

The action is skipped unless:

* the PR source branch has a `release/` prefix or
* a git tag is being built

```yaml
jobs:

  missing-translations-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5
      - uses: open-formulieren/actions/check-missing-translations@v1
        with:
          messages-path: i18n/messages
          locales: nl  # comma-separated list of locales, matching the i18n/messages/{locale}.json path
```
