import time
import subprocess

while True:
    print("Please sip some water")
    subprocess.run([
        "osascript", "-e",
        'display notification "You need to drink some water" with title "Please drink some water"'
    ])
    time.sleep(1800)  # Reminds every 30 minutes (change as needed)
