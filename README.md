# H4CK1NG_T00L v2.0

## Description

**H4CK1NG_T00L** is a comprehensive **penetration testing and security analysis** suite designed to offer a scalable and complete solution. This tool is aimed at both beginner and advanced users in the field of cybersecurity, with a focus on an **intuitive graphical interface** that makes common penetration testing tasks easier.

In this version 2.0, a modular structure has been implemented to allow for greater **scalability and ease of maintenance**. Each module is separated into individual scripts, which facilitates the addition of new features in the future.

## Project Structure

The project is organized as follows:

- **main.py**: The main file that starts the graphical interface and coordinates functionalities.
- **/gui**: Modules that handle the visual aspects of the tool.
  - `dark_theme.py`: Implements a dark theme for the GUI.
  - `frames.py`: Defines frames and windows for the interface.
- **/tools**: Modules containing the main analysis tools.
  - `dir_scanner.py`: Performs a dictionary-based analysis to find web directories.
  - `metadata_analyzer.py`: Extracts metadata from PDF and Word documents.
- **/utils**: Utility modules to manage various auxiliary functions.
  - `file_handler.py`: Manages necessary file operations.
  - `http_requests.py`: Handles HTTP/HTTPS requests for analysis functionalities.

## Features

### 1. Web Directory Analysis
- Conducts a dictionary-based scan to identify directories in a specified URL, checking their availability through HTTP/HTTPS requests.

### 2. Metadata Analysis
- Extracts metadata from PDF and Word documents, revealing potentially sensitive information such as author names, modification dates, and software details.

## Usage

To run the tool, simply execute `main.py`. The graphical interface will allow you to navigate through different functionalities, providing a smooth and user-friendly experience.

```bash
python main.py
