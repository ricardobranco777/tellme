# tellme

Get information from o.s.d Maintenance: Test Repo specific for SAP & HA

[![Build Status](https://travis-ci.org/ricardobranco777/tellme.svg?branch=master)](https://travis-ci.org/ricardobranco777/tellme)

## Requirements

- Python 3
- Beautiful Soup (install `python3-beautifulsoup4` package or run `pip3 install --user bs4`)

## Options

```
  -a, --all             Show all tests. Ignored if --status option is used
  -d DATE, --date DATE  Show results for date: [[[CC]YY]MM]DD | -<DAYS AGO>
  -H, --no-header       Do not show header
  -k, --insecure        Allow insecure server connections when using SSL
  -s STATUS, , --status STATUS
			Filter by status. May be specified multiple times
  Choices for STATUS:
	blocked cancelled failed incomplete none obsoleted parallel_failed parallel_restarted passed
	scheduled skipped softfailed timeout_exceeded unknown uploading user_cancelled user_restarted
```
