from icalevents.icalevents import events
from datetime import datetime 
import pytz
from testinternetconnection import TestInternetConnection

TIMEZONE = "07:00"

def CurrentTime():
    pacific_tz = pytz.timezone('US/Pacific')
    current_time = datetime.now(pacific_tz)
    return current_time

class Activity:
    def __init__(self,event,calName):
        self.calName = calName
        self.name = event.summary.strip()
        self.start = event.start
        self.end = event.end
        self.all_day = event.all_day
        self.recurring = event.recurring
        self.status = event.status
        self.timeZone = str(self.start).split("-")[-1]
        if self.timeZone != TIMEZONE:
            self.timeZone = "ERROR WRONG TIMEZONE"
    
    def __str__(self):
        return f"{self.name} {self.start}"


    def TimeLeft(self, time=None):
        time = time or CurrentTime()
        return self.start - time


def GetCalendarNameAndUrl() -> list[(str,str)]:
    lst = []
    with open("./SecretCalendarLinks.txt","r") as file:
        for line in file:
            line = line.strip()
            splitLines = line.split(",")
            name = splitLines[0]
            url = splitLines[1]
            lst.append((name,url))
    return lst

def GetActivities() -> list[Activity]:
    activityList = []
    NameUrlList = GetCalendarNameAndUrl()
    for name, url in NameUrlList:
        for event in events(url):
            temp = Activity(event,name)
            activityList.append(temp)
    return activityList

def GetTodaysActivities(lst: list[Activity]) -> list[Activity]:
    today = CurrentTime().day
    todaysActivities = []
    for activity in lst:
        if activity.start.day == today and activity.TimeLeft().total_seconds() >= 0:
            todaysActivities.append(activity)
    todaysActivities = sorted(todaysActivities, key=lambda x: x.TimeLeft())
    return todaysActivities

def PrintActivities(lst: list[Activity]) -> None:
    longestCalName = max(len(a.calName) for a in lst)
    longestName = max(len(a.name) for a in lst)
    print(f"{'CalName': <{longestCalName}} {'Name': <{longestName}}")
    print("-" * (longestCalName + longestName + 30))
    for a in lst:
        tl = a.TimeLeft().total_seconds() / 3600
        print(f"{a.calName: <{longestCalName}} | {a.name: <{longestName}} | {a.start.day:>2} | {a.start.hour:>2}:{a.start.minute:<2} | {str(tl)}")


if TestInternetConnection():
    activities = GetActivities()
    todaysActivities = GetTodaysActivities(activities)
    PrintActivities(todaysActivities)
else:
    print("No internet!")

