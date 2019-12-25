import requests
import json
import sys
import os

def banner():
    os.system("clear")
    print("""
                      ___.                         .__                         .__                             
    ___  __ __________\_ |__   ____  ______ ____   |  |__ _____  ______ ______ |__| ____   ____   ______ ______
    \  \/ // __ \_  __ \ __ \ /  _ \/  ___// __ \  |  |  \\\\__  \ \____ \\\\____ \|  |/    \_/ __ \ /  ___//  ___/
     \   /\  ___/|  | \/ \_\ (  <_> )___ \\\\  ___/  |   Y  \/ __ \|  |_> >  |_> >  |   |  \  ___/ \___ \ \___ \ 
      \_/  \___  >__|  |___  /\____/____  >\___  > |___|  (____  /   __/|   __/|__|___|  /\___  >____  >____  >
               \/          \/           \/     \/       \/     \/|__|   |__|           \/     \/     \/     \/ 
                                                                                                                \033[1;32;40m by Tamather \033[0m
            
    """)

def print_result(js, date):
    for x in js['candidates']:
        print("|  " + x['name'].ljust(30) + "|  ", end="")
        if 'cityLabel' in x.keys():
            print(str(x['cityLabel']).ljust(30) + "|  ", end="")
        else:
            print(''.ljust(30) + "|  ", end="")
        str(x['link'])[10:]
        print(str(date).ljust(30) + "|  " + str(x['diplomaSerieLabel']).ljust(30) + "|  " + str(x['link'])[10:].split("/")[0].ljust(30) + "|")


banner()
if len(sys.argv) >= 2:
    target = sys.argv[1]

    if len(sys.argv) < 3:
        date = 0
    else:
        date = int(sys.argv[2])

    print("\033[1;32;40m[+] Target ===> " + target + "\033[0m")
    print("\033[1;32;40m[+] Date ===> " + (str(date) if date else "2007 - 2019") + "\033[0m\n")

    print("   Nom".ljust(33) + "Ville".ljust(33) + "Date".ljust(33) + "Diplome".ljust(33) + "Academie")
    print("-" * 166)
    if date:
            r = requests.get("https://search-candidate.linternaute.com/bac/" + str(date) + "/1?candidate-name=" + target)
            js = json.loads(r.text)
            if js['candidates']:
                print_result(js, date)
    else:
        date = 2007
        while date <= 2019:
            r = requests.get("https://search-candidate.linternaute.com/bac/" + str(date) + "/1?candidate-name=" + target)
            js = json.loads(r.text)
            if js['candidates']:
                print_result(js, date)
            date = date + 1
    print("-" * 166)
else:
    print("error")