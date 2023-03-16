on run argv
    repeat with appName in argv
        tell application "System Events"
            set isRunning to (count of (every process whose name is appName)) > 0
        end tell
        
        if not isRunning then
            tell application appName to activate
        end if
    end repeat
end run

