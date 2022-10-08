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
            if int(place['xpostDate'][0:4]) >= 2015 :
                file.write(place["stitle"] + "," + place["address"][5:8] + "," + place["longitude"] + "," + place["latitude"] + "," + str('http'+place["file"].split("http")[1])+ "\n")


