import os
import random

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "new_file.txt")

file_path += str(random.randint(1,10000))

with open(file_path, "w") as file:
    file.write("This is a new file created with Python!")
