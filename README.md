# Mioritic Injector

An advanced web injection tool for testing vulnerabilities and injecting content into web applications.

## Features

- **Port Scanning**: Scans for open ports on target systems
- **Vulnerability Testing**: Tests for common web vulnerabilities
- **SQL Injection Testing**: Automated SQL injection vulnerability detection
- **XSS Testing**: Cross-site scripting vulnerability detection
- **Content Injection**: Attempts to inject custom text into web pages
- **Real-time Logging**: Live progress updates and detailed logging
- **Modern GUI**: Dark-themed interface with professional appearance

## Installation

### Prerequisites
- Python 3.6 or higher
- pip3 package manager

### Quick Setup
1. Clone or download the project files
2. Run the installation script:
   ```bash
   chmod +x install_and_run.sh
   ./install_and_run.sh
   ```

### Manual Installation
1. Install Python dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python3 mioritic_injector.py
   ```

## Usage

1. **Launch the Application**: Run `python3 mioritic_injector.py`

2. **Enter Injection Word**: Type the word you want to inject into the target

3. **Enter Target URL**: Provide the URL of the target website

4. **Start Injection**: Click "START INJECTION" to begin the process

5. **Monitor Progress**: Watch the real-time log for detailed progress updates

## What the Tool Does

### Step 1: URL Validation
- Validates the target URL format
- Ensures proper URL structure

### Step 2: Port Scanning
- Scans common ports (21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080, 8443)
- Identifies open ports on the target system

### Step 3: Vulnerability Scanning
- Checks for missing security headers
- Tests for server information disclosure
- Scans for sensitive directories and files

### Step 4: Content Analysis
- Analyzes webpage content
- Identifies potential injection points
- Attempts to inject custom text into page elements

### Step 5: SQL Injection Testing
- Tests URL parameters for SQL injection vulnerabilities
- Uses common SQL injection payloads
- Detects SQL error messages in responses

### Step 6: XSS Testing
- Tests for Cross-Site Scripting vulnerabilities
- Uses various XSS payloads
- Checks for reflected XSS in responses

## Security Notice

⚠️ **IMPORTANT**: This tool is designed for educational and authorized security testing purposes only. Always ensure you have proper authorization before testing any website or system. Unauthorized testing may be illegal.

## Features

- **Real-time Progress**: Live updates during scanning and testing
- **Comprehensive Logging**: Detailed logs of all activities
- **Thread-safe Operations**: Non-blocking GUI during operations
- **Error Handling**: Robust error handling and recovery
- **Professional UI**: Modern dark-themed interface

## Technical Details

- **Language**: Python 3
- **GUI Framework**: tkinter
- **HTTP Library**: requests
- **HTML Parsing**: BeautifulSoup4
- **Threading**: Multi-threaded operations for responsive UI

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Permission Errors**: Ensure the script is executable:
   ```bash
   chmod +x mioritic_injector.py
   ```

3. **Network Issues**: Check your internet connection and firewall settings

4. **Target Not Responding**: Verify the target URL is accessible

## License

This tool is provided for educational purposes. Use responsibly and only on systems you own or have explicit permission to test.

## Disclaimer

The authors are not responsible for any misuse of this tool. Users are responsible for ensuring they have proper authorization before testing any systems.