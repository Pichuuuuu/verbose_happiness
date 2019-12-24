import requests
import json
import sys

target = sys.argv[1]
date = "2018"


r = requests.get("https://search-candidate.linternaute.com/bac/" + date + "/1?candidate-name=" + target)
js = json.loads(r.text)

if js['candidates']:
    print("Nom".ljust(33) + "Ville".ljust(33) + "Code Postal".ljust(33) + "Diplome".ljust(33) + "Academie")
    print("-" * 163)
    for x in js['candidates']:
        print(x['name'].ljust(30) + "|  " + str(x['cityLabel']).ljust(30) + "|  " + str(x['cityLink']).ljust(30) + "|  " + str(x['diplomaSerieLabel']).ljust(30) + "|  " + str(x['link']).ljust(30) + "|")
else:
    print("No found !")