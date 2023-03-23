import sys
import os

def AddSourceDirToPath():
    # Get the path to the parent directory (i.e. the project directory)
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the 'src' directory to the Python path
    sys.path.insert(0, os.path.join(parent_dir, 'src'))
