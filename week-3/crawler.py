import urllib.request as req
import re

# url = "https://www.ptt.cc/bbs/movie/index.html"
# request=req.Request(url, headers={
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
#     })

for page in range(9494,9599,1):

    url="https://www.ptt.cc/bbs/movie/index"+str(page)+".html"
    request=req.Request(url, headers={
     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
     })
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4
    root = bs4.BeautifulSoup(data,"html.parser")

    with open("movie.txt","a",encoding="utf-8") as file:
        titles = root.find_all("div",class_="title")
        for title in titles:
            if title.a !=None and '好雷' in title.a.string  :
                file.write(title.a.string+"\n")
        for title_pu in titles:
            if title_pu.a !=None and '普雷' in title_pu.a.string  :
                file.write(title_pu.a.string+"\n")
        for title_fu in titles:
            if title_fu.a !=None and '負雷' in title_fu.a.string  :
                file.write(title_fu.a.string+"\n")




