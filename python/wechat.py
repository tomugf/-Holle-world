
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
    
def send_news():
    bot = Bot(cache_path=True)     #连接微信,会出现一个登陆微信的二维码
    contents = get_news()
    contents = contents[1:len(contents)-4]
    del contents[5]
    friend = bot.friends().search(u'.')[0]  #这里是你微信好友的昵称
    for content in contents:
        tt = str(content).split('、')
        aa = str(tt[1]).split('。')[0]
        friend.send(aa)
    
if __name__ == '__main__':
    t = Timer(1, send_news())
    t.start()   

        