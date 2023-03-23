from datetime import datetime 
import pytz

def CurrentTime():
    pacific_tz = pytz.timezone('US/Pacific')
    current_time = datetime.now(pacific_tz)
    return current_time

def DoesTimeMatch(td1, td2) -> bool:
    return td1.hour == td2.hour and td1.minute == td2.minute

def FloatToTime(float_hours):
    hours = int(float_hours)
    minutes = int((float_hours - hours) * 60)
    return f"{hours}:{minutes:02d}"
