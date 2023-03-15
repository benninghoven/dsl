import subprocess
import os
import sys

cwd = os.getcwd()
parentPath = os.path.dirname(cwd)
print(parentPath)
sys.path.insert(0, parentPath)

from src.activitycontainer import ActivityContainer
from src.testinternetconnection import TestInternetConnection
from src.currenttime import CurrentTime

urlFilePath = "../data/SecretCalendarLinks.txt"
phoneNumberPath = "../data/phonenumber.txt"
with open(phoneNumberPath, 'r') as file:
    phoneNumber = file.read()

def NameToCommand(name: str) -> str:
    cmd = "osascript "
    cmd += parentPath
    cmd += "/src/scripts/"
    if name == "Leet Code":
        cmd += "launchgooglewebsite.applescript"
        # arg here
    elif name == "":
        pass
    else:
        cmd += f"sendtext.applescript {phoneNumber} {a.name}"
    return cmd

# Execute the command
def ExecuteCmd(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)


if __name__ == '__main__':
    if TestInternetConnection():
        ct = CurrentTime()
        ac = ActivityContainer(urlFilePath) # Might take long
        todaysActivities = ac.TodaysActivities()
        if len(todaysActivities):
            for a in todaysActivities:
                cmd = NameToCommand(a.calName)
                ExecuteCmd(cmd)
    else:
        print("no internet connection...")
