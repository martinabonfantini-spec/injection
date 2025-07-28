#!/bin/bash

# Launch Mioritic Injector
cd "$(dirname "$0")"
source mioritic_env/bin/activate
python mioritic_injector.py
