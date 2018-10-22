import requests
import sys
import io
import ck

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

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

url = 'http://zhihu.com'


f=open('zh.txt','w',encoding='utf-8')
f.write(getHtml(url))
f.close()
