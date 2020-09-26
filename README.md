# tellme

Get information from o.s.d Maintenance: Test Repo specific for SAP & HA

## Requirements

- Python 3
- Beautiful Soup (run `pip3 install --user bs4`)

## Options

```
  -a, --all             Show all tests. Ignored if --status option is used
  -d DATE, --date DATE  Show results for date: [[[CC]YY]MM]DD | -<DAYS AGO>
  -s STATUS, , --status STATUS
			Filter by status. May be specified multiple times
  Choices for STATUS:
	blocked cancelled failed incomplete none obsoleted parallel_failed parallel_restarted passed
	scheduled skipped softfailed timeout_exceeded unknown uploading user_cancelled user_restarted
```
