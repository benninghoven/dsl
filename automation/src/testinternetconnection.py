import urllib.request
import time
import subprocess

def TestInternetConnection():
    try:
        urllib.request.urlopen('https://www.google.com/', timeout=1)
        return True
    except urllib.error.URLError:
        return False
