# encoding: utf-8

from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.ptt.cc/bbs/HatePolitics/index.html')
soup = BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for line in soup.select('.r-ent'):
    s1 = line.select('.date')[0].text.encode('utf-8').decode('utf-8')
    s2 = line.select('.author')[0].text.encode('utf-8').decode('utf-8')
    s3 = line.select('.title')[0].text.encode('utf-8').decode('utf-8')
   
    s4 = ''
    line4 = line.select('.item')
    if len(line4) > 0:
        s4 = line4[0].text.encode('utf-8').decode('utf-8')
    
    s5 = soup.select('.board')[0].text.encode('utf-8').decode('utf-8')
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    
