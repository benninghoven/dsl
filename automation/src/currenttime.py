from datetime import datetime 
import pytz

def CurrentTime():
    pacific_tz = pytz.timezone('US/Pacific')
    current_time = datetime.now(pacific_tz)
    return current_time
