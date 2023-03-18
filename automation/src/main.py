import sys
import datetime
from getparentdir import GetParentDir

projpath = GetParentDir()
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
from doestimematch import DoesTimeMatch

if __name__ == '__main__':
    if TestInternetConnection():

        ct = CurrentTime()
        ac = ActivityContainer(urlFilePath)
        todaysActivities = ac.TodaysActivities()

        if len(todaysActivities) and DoesTimeMatch(ct,todaysActivities[0].start):
            name = todaysActivities[0].name
            scripts = NameToScripts(name)
            ExecuteAppleCommand(scripts,projpath)
    else:
        print("no internet connection...")
