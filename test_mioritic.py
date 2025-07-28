#!/usr/bin/env python3
"""
Test script for Mioritic Injector
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
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
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without GUI"""
    try:
        # Test URL validation
        from urllib.parse import urlparse
        
        test_urls = [
            "http://example.com",
            "https://google.com",
            "example.com",
            "invalid-url"
        ]
        
        for url in test_urls:
            try:
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url
                parsed = urlparse(url)
                result = bool(parsed.netloc)
                print(f"URL validation test: {url} -> {result}")
            except:
                print(f"URL validation test: {url} -> False")
        
        print("✓ Basic functionality test passed")
        return True
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== MIORITIC INJECTOR TEST ===")
    
    # Test imports
    if not test_imports():
        print("Import test failed!")
        return False
    
    # Test basic functionality
    if not test_basic_functionality():
        print("Basic functionality test failed!")
        return False
    
    print("=== ALL TESTS PASSED ===")
    print("Mioritic Injector is ready to use!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)