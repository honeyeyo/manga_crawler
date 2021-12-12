from time import sleep

import requests
from bs4 import BeautifulSoup
from config import Config

def htmlParse(f,i):
    started = False;
    config = Config().fetch()
    url = "https://mox.moe/l/all,all,%E5%AE%8C%E7%B5%90,score,all,all,BL/"+str(i)+".htm"
    print(url)
    html = requests.get(url, cookies=config["account"], headers = {"user-agent": config["ua"]}).text

    soup = BeautifulSoup(html, "html.parser")

    if not started:
        tag = soup.find_all('td',attrs={"class": "listtitle"})[1]
        # print(type(tag))
        print(tag.get_text())
        started = True

    result = soup.find_all('tr',attrs={"class": "listbg"})

    for item in result:
        for item2 in item.find_all('a'):
            if item2.string != None:
                print(item2.string)
                f.write(item2.string)
                f.write('\n')

    sleep(1)

filename = "MangaList.txt"
mf = open(filename, "a+", encoding='utf-8')
i = 1
while(i<=50):
    htmlParse(mf,i)
    print('page ', i)
    i+=1

mf.close
#
# ml = open(filename, "w", encoding='utf-8')
# ml.write(html)
# ml.close()


