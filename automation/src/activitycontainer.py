from .activity import Activity
from .currenttime import CurrentTime
from .float_to_time import FloatToTime
import datetime
from icalevents.icalevents import events


class ActivityContainer:
    def __init__(self,filePath):
        if filePath == None:
            raise ValueError("filepath is required")
        self.filePath = filePath
        self.activityList = []
        self.GetActivities()
    
    def __str__(self):
        return f"{self.activityList}"

    def ReadFile(self):
        lst = []
        with open(self.filePath,"r") as file:
            for line in file:
                line = line.strip()
                splitLines = line.split(",")
                name = splitLines[0]
                url = splitLines[1]
                lst.append((name,url))
        return lst

    def GetActivities(self):
        NameUrlList = self.ReadFile()
        for name, url in NameUrlList:
            for event in events(url,start = CurrentTime() - datetime.timedelta(minutes=1)):
                temp = Activity(event,name)
                self.activityList.append(temp)

    def TodaysActivities(self) -> list[Activity]:
        today = CurrentTime().day
        todaysActivities = []
        for activity in self.activityList:
            if activity.start.day == today and activity.TimeLeft().total_seconds() >= -60:
                todaysActivities.append(activity)
        todaysActivities = sorted(todaysActivities, key=lambda x: x.TimeLeft())
        return todaysActivities

    def PrintActivities(self, lst = None):
        if lst == None:
            print("NONE PROVIDED")
            lst = self.activityList
        if len(lst) == 0:
            print("no activities left for today")
            return
        longestCalName = max(len(a.calName) for a in lst)
        longestName = max(len(a.name) for a in lst)
        ct = CurrentTime()
        print(f"current time [{ct.hour:>2}:{ct.minute:<2}]")
        print(" day| start | left | name ")
        print("-" * 50)
        for a in lst:
            tl = a.TimeLeft().total_seconds() / 3600
            output = ""
            output += f" {a.start.day:<2} |"
            output += f" {a.start.hour:>2}:{a.start.minute:<2} |"
            output += f" {FloatToTime(tl)} |"
            output += f" {a.name:<{longestName}} |"
            print(output)

