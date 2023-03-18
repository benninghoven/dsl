def NameToScripts(name: str) -> str:

    scripts = []

    name = name.upper()

    if "LEET CODE" in name:
        script = "launchgooglewebsite.applescript https://www.bigocheatsheet.com/ https://leetcode.com/problemset/all/"
        scripts.append(script)

    elif "CODE" in name:
        script = "launchgooglewebsite.applescript https://github.com/benninghoven?tab=repositories https://chat.openai.com/chat https://music.youtube.com/"
        scripts.append(script)
        script = "openapp.applescript iTerm"
        scripts.append(script)

    elif "STUDY" in name:
        script = "launchgooglewebsite.applescript https://www.fullerton.edu/ecs/cs/resources/advisement.php https://chat.openai.com/chat https://learn.zybooks.com/library https://csufullerton.instructure.com/"
        scripts.append(script)

    return scripts
