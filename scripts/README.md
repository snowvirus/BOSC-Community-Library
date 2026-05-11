# Scripts Directory

The `scripts/` directory contains command-line utilities for maintaining or searching the BOSC Community Library resource catalogue.

## Available Scripts

### `search_resources.py`

Searches [../resources/resource-database.csv](../resources/resource-database.csv) and prints matching resources.

Examples:

```bash
python3 scripts/search_resources.py digital
python3 scripts/search_resources.py safety --category "Digital Literacy"
python3 scripts/search_resources.py --category "Teacher Training"
```

The script searches useful catalogue fields such as title, category, provider, audience, connectivity, description, and status. Results include the resource title, category, audience, access path, connectivity needs, license, review status, and description.

## Maintenance Notes

- Keep scripts small and readable so students and new contributors can understand them.
- Document each script in this README before adding more tools.
- Scripts should use repository-relative paths when possible.
- Test scripts after changing the CSV structure or resource field names.
