from utils import AddSourceDirToPath
from datetime import datetime, timedelta
AddSourceDirToPath()

from chrono import *

def test_DoesTimeMatch():

    a = b = CurrentTime() 
    assert DoesTimeMatch(a,b) == True

    now = datetime.now()
    now_plus_10 = now + timedelta(minutes = 10)
    assert DoesTimeMatch(now,now_plus_10) == False


