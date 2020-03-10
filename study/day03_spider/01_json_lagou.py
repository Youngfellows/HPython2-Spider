# coding=utf-8
import urllib2
# json解析库，对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath

# 拉钩接口
url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"

# 请求的User-Agent头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# 构造请求
request = urllib2.Request(url, headers=headers)

# 获取请求响应
response = urllib2.urlopen(request)

#  取出json文件里的内容，返回的格式是字符串
html = response.read()
print(html)

# 把json形式的字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)

# Python形式的列表,解析name属性
city_list = jsonpath.jsonpath(unicodestr, "$..name")
for city in city_list:
    print(city)

# dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
# 禁用ascii编码格式，返回的Unicode字符串，方便使用
# array = json.dumps(city_list)
array = json.dumps(city_list, ensure_ascii=False)

print("type(array):{}".format(type(array)))
print(array)
# 将Unicode字符串以utf-8编码写人文件
with open("./json/lagou_city.json", "wb") as fp:
    fp.write(array.encode("utf-8"))
