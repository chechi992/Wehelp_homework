import string
import urllib.request as req
import re
import bs4


# url = "https://www.ptt.cc/bbs/movie/index.html"
# request=req.Request(url, headers={
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
#     })

for page in range(9494,9504,1):

    url="https://www.ptt.cc/bbs/movie/index"+str(page)+".html"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53"
        })
        
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data,"html.parser")
        
        good = []
        simple = []
        bad = []
        title = root.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel 

        for s in title:
            if '好雷' in s.text :
                good.append(s.text)
                for i in good:
                    # with open("movie.txt","w",encoding="utf-8") as file:  
                    #     file.write(i+'\n')
                         print(i)
        for d in title:            
            if '普雷' in d.text :
                simple.append(d.text)
                for y in simple:
                    with open("movie.txt","w",encoding="utf-8") as file:  
                        print(y)
        for e in title:            
            if '負雷' in e.text :
                bad.append(e.text)
                for z in bad:
                    with open("movie.txt","a",encoding="utf-8") as file:  
                        file.write(z+'\n')
                        print(z)
                break


