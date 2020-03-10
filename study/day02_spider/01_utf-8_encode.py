# -*- coding:utf-8 -*-
import json

person = {"name": "老王", "age": 23, "address": "武当", "kongfu": "太极拳"}

print(person)

# 转化为json中文
json_str = json.dumps(person, ensure_ascii=False)
print(json_str)

# 转化为json中文
# json_str2 = json.dumps(person, ensure_ascii=False).decode('utf8').encode('gb2312')
json_str2 = json.dumps(person, ensure_ascii=False).decode('utf8')
print(json_str2)

with open('test.json', 'w') as fp:
    # fp.write(json_duanzi)
    json.dump(person, fp, ensure_ascii=False)
