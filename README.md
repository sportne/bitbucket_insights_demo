# Bitbucket Insights Report Demo

This demo project uses the [atlassian-python-api](https://github.com/atlassian-api/atlassian-python-api) to create a Bitbucket Code Insights report and then add annotations to that report. It also logs the equivalent curl commands for each HTTP request to help with debugging.

The insights report includes:
- One string field (e.g. a descriptive message)
- One number field (e.g. a score or count)
- One annotation with fields such as a message, a line number, and a severity

> **Note:** Adjust the Bitbucket server URL, credentials, project key, repository slug, commit ID, and report key to match your environment.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Configuration & Debug Logging](#configuration--debug-logging)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

---

## Overview

This demo illustrates how to:
- Create a Code Insights report on a Bitbucket instance using the `create_code_insights_report` method.
- Add annotations to the report using the `add_code_insights_annotations_to_report` method.
- See detailed debug output (including an equivalent curl command) generated by the atlassian‑python‑api library for each HTTP request.

---

## Prerequisites

- **Python 3.6+** (Python 3.8 or later is recommended)
- Access to a Bitbucket Server instance (self-hosted) with Code Insights enabled
- Valid Bitbucket credentials (username/password or token)
- Git (to clone the repository, if necessary)

---

## Project Structure

The project is organized as follows:

```
demo_project/
├── README.md         # This documentation file
├── setup.sh          # Setup script to create a virtual environment and install dependencies
└── demo.py           # Demo script to create a report and add annotations
```

---

## Setup Instructions

### 1. Clone the Repository or Create the Project Directory

If you haven’t already, create a directory for the project:

```bash
mkdir demo_project
cd demo_project
```

Then, create the files as outlined in this README (or clone your own repository with these files).

### 2. Setup the Virtual Environment

Run the provided `setup.sh` script. This script checks for an existing virtual environment, creates one if needed, and installs the required package:

```bash
./setup.sh
```

*If you are on Windows, you can execute the equivalent commands in PowerShell:*

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install atlassian-python-api
```

### 3. Activate the Virtual Environment

Before running the demo, activate the virtual environment:

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

- **Windows:**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

---

## Usage

Once your environment is set up and activated, run the demo script:

```bash
python demo.py
```

The demo script will:
1. Create a Code Insights report with a specified report key and title.
2. Post report data that includes a string field (`"This is a demo string"`) and a number field (`42`).
3. Add an annotation (with a message, a line number, and a severity level) to the report.
4. Log all HTTP request details—including a generated curl command—for debugging purposes.

You should see log output similar to:

```
2025-02-14 18:00:00 atlassian.rest_client DEBUG: curl --silent -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' --data '{"string_field": "This is a demo string", "number_field": 42}' 'http://localhost:7990/rest/api/latest/insights/…'
Created report: { ... }
2025-02-14 18:00:05 atlassian.rest_client DEBUG: curl --silent -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' --data '{"annotations": [...]}' 'http://localhost:7990/rest/api/latest/insights/…'
Added annotations: { ... }
```

---

## Black Formatter

This uses [Black](https://github.com/psf/black) for code formatting. To format the code manually, run:

```bash
black .
```

This will reformat all Python files in the project according to Black's standards.

---

## Configuration & Debug Logging

The demo script configures Python’s logging system to output DEBUG-level messages. This is done via `logging.basicConfig(...)` in the demo script, which ensures that internal debug messages—such as the output from the `log_curl_debug` method—are printed to the console.

If you want to adjust the log level or format, modify the following section in `demo.py`:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s"
)
```

This configuration is essential for seeing the curl command representations of HTTP requests, which you can copy and execute manually if needed.

---

## Troubleshooting

- **No Debug Output:**  
  If you do not see the curl debug commands, verify that the logging level is set to DEBUG and that no other logger configuration overrides your settings.

- **Authentication Errors:**  
  Make sure your Bitbucket credentials (username, password, or token) and URL are correct. Adjust these values in `demo.py`.

- **Virtual Environment Issues:**  
  If the setup script reports that the virtual environment already exists, try removing the `venv` directory and re-running `setup.sh`.

- **Network Issues:**  
  Ensure that your Bitbucket server is accessible from your machine and that any required network proxies or firewall rules are properly configured.

---

## Contributing

Contributions to this demo project are welcome! If you have suggestions, improvements, or bug fixes:
- Fork the repository.
- Create a new branch for your changes.
- Submit a pull request with a detailed explanation of your changes.

For larger changes or feature requests, please open an issue in the repository.

---

## License

This demo project is provided under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See the LICENSE file for details.

---

## References

- [atlassian-python-api GitHub Repository](https://github.com/atlassian-api/atlassian-python-api)
- [Bitbucket Code Insights REST Documentation](https://docs.atlassian.com/bitbucket-server/rest/6.6.1/bitbucket-code-insights-rest.html)
- [Method: `create_code_insights_report`](https://github.com/atlassian-api/atlassian-python-api/blob/master/atlassian/bitbucket/__init__.py#L2594)
- [Method: `add_code_insights_annotations_to_report`](https://github.com/atlassian-api/atlassian-python-api/blob/master/atlassian/bitbucket/__init__.py#L2545)

---

By following these instructions, you should have a fully functional demo project that creates a Bitbucket insights report, posts an annotation, and logs detailed HTTP request data (including curl commands) for debugging. Enjoy exploring and customizing the demo!
