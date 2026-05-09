# Scripts Directory

The `scripts/` directory contains command-line utilities for maintaining or searching the BOSC Community Library resource catalogue.

## Available Scripts

### `search_resources.py`

Searches [../resources/resource-database.csv](../resources/resource-database.csv) and prints matching resources.

Example:

```bash
python3 scripts/search_resources.py digital
```

## Maintenance Notes

- Keep scripts small and readable so students and new contributors can understand them.
- Document each script in this README before adding more tools.
- Scripts should use repository-relative paths when possible.
- Test scripts after changing the CSV structure or resource field names.
