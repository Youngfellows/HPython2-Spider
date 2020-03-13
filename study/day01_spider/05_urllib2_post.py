# coding=utf-8

import urllib
import urllib2
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "https://aidemo.youdao.com/trans"

# 完整的headers
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": " http://ai.youdao.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Referer": "http://ai.youdao.com/product-fanyi-text.s",
}

# 用户接口输入
key = raw_input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
    "q": key,
    "from": "Auto",
    "to": "Auto"
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data=data, headers=headers)

html = urllib2.urlopen(request).read().decode("utf-8")
print html

# unicode 转 中文
translate_results = json.loads(html)
results = translate_results["basic"]["explains"]
print ("翻译中文: {} ".format(translate_results["query"]))
print ("翻译结果: {} ".format(results))
i = 1
for english in results:
    print("{} {}".format(i, english))
    i += 1
