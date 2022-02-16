import subprocess
from unittest import result

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profile:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<3}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<3}|  {:<}".format(i, "None"))
input("\n\nPress enter to continue...")       
