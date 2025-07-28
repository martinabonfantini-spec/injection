#!/usr/bin/env python3
"""
Debug test for Mioritic Injector
"""

print("=== DEBUG TEST STARTED ===")

try:
    print("Testing basic imports...")
    import tkinter as tk
    print("✓ tkinter imported successfully")
    
    from tkinter import ttk, messagebox, scrolledtext
    print("✓ tkinter widgets imported successfully")
    
    import threading
    print("✓ threading imported successfully")
    
    import socket
    print("✓ socket imported successfully")
    
    import requests
    print("✓ requests imported successfully")
    
    from bs4 import BeautifulSoup
    print("✓ BeautifulSoup imported successfully")
    
    import random
    print("✓ random imported successfully")
    
    import ssl
    print("✓ ssl imported successfully")
    
    print("✓ All imports successful!")
    
    # Test basic tkinter functionality
    print("Testing tkinter functionality...")
    root = tk.Tk()
    root.withdraw()  # Hide the window
    print("✓ tkinter window created successfully")
    root.destroy()
    print("✓ tkinter window destroyed successfully")
    
    print("=== ALL TESTS PASSED ===")
    print("The tool should work fine!")
    
except Exception as e:
    print(f"✗ ERROR: {str(e)}")
    print("This is what's preventing the tool from opening")