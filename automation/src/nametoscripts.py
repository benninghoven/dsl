def NameToScripts(name: str) -> list[str]:
    lst = []

    if name == "Leet Code": # launch website
        file = "launchgooglewebsite.applescript"
        args = ["https://leetcode.com/problemset/all/",
                "https://www.bigocheatsheet.com/",
                ]
        lst.append(f"{file} {args}")

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
        args = ["iTerm"]
        lst.append(f"{file} {args}")

    else:
        pass
    return lst
