# coding=utf-8

import urllib
import urllib2
import ssl

url = "http://www.baidu.com/s"

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

keyword = raw_input("清输入您要查询的关键字: ")

wd = {"wd": keyword}

# 通过urllib.urlencode() 参数是一个dict类型
wd = urllib.urlencode(wd)

# 拼接完整的url
# https://www.baidu.com/s?wd=美女
fullurl = url + "?" + wd

# 构造请求对象
request = urllib2.Request(fullurl, headers=ua_headers)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

print(html)
