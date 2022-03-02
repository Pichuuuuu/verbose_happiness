from nbformat import write
import requests
import json
import sys
import os
from prettytable import PrettyTable

tab = PrettyTable()
tab.field_names = ["Nom", "Ville", "Date", "Diplome", "Académie"]

def banner():
    os.system("clear")
    print("""\033[1;31;60m
                      ___.                         .__                         .__                             
    ___  __ __________\_ |__   ____  ______ ____   |  |__ _____  ______ ______ |__| ____   ____   ______ ______
    \  \/ // __ \_  __ \ __ \ /  _ \/  ___// __ \  |  |  \\\\__  \ \____ \\\\____ \|  |/    \_/ __ \ /  ___//  ___/
     \   /\  ___/|  | \/ \_\ (  <_> )___ \\\\  ___/  |   Y  \/ __ \|  |_> >  |_> >  |   |  \  ___/ \___ \ \___ \ 
      \_/  \___  >__|  |___  /\____/____  >\___  > |___|  (____  /   __/|   __/|__|___|  /\___  >____  >____  >
               \/          \/           \/     \/       \/     \/|__|   |__|           \/     \/     \/     \/ 
                                                                                                                \033[0m
            
    """)

banner()
if len(sys.argv) >= 2:
    target = sys.argv[1]
    if len(sys.argv) < 3:
        date = 0
    else:
        date = int(sys.argv[2])
    print("\033[1;32;60m[+] Target ===> " + target + "\033[0m")
    print("\033[1;32;60m[+] Date ===> " + (str(date) if date else "2007 - 2021") + "\033[0m\n")
    if date:
            r = requests.get("https://search-candidate.linternaute.com/bac/" + str(date) + "/1?candidate-name=" + target)
            js = json.loads(r.text)
            if js['candidates']:
                for x in js['candidates']:
                    if 'cityLabel' in x.keys():
                        tab.add_row([x['name'], x['cityLabel'], date, x['diplomaSerieLabel'], x['link'][10:].split("/")[0]])
                    else:
                        tab.add_row([x['name'], "", date, x['diplomaSerieLabel'], x['link'][10:].split("/")[0]])
    else:
        date = 2007
        while date <= 2021:
            r = requests.get("https://search-candidate.linternaute.com/bac/" + str(date) + "/1?candidate-name=" + target)
            js = json.loads(r.text)
            if js['candidates']:
                    for x in js['candidates']:
                        if 'cityLabel' in x.keys():
                            tab.add_row([x['name'], x['cityLabel'], date, x['diplomaSerieLabel'], x['link'][10:].split("/")[0]])
                        else:
                            tab.add_row([x['name'], "", date, x['diplomaSerieLabel'], x['link'][10:].split("/")[0]])
            date = date + 1
        print("\033[1;32;60mdone!\033[0m")
    print(tab)
else:
    print("use -> run.py [target] or run.py [target] [date]")
    print("target format -> 'nom' or 'nom prenom'")
    print("date format -> YYYY")
    print("\033[1;31;60moldest date is 2007!\033[0m")