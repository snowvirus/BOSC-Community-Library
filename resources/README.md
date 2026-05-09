# Resources Directory

The `resources/` directory contains the learning catalogue used by the BOSC Community Library. It is the community-facing part of the repository where learners, teachers, and contributors can find or improve resource entries.

## Structure

```text
resources/
├── categories/              # Markdown summaries grouped by education topic
├── local-language/          # Local language summaries and translation support
├── README.md
└── resource-database.csv    # Structured resource index used by scripts
```

## Category Files

- [Digital Literacy](categories/digital-literacy.md)
- [Open Science](categories/open-science.md)
- [Teacher Training](categories/teacher-training.md)
- [Civic Education](categories/civic-education.md)
- [Local Language Support](categories/local-language-support.md)

## Local Language Files

- [Luganda Summary](local-language/luganda-summary.md)

## Resource Database

The CSV file [resource-database.csv](resource-database.csv) is the structured catalogue. Each row should include the resource ID, title, category, provider, location, license, audience, connectivity requirement, summary, and review status.

## Maintenance Notes

- Keep category summaries readable for non-technical contributors.
- Keep CSV entries aligned with the related category markdown files.
- Mark unclear resource licenses as `Review` instead of treating them as reusable.
- Prefer low-bandwidth and offline-friendly notes where they help schools or community study groups.
