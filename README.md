# SecureNet Scanner

![SecureNet Scanner](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOLbOU-EGxnmG7lIuCaPq5F_No0qeHEcct0w&s) 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

SecureNet Scanner is an advanced network vulnerability scanner designed to identify potential security weaknesses in your network infrastructure. It provides automated reporting and remediation suggestions to help secure your systems.

## Features

- Scans specified IP ranges for vulnerabilities.
- Provides detailed reports in HTML format.
- Suggests remediation steps for identified vulnerabilities.
- User-friendly command-line interface.

## Installation

To set up the SecureNet Scanner, follow these steps:

1. **Clone the repository:**

   ```bash
   https://github.com/eugene12345678/SecureNet-Scanner.git
   cd SecureNet-Scanner
   ```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Install `wkhtmltopdf` for PDF generation (if needed):**

Follow the installation instructions from the wkhtmltopdf website.

## Usage
To run the SecureNet Scanner, use the following command:

```bash
python app.py
```
You will be prompted to enter an IP range to scan `(e.g., 192.168.1.0/24)`. After the scan completes, a report will be generated in HTML format.

### Example
```bash
Enter IP range to scan (e.g., 192.168.1.0/24): 172.20.10.0/24
```
## Technologies Used
- **Python:** Programming language for the application logic.
- **Flask:** Web framework for creating the web application.
- **Nmap:** Network scanning tool used for identifying vulnerabilities.
- **Scapy:** Python library for packet manipulation and analysis.
- **PDFKit:** Library for generating PDF reports.
- **HTML/CSS:** For report formatting.

## Contributing
Contributions are welcome! If you want to contribute to SecureNet Scanner, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or suggestions, please reach out to me at:

[Eugene Mathenge](eugenemathenge4@gmail.com)





