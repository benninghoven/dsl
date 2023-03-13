from activity import Activity
# NOT WORKING

class ActivityContainer:
    def __init__(self,lst: list[Activity]):
        if lst == None:
            raise ValueError("parameter required")
        self.activityList = lst
    
    def __str__(self):
        return f"pizza"

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

