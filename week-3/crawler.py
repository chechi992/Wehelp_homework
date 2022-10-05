import urllib.request as req
import re

# url = "https://www.ptt.cc/bbs/movie/index.html"
# request=req.Request(url, headers={
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
#     })

for page in range(9494,9504):

    url="https://www.ptt.cc/bbs/movie/index"+str(page)+".html"
    request=req.Request(url, headers={
     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
     })
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data,"html.parser")

    with open("movie.txt","w",encoding="utf-8") as file:
        titles = root.find_all("div",class_="title")
        for title in titles:
            if title.a !=None and '好' in title.a.string  :
                file.write(title.a.string+"\n")
