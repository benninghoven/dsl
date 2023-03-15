import subprocess
import os
import sys

#cmd += f"sendtext.applescript {phoneNumber} {a.name}"

projpath = "/Users/devin/Sandbox/dsl/automation"
sys.path.append(projpath)

from src.activitycontainer import ActivityContainer
from src.testinternetconnection import TestInternetConnection
from src.currenttime import CurrentTime

urlFilePath = projpath + "/data/SecretCalendarLinks.txt"
phoneNumberPath = projpath + "/data/phonenumber.txt"
with open(phoneNumberPath, 'r') as file:
    phoneNumber = file.read()

def NameToCommand(name: str) -> str:
    cmd = "osascript "
    cmd += projpath
    cmd += "/src/scripts/"
    if name == "Leet Code":
        cmd += "launchgooglewebsite.applescript"
        # arg here
    elif name == "":
        cmd = ""
        pass
    else:
        cmd = ""
        pass
    return cmd

# Execute the command
def ExecuteCmd(command):
    if not command:
        return
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)


if __name__ == '__main__':
    if TestInternetConnection():
        ct = CurrentTime()
        ac = ActivityContainer(urlFilePath) # Might take long
        todaysActivities = ac.TodaysActivities()
        if len(todaysActivities):
            for a in todaysActivities:
                print(a)
                cmd = NameToCommand(a.calName)
                ExecuteCmd(cmd)
    else:
        print("no internet connection...")
