import sys

projpath = "/Users/devin/Sandbox/dsl/automation"
sys.path.append(projpath)

from src.activitycontainer import ActivityContainer
from src.testinternetconnection import TestInternetConnection
from src.currenttime import CurrentTime
from src.nametoscripts import NameToScripts
from src.executecommands import ExecuteAppleCommand

urlFilePath = projpath + "/data/SecretCalendarLinks.txt"

phoneNumberPath = projpath + "/data/phonenumber.txt"
with open(phoneNumberPath, 'r') as file:
    phoneNumber = file.read()

if __name__ == '__main__':
    if TestInternetConnection():
        scripts = NameToScripts("Code")
        ExecuteAppleCommand(scripts,projpath)
    else:
        print("no internet connection...")

"""
        ct = CurrentTime()
        ac = ActivityContainer(urlFilePath) # Might take long
        todaysActivities = ac.TodaysActivities()
        if len(todaysActivities):
            for a in todaysActivities:
                script = NameToScript(a.name)
                if script:
                    scriptPath = projpath + "/src/scripts/"
                    scriptPath += NameToScript(a.name)
                    ExecuteCommand("osascript " + scriptPath)
                    print(a.name, scriptPath)
                else:
                    print(a.name, "No script!")
                    """
