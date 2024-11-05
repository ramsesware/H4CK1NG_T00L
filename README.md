# H4CK1NG_T00L v2.3

## Description

**H4CK1NG_T00L** is a comprehensive **penetration testing and security analysis** suite designed to offer a scalable and complete solution. This tool is aimed at both beginner and advanced users in the field of cybersecurity, with a focus on an **intuitive graphical interface** that makes common penetration testing tasks easier.

In version 2.3, a vulnerability scanner module has been added, enabling users to scan specified IP addresses for open ports and services. This functionality expands the tool's capabilities by allowing for a more thorough vulnerability assessment. The modular structure of the tool continues to support scalability and easy maintenance.

--- 

## Project Structure

The project is organized as follows:

- **main.py**: The main file that starts the graphical interface and coordinates functionalities.
- **/gui**: Modules that handle the visual aspects of the tool.
  - `dark_theme.py`: Implements a dark theme for the GUI.
  - `frames.py`: Defines frames and windows for the interface.
- **/tools**: Modules containing the main analysis tools.
  - `dir_scanner.py`: Performs a dictionary-based analysis to find web directories.
  - `metadata_analyzer.py`: Provides functionality for analyzing and removing metadata from documents.
  - `vulnerability_scanner.py`: Scans specified IP addresses to identify open ports and potential vulnerabilities.
- **/utils**: Utility modules to manage various auxiliary functions.
  - `file_handler.py`: Manages necessary file operations.
  - `http_requests.py`: Handles HTTP/HTTPS requests for analysis functionalities.

--- 

## Features

### 1. Web Directory Analysis
- Conducts a dictionary-based scan to identify directories in a specified URL, checking their availability through HTTP/HTTPS requests.

### 2. Metadata Analysis and Removal
- **Metadata Analysis**: This functionality extracts metadata from PDF and Word documents, revealing potentially sensitive information such as author names, modification dates, and software details.
- **Metadata Removal**: In addition to analysis, this version introduces the ability to remove metadata from documents. Users can remove metadata from a single document or from all documents within a specified directory, helping prevent unintentional exposure of sensitive information during document sharing or storage.
  
### 3. Vulnerability Port Scanning
- **Port and Service Scanning**: Scans a specified IP address for open ports (within the range 0-10000) and identifies active services. This scanner uses Nmap for identifying open ports and services.
- **Detailed Results**: Displays each detected open port, its associated service (if identified), and the current state, providing a comprehensive view of the target's surface vulnerabilities.

### Dependencies:
- `tkinter`
- `requests`
- `PyPDF2`
- `python-docx`
- `piexif`
- `Pillow`
- `python-nmap`

--- 

## Usage

To run the tool, simply execute `main.py`. The graphical interface will allow you to navigate through different functionalities, providing a smooth and user-friendly experience.

```bash
python main.py
