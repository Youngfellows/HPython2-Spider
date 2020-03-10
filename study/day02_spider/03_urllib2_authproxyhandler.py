# coding=utf-8
import urllib2

# 设置代理
# authproxy_handler = urllib2.ProxyHandler({"http": "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
authproxy_handler = urllib2.ProxyHandler({"http": "113.87.224.16:9000"})
# authproxy_handler = urllib2.ProxyHandler({"http": "114.215.104.49:16816"})

opener = urllib2.build_opener(authproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib2.install_opener(opener)

# 获取请求
url = "http://www.baidu.com/"
request = urllib2.Request(url)

# 获取响应
response = opener.open(request)

# 获取响应的html信息
html = response.read()

print(html)
