import sys
import datetime

projpath = "/Users/devin/Sandbox/dsl/automation"
sys.path.append(projpath)

urlFilePath = projpath + "/data/SecretCalendarLinks.txt"
phoneNumberPath = projpath + "/data/phonenumber.txt"
with open(phoneNumberPath, 'r') as file:
    phoneNumber = file.read()

from src.activitycontainer import ActivityContainer
from src.testinternetconnection import TestInternetConnection
from src.currenttime import CurrentTime
from src.nametoscripts import NameToScripts
from src.executecommands import ExecuteAppleCommand

def DoesTimeMatch(td1, td2) -> bool:
    return td1.hour == td2.hour and td1.minute == td2.minute

        #scripts = NameToScripts("Leet Code")
        #ExecuteAppleCommand(scripts,projpath)
if __name__ == '__main__':
    if TestInternetConnection():
        ct = CurrentTime()
        ac = ActivityContainer(urlFilePath)
        todaysActivities = ac.TodaysActivities()
        if len(todaysActivities) and DoesTimeMatch(ct,todaysActivities[0].start):
            name = todaysActivities[0]
            name = "Code"
            scripts = NameToScripts(name)
            ExecuteAppleCommand(scripts,projpath)
    else:
        print("no internet connection...")

"""
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
