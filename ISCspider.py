import requests,re
import html

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

res = requests.get('https://mp.weixin.qq.com/s/8eZ1YQ0wqmyv2dpG0P8nmg', cookies=cookies, headers=headers)
lis=[]
# print(res.text)
# all_p=re.findall(r'<(?:section|p)(.*?)(?:</section>|</p>)',res.text)
all_p=re.findall(r'<p(.*?)</p>',res.text)
for p in all_p:
    img=re.findall(r'src="(.*?)"',p)
    if img:
        print(img)
        lis.append(img[0])
    text=''.join(re.findall(r'>(.*?)<',p))
    text=html.unescape(text)
    if text!='':
        print(text)
        lis.append(text)
print(lis)
n=0
for i in lis:
    if i.startswith('http'):
        n+=1
