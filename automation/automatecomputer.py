from icalevents.icalevents import events

TIMEZONE = "07:00"

class Activity:
    def __init__(self,event,calName):
        self.calName = calName
        self.name = event.summary
        self.start = event.start
        self.end = event.end
        self.all_day = event.all_day # bool
        self.recurring = event.recurring
        self.status = event.status
        self.timeZone = str(self.start).split("-")[-1]
    
    def __str__(self):
        if self.timeZone != TIMEZONE:
            self.timeZone = "ERROR WRONG TIMEZONE"
        return f"""[{self.calName} - {self.name}] {self.start.hour}:{self.start.minute}"""


def GetCalendarNames() -> list[str]:
    lst = []
    with open("./SecretCalendarLinks.txt","r") as urlLinksFile:
        for line in urlLinksFile:
            line = line.strip()
            lst.append(line.split(",")[0])
    return lst

def GetCalendarURLs() -> list[str]:
    urls = []
    with open("./SecretCalendarLinks.txt","r") as urlLinksFile:
        for line in urlLinksFile:
            line = line.strip()
            urls.append(line.split(",")[-1])
    return urls

def GetCurWeekActivities(urls) -> list[events]:
    lst = []
    names = GetCalendarNames()
    for i, url in enumerate(urls):
        activities = events(url)
        for activity in activities:
            temp = Activity(activity,names[i])
            lst.append(temp)
    return lst

lst = GetCurWeekActivities(GetCalendarURLs())

for x in lst:
    print(x)
