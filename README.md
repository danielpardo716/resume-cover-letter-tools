# Resume & Cover Letter Tools
This repository contains tools for programmatically building resumes and cover letters. Documents are based on templates and filled with data from a structured format to provide a single source of truth.

For resumes, there are three templates:
- Plaintext - for pasting in text boxes
- Minimalist - minimalist, ATS-friendly resume
- Two-Column - eye-catching resume to send directly to network connections

Cover letters can also be generated to be consistent with the two-column resume format.

# Dependencies
This project uses [uv](https://docs.astral.sh/uv/) for dependency management and Python versioning. The following Python libraries were used:
- [jinja2](https://jinja.palletsprojects.com/en/stable/) - templating engine
- [pyyaml](https://pyyaml.org/) - YAML parsing. YAML was chosen over JSON because it's a little more human-readable.

## VSCode Extensions
The following extensions were used for ease of use:
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
    - For building LaTeX documents, a TeX distribution must be installed on the system. In this project, [MiKTeX](https://miktex.org/) was used.
- [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml)

# Usage
After cloning and making sure dependencies are installed, simply run ```uv run source/main.py```.