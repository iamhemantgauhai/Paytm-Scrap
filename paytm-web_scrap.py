from bs4 import BeautifulSoup
import requests,json
from pprint import pprint
list2=[]
for i in range(1,14):
    url=("https://paytmmall.com/shop/search?q=pickle&from=organic&child_site_id=6&site_id=2&category=101405&page="+str(i))
    page= requests.get(url)
    soup= BeautifulSoup(page.text,'html.parser')
    
    name=soup.find_all(class_="UGUy")
    rr=[]
    for i in name:
        rr.append(i.text)

    price=soup.find_all(class_="_1kMS")
    b=[]
    for j in price:
        b.append(j.text)
    ss=[]
    for i,g,m in zip(rr,rr,b): 
        jjj=(i[-5:])
        
    
        dic={'gram':jjj,'name':g,'price':m}
        list2.append(dic)
    print(list2)
    with open('pay.json','w')as f:
        f.write(json.dumps(list2,indent=4))
        f.close()
#........................................................Patyam_Completed........................................................#