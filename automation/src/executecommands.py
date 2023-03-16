import subprocess

def ExecuteAppleCommand(commands: list[str], absPath: str):
    if absPath == None:
        pass # do relative path instead
    if commands == None:
        raise ValueError("Must have two parameters")
    for command in commands:
        fullCmd = "osascript "
        fullCmd += absPath + "/src/scripts/"
        fullCmd += command
        process = subprocess.Popen(fullCmd.split(), stdout=subprocess.PIPE)

