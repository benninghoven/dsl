tell application "System Events"
    tell process "SystemUIServer"
        set isMenuVisible to (menu bar item "Displays" of menu bar 1 exists)
        if not isMenuVisible then
            click (menu bar item "Displays" of menu bar 1)
        end if
        tell (menu item "Connect to Sidecar Display" of menu of menu bar item "Displays" of menu bar 1)
            click
        end tell
    end tell
end tell

