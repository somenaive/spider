import requests
from bs4 import BeautifulSoup
import sys
import io
import ck

# 登录后才能访问的网页

def getHtml(url):
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = ck.ck

    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    # 设置请求头
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    # 在发送get请求时带上请求头和cookies
    resp = requests.get(url, headers=headers, cookies=cookies)
    return resp.content.decode('utf-8')

def saveImg(imgSrc):
    i=0
    for url in imgSrc:
        i+=1
        path='./img/'+str(i)+'.jpg'
        print(path)
        with open(path, 'wb') as f:
            f.write(requests.get(url).content)


if __name__=='__main__':
    url = 'https://www.zhihu.com/topic/20022251/hot'
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    src = []
    for im in soup.find_all('img'):
        src.append(im.attrs['src'])

    saveImg(src)

