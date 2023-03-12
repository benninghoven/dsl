from icalevents.icalevents import events
from datetime import datetime 
import pytz

TIMEZONE = "07:00"

def CurrentTime():
    pacific_tz = pytz.timezone('US/Pacific')
    current_time = datetime.now(pacific_tz)
    return current_time


class Activity:
    def __init__(self,event,calName):
        self.calName = calName
        self.name = event.summary
        self.start = event.start
        self.end = event.end
        self.all_day = event.all_day
        self.recurring = event.recurring
        self.status = event.status
        self.timeZone = str(self.start).split("-")[-1]
        if self.timeZone != TIMEZONE:
            self.timeZone = "ERROR WRONG TIMEZONE"
    
    def __str__(self):
        return f"""[{self.calName} {self.name}] {self.start.hour}:{self.start.minute} starts in: {self.TimeLeft()}"""

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
    todaysActivities = []
    for activity in lst:
        if activity.TimeLeft().days == 0:
            todaysActivities.append(activity)
    return todaysActivities

todaysActivities = GetTodaysActivities(GetActivities())

for act in todaysActivities:
    print(act)
