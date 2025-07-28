# MIORITIC INJECTOR - TROUBLESHOOTING GUIDE

## 🚨 **The Tool Won't Open - Here's How to Fix It!**

### **Option 1: Try the Command-Line Version (Recommended)**
If the GUI version isn't working, use the command-line version:

```bash
# Run the command-line version
./run_cli.sh
```

This version works without GUI and has all the same functionality!

### **Option 2: Try the Simple GUI Version**
```bash
# Run the simplified GUI version
source mioritic_env/bin/activate
python simple_mioritic.py
```

### **Option 3: Test Basic Functionality**
```bash
# Test if Python and tkinter work
python basic_test.py
```

### **Option 4: Manual Launch**
```bash
# Activate environment and run manually
source mioritic_env/bin/activate
python mioritic_injector.py
```

## 🔧 **Common Issues and Solutions:**

### **Issue 1: "No module named 'tkinter'"**
**Solution:**
```bash
sudo apt install python3-tk
```

### **Issue 2: "Permission denied"**
**Solution:**
```bash
chmod +x *.sh
chmod +x *.py
```

### **Issue 3: "Virtual environment not found"**
**Solution:**
```bash
python3 -m venv mioritic_env
source mioritic_env/bin/activate
pip install -r requirements.txt
```

### **Issue 4: "Import errors"**
**Solution:**
```bash
source mioritic_env/bin/activate
pip install requests beautifulsoup4 lxml
```

### **Issue 5: "Window doesn't appear"**
**Solution:**
- Try the command-line version instead
- Check if you're in a headless environment
- Use the CLI version: `./run_cli.sh`

## 🎯 **Quick Start - Command Line Version:**

The **command-line version** is the most reliable and has all the same features:

```bash
./run_cli.sh
```

Then enter:
1. **Target URL** (e.g., `http://example.com`)
2. **Injection word** (e.g., `hacked`)

The tool will:
- ✅ Scan ports
- ✅ Test vulnerabilities  
- ✅ Attempt injections
- ✅ Show real-time results

## 🚀 **All Available Versions:**

1. **`cli_mioritic.py`** - Command-line version (most reliable)
2. **`simple_mioritic.py`** - Simple GUI version
3. **`mioritic_injector.py`** - Full GUI version
4. **`basic_test.py`** - Basic functionality test

## 🎯 **Recommended Usage:**

```bash
# Use the command-line version (most reliable)
./run_cli.sh
```

This will work in any environment and has all the same scanning capabilities!

## ⚠️ **If Nothing Works:**

1. **Check Python installation:**
   ```bash
   python3 --version
   ```

2. **Check virtual environment:**
   ```bash
   ls -la mioritic_env/
   ```

3. **Reinstall dependencies:**
   ```bash
   source mioritic_env/bin/activate
   pip install --upgrade requests beautifulsoup4 lxml
   ```

4. **Use the command-line version** - it's the most reliable!

## 🎉 **Success Indicators:**

- ✅ Command-line version runs without errors
- ✅ You can enter URL and injection word
- ✅ Tool performs port scanning
- ✅ Tool shows vulnerability results
- ✅ Tool attempts injections

**The command-line version (`./run_cli.sh`) should work in any environment!**