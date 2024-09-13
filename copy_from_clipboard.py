#!/usr/bin/env python3
import json
import os
import subprocess

HISTORY_FILE = os.path.expanduser("~/.clipboard_history.json")

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def copy_to_clipboard(text):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def fzf_select(items):
    input_str = '\0'.join(items)
    
    try:
        result = subprocess.run([
            'fzf',
            '--read0',
            '--highlight-line',
            '--preview', 'echo {} | head -n 10',
            '--preview-window', 'right:50%:wrap'
        ], input=input_str, text=True, capture_output=True)
        
        if result.returncode == 0:
            return result.stdout.rstrip('\0')
    except subprocess.CalledProcessError:
        pass
    return None

def main():
    history = load_history()
    if not history:
        print("No clipboard history available.")
        return

    selected = fzf_select(history)
    if selected:
        copy_to_clipboard(selected)
        print(f"Copied to clipboard: {selected[:50].replace(chr(10), '␤')}...")
    else:
        print("No selection made.")

if __name__ == "__main__":
    main()
