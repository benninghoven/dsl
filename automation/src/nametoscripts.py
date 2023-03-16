def NameToScripts(name: str) -> list[str]:
    lst = []
    if name == "Leet Code": # launch website
        file = "launchgooglewebsite.applescript"
        args = [
                "https://www.bigocheatsheet.com/",
                "https://leetcode.com/problemset/all/",
                ]
        argString = ""
        for arg in args:
            argString += arg
            argString += " "
        lst.append(f"{file} {argString}")

    elif name == "Code": # launch iterm2,website

        file = "launchgooglewebsite.applescript"
        args = [
                "https://music.youtube.com/",
                "https://github.com/benninghoven?tab=repositories",
                "https://chat.openai.com/chat",
                ]
        argString = ""
        for arg in args:
            argString += arg
            argString += " "
        lst.append(f"{file} {argString}")

        file = "openapp.applescript"
        args = "iTerm"
        lst.append(f"{file} {args}")

    elif "Study Block" in name:
        file = "launchgooglewebsite.applescript"
        args = [
                "https://www.fullerton.edu/ecs/cs/resources/advisement.php",
                "https://chat.openai.com/chat",
                "https://learn.zybooks.com/library",
                "https://csufullerton.instructure.com/",
                ]
        argString = ""
        for arg in args:
            argString += arg
            argString += " "
        lst.append(f"{file} {argString}")
    else:
        pass
    return lst
