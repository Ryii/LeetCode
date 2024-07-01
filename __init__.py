import sys
import os

# Get the current directory of this __init__.py file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directory containing auto_import.py to sys.path
auto_import_dir = os.path.join(current_dir, '')
sys.path.append(auto_import_dir)