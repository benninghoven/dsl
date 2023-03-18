import os
import sys
import time

projpath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(projpath)

from src.activitycontainer import ActivityContainer
from src.testinternetconnection import TestInternetConnection
from src.currenttime import CurrentTime
from src.nametoscripts import NameToScripts
from src.executecommands import ExecuteAppleCommand
from src.doestimematch import DoesTimeMatch

urlFilePath = projpath + "/data/SecretCalendarLinks.txt"
phoneNumberPath = projpath + "/data/phonenumber.txt"
with open(phoneNumberPath, 'r') as file:
    phoneNumber = file.read()


if __name__ == '__main__':

    ac = ActivityContainer(urlFilePath)
    todaysActivities = ac.TodaysActivities()

    ct = CurrentTime()

    name = todaysActivities[0].name

    scripts = NameToScripts(name)
    ExecuteAppleCommand(scripts,projpath)
