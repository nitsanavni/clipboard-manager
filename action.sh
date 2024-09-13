#!/bin/bash
osascript -e 'tell application "Terminal"
    activate
    do script "python3 \"/Users/nitsanavni/code/clipboard-manager/copy_from_clipboard.py\" && exit"
end tell'

