from icalevents.icalevents import events
from .currenttime import CurrentTime

class Activity:
    def __init__(self,event = None ,calName = None):
        if event == None and calName == None:
            raise ValueError("both parameters are required")
        self.calName = calName
        self.name = event.summary.strip()
        self.start = event.start
        self.end = event.end
        self.all_day = event.all_day
        self.recurring = event.recurring
        self.status = event.status
        self.timeZone = str(self.start).split("-")[-1]
    
    def __str__(self):
        return f"{self.name} {self.start}"


    def TimeLeft(self, time=None):
        time = time or CurrentTime()
        return self.start - time

