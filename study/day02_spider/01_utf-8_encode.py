# -*- coding:utf-8 -*-
import json

person = {"name": "老王", "age": 23, "address": "武当", "kongfu": "太极拳"}

print("type:%s,%s" % (type(person), person))

# 1. 将python对象编码成Json字符串,转化为json中文
json_str = json.dumps(person, ensure_ascii=False)
print("type:%s,%s" % (type(json_str), json_str))

# 将python对象编码成Json字符串,转化为json中文
# json_str2 = json.dumps(person, ensure_ascii=False).decode('utf8').encode('gb2312')
json_str2 = json.dumps(person, ensure_ascii=False).decode('utf8').encode("utf-8")
print("type:%s,json_str2=%s" % (type(json_str2), json_str2))

# 2. 将python中的对象转化成json储存到文件中
with open('test.json', 'w') as fp:
    json.dump(person, fp, ensure_ascii=False)

# 3. 将Json字符串解码成python对象
laowang = json.loads(json_str2)
print("type:%s,%s" % (type(laowang), laowang))
new_result = json.dumps(laowang, ensure_ascii=False)  # 参考网上的方法，***ensure_ascii***设为False
print new_result

# 4. 将文件中的json的格式转化成python对象提取
with open("test.json", "r") as fp:
    laowang1 = json.load(fp, encoding="utf-8")
    print("type:%s,%s" % (type(laowang1), laowang1))
    new_result = json.dumps(laowang1, ensure_ascii=False)  # 参考网上的方法，***ensure_ascii***设为False
    print new_result

# 5. Pythonython实现的json文件读取及中文乱码显示问题解决方法
# Python使用json.loads之后打印中文会出现乱码的问题，解决方法如下：
with open('lxml/json/city.json', 'r') as json_file:
    """
    读取该json文件时，先按照gbk的方式对其解码再编码为utf-8的格式
    """
    # data = json_file.read().decode(encoding='gbk').encode(encoding='utf-8')
    data = json_file.read().decode(encoding='utf-8').encode(encoding='utf-8')  # 读取json文件
    print type(data)  # type(data) = 'str'
    print data
    result = json.loads(data)  # 将Json字符串解码成python对象
    print ("xxx: %s" % result)
    # 将python对象编码成Json字符串,转化为json中文
    new_result = json.dumps(result, ensure_ascii=False)  # 参考网上的方法，***ensure_ascii***设为False
    print new_result
