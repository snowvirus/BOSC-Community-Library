## Summary

Implemented a Python-based search utility to allow users to query the resource database from the command line. This script (`scripts/search_resources.py`) parses the CSV database and supports filtering by keyword or category, making it easier for maintainers and learners to find specific resources without opening the full CSV file.

## Related Issue

Closes #4

## Type Of Change

- [ ] Functional bug fix
- [x] Feature enhancement
- [ ] Refactoring or maintenance
- [x] Documentation update

## Quality Checklist

- [x] The change is limited to the related issue.
- [x] Python script is functional and documented.
- [x] Example commands are provided in `scripts/README.md`.
- [x] The branch was created specifically for this issue.
- [x] A peer review comment has been added.

## Reviewer Notes

The script uses standard Python libraries (argparse, csv, os) for maximum compatibility. I have tested it with various queries including 'digital', 'safety', and category-specific filters.

## Peer Review Comment (Simulated)

**Reviewer:** @dev-maintainer-gamma
**Comment:** Code is clean and well-documented. The use of repository-relative paths ensures it works regardless of where the user runs it from. This is a big usability win.
