import requests,re, json
import html
from app.models import db,Articles

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db_config import Config


cookies = {
    'RK': 'D2UJ1Su71w',
    'ptcz': 'd18e7d4917bff661087236e1d1610c39484b8f0a1685e28301b0b9d349fcb511',
    'rewardsn': '',
    'wxtokenkey': '777',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'http://cic.isc.org.cn/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'RK=D2UJ1Su71w; ptcz=d18e7d4917bff661087236e1d1610c39484b8f0a1685e28301b0b9d349fcb511; rewardsn=; wxtokenkey=777',
}
result={}
url="https://mp.weixin.qq.com/s/C1jsAd9YpZeg0z42PVH-pw"
res = requests.get(url, cookies=cookies, headers=headers)
lis=[]
# print(res.text)
all_p=re.findall(r'<(?:section|p)(.*?)(?:</section>|</p>)',res.text)
with open('ISC.txt','w+',encoding='utf-8') as f:
    f.write(res.text)
# all_p=re.findall(r'<p(.*?)</p>',res.text)
title=re.findall(r'<h1 class="rich_media_title " id="activity-name">\s*(.*?)\s*</h1>',res.text,re.S)[0]
timestamp=re.findall(r"var oriCreateTime = '(.*?)';",res.text)[0]

for p in all_p:
    img=re.findall(r'src="(.*?)"',p)
    if img:
        image=f"<img src='{img[0]}' referrerPolicy='no-referrer'>"
        lis.append(image)
    text=''.join(re.findall(r'>(.*?)<',p))
    text=html.unescape(text)
    if text!='':
        lis.append(text)
result['title']=title
result['content']=lis[1:-3]
result['timestamp']=timestamp

# result['content'] = [f"<img src='{img}' referrerPolicy='no-referrer'>" if img.startswith('http') else img for img in result['content']]
r=json.loads(json.dumps(result, ensure_ascii=False))
Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
try:
    new_article = Articles(
        title=title,
        content=r,
        timestamp=timestamp
    )
    # print(type(r))
    session.add(new_article)
    session.commit()
    print(f"插入成功，ID: {new_article.id}")
except Exception as e:
    session.rollback()
    print("插入失败:", str(e))
finally:
    session.close()



