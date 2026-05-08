# BOSC Community Library

BOSC Community Library is an open source education resource catalogue created for my BSCT 3221 Open Source Software exam at Bugema University. I am doing a Bachelor of Science in Software Engineering, and I built this project to practise how a real open source repository should be organized, documented, licensed, and maintained.

The idea behind the project is to collect and organize learning resources that can help schools, teachers, learners, and community study groups. The library focuses on open or reusable resources, low-bandwidth access, clear categories, and public contribution.

## Project Goals

- Create a structured index of open education resources.
- Use open source governance files such as a license, Code of Conduct, and contribution guide.
- Show a clear GitHub workflow using issues, branches, pull requests, and reviews.
- Support public-sector education by reducing dependence on closed proprietary platforms.
- Encourage future local language and community-based resource contributions.

## Repository Structure

```text
.
├── .github/                  # Issue and pull request templates
├── docs/                     # Proposal, reflection, audit log, and work plan
├── governance/               # Code of Conduct and Contributing guide
├── resources/                # Resource catalogue and category files
│   ├── categories/
│   ├── local-language/
│   └── resource-database.csv
├── scripts/                  # Utility scripts (Search tool)
├── LEGAL_ANALYSIS.md
├── LICENSE
├── README.md
└── SUSTAINABILITY.md
```

## Resource Categories

- [Digital Literacy](resources/categories/digital-literacy.md)
- [Open Science](resources/categories/open-science.md)
- [Teacher Training](resources/categories/teacher-training.md)
- [Civic Education](resources/categories/civic-education.md)
- [Local Language Support](resources/categories/local-language-support.md)
- [Luganda Summary](resources/local-language/luganda-summary.md)

The searchable resource index is stored in [resources/resource-database.csv](resources/resource-database.csv). You can search it using the [search_resources.py](scripts/search_resources.py) script.

## Contributing

Contributors should open an issue first, create a branch for the work, make a focused change, and then submit a pull request for review. This workflow is part of the exam requirement and also reflects normal open source practice.

See [governance/CONTRIBUTING.md](governance/CONTRIBUTING.md) for the full process.


## License

This project uses the Apache License 2.0. See [LICENSE](LICENSE) and [LEGAL_ANALYSIS.md](LEGAL_ANALYSIS.md) for the licensing explanation.

## Maintainer

Maintainer: Bazzenkya Francis  
Registration Number: 23/BSE/BU/R/0005  
Course: Bachelor of Science in Software Engineering, Bugema University
