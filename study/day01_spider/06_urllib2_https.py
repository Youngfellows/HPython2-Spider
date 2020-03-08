# coding=utf-8

import urllib2
import ssl

# 忽略SSL安全认证
context = ssl._create_unverified_context()

url = "https://www.12306.cn/index/"
# url = "https://www.baidu.com/"

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# 获得Request
request = urllib2.Request(url, headers=ua_headers)

# 添加到context参数里
response = urllib2.urlopen(request, context=context)

# 获取响应
html = response.read()

print(html)
