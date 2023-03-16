import os

def GetParentDir() -> str:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    return parent_directory

