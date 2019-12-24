import requests
import json
import sys
import os

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
if len(sys.argv) >= 2:
    target = sys.argv[1]

    if len(sys.argv) < 3:
        date = "2018"
    else:
        date = sys.argv[2]

    print("\033[1;32;40m[+] Target ===> " + target + "\033[0m")
    print("\033[1;32;40m[+] Date ===> " + date + "\033[0m\n")
    r = requests.get("https://search-candidate.linternaute.com/bac/" + date + "/1?candidate-name=" + target)
    js = json.loads(r.text)

    if js['candidates']:
        print("Nom".ljust(33) + "Ville".ljust(33) + "Code Postal".ljust(33) + "Diplome".ljust(33) + "Academie")
        print("-" * 163)
        for x in js['candidates']:
            print(x['name'].ljust(30) + "|  " + str(x['cityLabel']).ljust(30) + "|  " + str(x['cityLink']).ljust(30) + "|  " + str(x['diplomaSerieLabel']).ljust(30) + "|  " + str(x['link']).ljust(30) + "|")
    else:
        print("No found !")
else:
    print("error")