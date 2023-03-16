on run argv
    tell application "Google Chrome"
        activate
        repeat with i from 1 to count of argv
            open location item i of argv
        end repeat
    end tell
end run
