from icalevents.icalevents import events
import subprocess
import time

# TODO: Cache the data! Update it once a day or manually

def CheckCurrentTimeAgainstString(compareTime="12:00"):
    current_time = time.localtime()
    hour = compareTime.split(":")[0]
    minute = compareTime.split(":")[1]
    return current_time.tm_hour == int(hour) and current_time.tm_min == int(minute)

def LoadCalendarEvents():
    urls = []
    with open("./SecretCalendarLinks.txt","r") as urlLinksFile:
        for line in urlLinksFile:
            line = line.strip()
            urls.append(line)
    return urls


urls = LoadCalendarEvents()

class Activity:
    def __init__(self, name, hour, minute):
        self.name = name
        self.hour = hour
        self.minute = minute
    
    def __str__(self):
        return f"{self.name} - {self.hour}:{self.minute}"

def sort_by_time(obj):
    return int(obj.hour), int(obj.minute)

todayActivities = []

for url in urls:
    es  = events(url)
    for e in es:
        tl = e.time_left()
        if tl.days == 0: # stuff will happen in less then a day
            eventName = e.summary
            timeList= str(tl).split(":")
            hoursLeft = timeList[0]
            minsLeft = timeList[1]
            temp = Activity(eventName,hoursLeft,minsLeft)
            todayActivities.append(temp)

sorted_list = sorted(todayActivities, key=sort_by_time)

for i,x in enumerate(sorted_list):
    print(i,x)




