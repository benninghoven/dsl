import subprocess

def ExecuteAppleCommand(scripts: str, absPath: str) -> None:

    if absPath == None:
        pass # do relative path instead
    if scripts == None:
        raise ValueError("must have a parameter")

    for script in scripts:
        fullScript = "osascript " + absPath + "/src/scripts/" + script
        process = subprocess.Popen(fullScript.split(), stdout=subprocess.PIPE)
