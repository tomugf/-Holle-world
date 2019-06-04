
import requests
from bs4 import BeautifulSoup


    
url = "http://www.buhuiwan.com/juzi/4508.html"
headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
              }  
response = requests.get(url,headers = headers)
html = response.text
soup = BeautifulSoup(html,'lxml')

contant = soup.find_all('p')

for n in range(1,len(contant)-4):
    if(n < 11):
        print(contant[n].text[2:])
    else:
        print(contant[n].text[3:])



