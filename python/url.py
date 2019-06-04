from threading import Timer
from bs4 import BeautifulSoup
from wxpy import Bot
import requests

def get_news():
    url = "http://www.buhuiwan.com/juzi/4508.html"
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
              }  
    response = requests.get(url,headers = headers)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    content = soup.find_all('p')
    return content

if __name__ == "__main__":
    con = get_news()
    con = con[1:len(con)-4]
    del con[5]
    for i in con:
        tt = str(i).split('、')
        aa = str(tt[1]).split('。')[0]
        print(aa)
        