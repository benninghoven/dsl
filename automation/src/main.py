from activitycontainer import ActivityContainer
from testinternetconnection import TestInternetConnection

urlFilePath = "../data/SecretCalendarLinks.txt"

if __name__ == '__main__':
    if TestInternetConnection():
        b = ActivityContainer(urlFilePath)
        print(b.PrintActivities(b.TodaysActivities()))
    else:
        print("no internet connection...")
