from activitycontainer import ActivityContainer
from testinternetconnection import TestInternetConnection
from currenttime import CurrentTime
import subprocess

urlFilePath = "../data/SecretCalendarLinks.txt"

#FIXME make a command parser

if __name__ == '__main__':
    if TestInternetConnection():
        ct = CurrentTime()
        b = ActivityContainer(urlFilePath) # Might take long
        todaysActivities = b.TodaysActivities()
        if len(todaysActivities):
            cur = todaysActivities[0]
            # NOT WORKING
            # maybe does not have the current one
            if cur.start.hour == ct.hour and cur.start.minute == ct.minute:
                cmd = "osascript "
                cmd += "./launchleetcode.apple"
                subprocess.call(cmd, shell=True)
    else:
        print("no internet connection...")
