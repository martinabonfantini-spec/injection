#!/usr/bin/env python3

print("Testing basic Python functionality...")

try:
    import tkinter as tk
    print("✓ tkinter imported successfully")
    
    # Create a simple window
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("300x200")
    
    label = tk.Label(root, text="MIORITIC INJECTOR TEST")
    label.pack(pady=50)
    
    print("✓ Window created successfully")
    print("If you see a window, the tool should work!")
    print("Close the window to continue...")
    
    root.mainloop()
    
except Exception as e:
    print(f"✗ ERROR: {e}")
    print("This is preventing the tool from opening")