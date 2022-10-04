#網路連線
import urllib.request as request
import json
import re
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src)as response: 
    data = json.load(response)
    clist=data["result"]["results"]
    with open("data.csv","w",encoding="utf-8") as file:
        for place in clist:
            file.write(place["stitle"] + "," + place["address"][5:8] + "," + place["longitude"] + "," + place["latitude"] + "," + place["file"].re.findall("https:[^:]+.jpg",string) + "\n")


