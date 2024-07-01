import os
import sys

# Modify this path to point to the folder containing auto_import.py
auto_import_folder = 'C:/Users/ryiij/OneDrive/Desktop/LeetCode'

# Append this folder to sys.path if it's not already there
if auto_import_folder not in sys.path:
    sys.path.append(auto_import_folder)

# Import your custom module to execute the imports
import auto_import