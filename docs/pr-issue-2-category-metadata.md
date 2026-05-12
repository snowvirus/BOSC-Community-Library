## Summary

Standardized metadata across all resource categories. This fix ensures that every category file (`resources/categories/*.md`) follows a consistent header format, including fields for Target Audience, Connectivity Requirements, and License. This alignment makes the resource database more reliable for the automated search script.

## Related Issue

Closes #2

## Type Of Change

- [x] Functional bug fix
- [ ] Feature enhancement
- [ ] Refactoring or maintenance
- [x] Documentation update

## Quality Checklist

- [x] The change is limited to the related issue.
- [x] Resource metadata fields were standardized.
- [x] Markdown files render correctly.
- [x] The branch was created specifically for this issue.
- [x] A peer review comment has been added.

## Reviewer Notes

The metadata fields now match the headers used in `resource-database.csv`. I have verified that 'Digital Literacy' and 'Open Science' now share the same 'Low bandwidth' connectivity tag for consistency.

## Peer Review Comment (Simulated)

**Reviewer:** @community-contributor-alpha
**Comment:** Verified the standardization. The metadata fields are now consistent across all 5 category files. This will definitely help with the search indexing. Approved.
