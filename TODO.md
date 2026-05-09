# GitHub Issues To Create

Use these entries to create the five GitHub issues before continuing implementation work. Each `TODO:` line is written so VS Code TODO extensions can index the backlog.

When this file and `.github/workflows/sync-todo-issues.yml` are pushed to the `main` branch, GitHub Actions will read this file and create any missing GitHub issues by title. The workflow can also be run manually from the repository's **Actions** tab.

---

## TODO: Issue #1 - Fix broken resource links

**GitHub title:** `[Functional bug]: Fix broken resource links`

**Issue type:** Functional bug

**Suggested branch:** `fix/resource-link-validation`

**Labels:** `bug`, `resources`, `triage`

### Description

Some resource category markdown files may contain broken, incomplete, or unclear resource links. The repository needs a link validation pass so learners and teachers can trust the listed materials.

### Current Behavior

Resource category files in `resources/categories/` have not been fully checked for broken links, missing access notes, or inconsistent link formatting.

### Expected Behavior

All category resource links should be valid, clearly named, and usable in low-bandwidth community learning contexts.

### Affected Files Or Sections

- `resources/categories/*.md`
- `resources/resource-database.csv`
- `README.md`

### Acceptance Criteria

- [ ] All resource links in category markdown files are reviewed.
- [ ] Broken or unclear links are fixed or replaced.
- [ ] Low-bandwidth or offline access notes are preserved where relevant.
- [ ] The change is committed from `fix/resource-link-validation`.
- [ ] A pull request references this issue and receives review evidence before merge.

---

## TODO: Issue #2 - Standardize category metadata

**GitHub title:** `[Functional bug]: Standardize category metadata`

**Issue type:** Functional bug

**Suggested branch:** `fix/category-metadata`

**Labels:** `bug`, `metadata`, `triage`

### Description

The resource category markdown files should use consistent metadata so future automation can parse the library reliably.

### Current Behavior

Category files may use inconsistent headings, status labels, audience notes, or metadata structure.

### Expected Behavior

Each category file should follow the same metadata pattern and describe audience, access format, license expectations, and review status consistently.

### Affected Files Or Sections

- `resources/categories/*.md`
- `resources/resource-database.csv`

### Acceptance Criteria

- [ ] Category metadata fields are consistent across all category files.
- [ ] Metadata aligns with the CSV resource database.
- [ ] Markdown remains readable for non-technical contributors.
- [ ] The change is committed from `fix/category-metadata`.
- [ ] A pull request references this issue and receives review evidence before merge.

---

## TODO: Issue #3 - Add local language support

**GitHub title:** `[Feature enhancement]: Add local language support`

**Issue type:** Feature enhancement

**Suggested branch:** `feat/local-language-support`

**Labels:** `enhancement`, `localization`, `triage`

### Description

The community library should support local language access so more learners and teachers can benefit from the project.

### Current Behavior

The project has limited localized content and needs a clear place for translated summaries or contribution guidance.

### Expected Behavior

The repository should include a local language section, beginning with Luganda support, and explain how contributors can add translated resource summaries.

### Affected Files Or Sections

- `resources/categories/local-language-support.md`
- `resources/local-language/`
- `resources/resource-database.csv`
- `README.md`

### Acceptance Criteria

- [ ] A local language section exists in the resources structure.
- [ ] Luganda summary or guidance content is added.
- [ ] The resource database includes the local language support entry.
- [ ] Main documentation links to the local language section.
- [ ] The change is committed from `feat/local-language-support`.
- [ ] A pull request references this issue and receives review evidence before merge.

---

## TODO: Issue #4 - Implement searchable resource database

**GitHub title:** `[Feature enhancement]: Implement searchable resource database`

**Issue type:** Feature enhancement

**Suggested branch:** `feat/searchable-resource-database`

**Labels:** `enhancement`, `script`, `triage`

### Description

Users should be able to search the resource database by keyword or category instead of manually scanning the CSV file.

### Current Behavior

The resource database exists as `resources/resource-database.csv`, but searching depends on manual file inspection or basic editor search.

### Expected Behavior

A simple CLI search script should let users query the CSV and return matching resources with useful fields such as title, category, audience, access notes, and status.

### Affected Files Or Sections

- `scripts/search_resources.py`
- `resources/resource-database.csv`
- `scripts/README.md`
- `README.md`

### Acceptance Criteria

- [ ] A CLI search script can search by keyword or category.
- [ ] The script reads `resources/resource-database.csv`.
- [ ] Search results include the most useful resource details.
- [ ] Usage instructions are documented.
- [ ] The change is committed from `feat/searchable-resource-database`.
- [ ] A pull request references this issue and receives review evidence before merge.

---

## TODO: Issue #5 - Refactor repository organization

**GitHub title:** `[Refactoring]: Improve repository organization`

**Issue type:** Refactoring or maintenance

**Suggested branch:** `refactor/resource-organization`

**Labels:** `maintenance`, `documentation`, `triage`

### Description

The repository should clearly separate community resources, governance documents, scripts, and exam documentation so contributors can navigate it easily.

### Current Behavior

Some files and folders may be difficult for new contributors to understand without opening several documents first.

### Expected Behavior

Each major directory should have a clear purpose, documentation files should be linked from the README, and resource-related files should be organized predictably.

### Affected Files Or Sections

- `README.md`
- `docs/`
- `governance/`
- `resources/`
- `scripts/`

### Acceptance Criteria

- [ ] Major directories have clear README or navigation notes.
- [ ] Community-facing docs and technical docs are easy to distinguish.
- [ ] README repository structure matches the actual files.
- [ ] Existing links still work after organization changes.
- [ ] The change is committed from `refactor/resource-organization`.
- [ ] A pull request references this issue and receives review evidence before merge.
