import os
import sys

cwd = os.getcwd()
parentPath = os.path.dirname(cwd)
print(parentPath)
sys.path.insert(0, parentPath)

from src.activity import 
