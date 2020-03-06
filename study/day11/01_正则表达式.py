import re

"""
一、Python3 正则表达式
"""

"""
1、re.match函数
   re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
"""

# 在起始位置匹配,只匹配出第一个
print("********** match() 方法 *********************")
matchObj = re.match("www", "www.google.com;www.baidu.com")
matchObj2 = re.match("(www)", "www.google.com;www.baidu.com")  # 获取匹配分组
print(matchObj.span())
print(matchObj.group())
print(matchObj.group(0))
# print(matchObj.group(1))
print(matchObj.groups())
print(matchObj2.groups())

# 不在起始位置匹配
matchobj3 = re.match("com", "www.tencent.com;www.qq.com")
print("matchObj3 = {}".format(matchobj3))

# 正则匹配
line = "Cats are smarter than dogs ..."
matchObj4 = re.match(r"(.*)\sare\s(.*?)\s.*", line)  # 非贪婪模式
print("matchObj4 = {}".format(matchObj4))
print(matchObj4.group())
print(matchObj4.group(0))
print(matchObj4.group(1))
print(matchObj4.group(2))
# 返回分组列表
print(matchObj4.groups())

"""
2、re.search方法
   re.search 扫描整个字符串并返回第一个成功的匹配。
"""
print("\n********** search() 方法 *********************")
line = "www.google.com; www.apple.com; www.qq.com"

matchObj5 = re.search(r"com", line)
print("matchObj5 = {}".format(matchObj5))
print(matchObj5.start())
print(matchObj5.end())
print(matchObj5.span())
print(matchObj5.group())
print(matchObj5.group(0))
# print(matchObj5.group(1))
# print(matchObj5.group(2))
print(matchObj5.groups())  # 没有分组

print("-" * 30)
line = "www.google.com; www.apple.com; www.qq.com"
matchObj6 = re.search(r"w{3}\.(.*)\..*w{3}\.(.*)\..*w{3}\.(.*)\..*", line)
print("matchObj6 = {}".format(matchObj6))
print(matchObj6.start())
print(matchObj6.end())
print(matchObj6.span())
print("matchObj6.group(): ", matchObj6.group())
print("matchObj6.group(0): ", matchObj6.group(0))
print("matchObj6.group(1): ", matchObj6.group(1))
print("matchObj6.group(2): ", matchObj6.group(2))
print("matchObj6.group(3): ", matchObj6.group(3))
print(matchObj6.groups())  # 分组列表

"""
3、re.match与re.search的区别
   re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
   而 re.search 匹配整个字符串，直到找到一个匹配。
"""
print("-" * 30)
line = "The cat loves to eat fish and shrimp ..."

matchObj = re.match(r"fish", line)
if matchObj:
    print("matchObj = {}".format(matchObj))
    print("matchObj.group() = {}".format(matchObj.group()))
else:
    print("matchObj = {}".format(matchObj))

matchObj = re.search(r"fish", line)
if matchObj:
    print("search, matchObj = {}".format(matchObj))
    print("search, matchObj.group() = {}".format(matchObj.group()))
else:
    print("search, matchObj = {}".format(matchObj))

"""
4、检索和替换
"""
print("**************检索和替换*********************")
phoneStr = "电话: 0859-3562-798,欢迎来电咨询!!!"

# 删除非号码
new_phone = re.sub(r".*:", "", phoneStr)
print(new_phone)
new_phone = re.sub(r",.*$", "", new_phone)
print(new_phone)
# new_phone = re.sub(r"[^0-9]","",new_phone)
# new_phone = re.sub(r"[^0-9]+", "", new_phone)
new_phone = re.sub(r"\D+", "", new_phone)
print(new_phone)

"""
5、compile 函数
   compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
"""
print("****************** compile 函数 ********************")
line = "one 123 two 3.14 three 489 five 987 ..."

# 用于匹配至少一个数字
pattern = re.compile(r"\d+")

# 查找头部，没有匹配
matchObj = pattern.match(line)
print("matchObj = {}".format(matchObj))

matchObj = pattern.match(line, 2)  # 从'e'的位置开始匹配，没有匹配
print("matchObj = {}".format(matchObj))

matchObj = pattern.match(line, 4)  # 从'1'的位置开始匹配，没有匹配
print("matchObj = {}".format(matchObj))

matchObj = pattern.match(line, 8)  # 从't'的位置开始匹配，没有匹配
print("matchObj = {}".format(matchObj))

# 查找头部，没有匹配
matchObj = pattern.search(line)
print("search, matchObj = {}".format(matchObj))

matchObj = pattern.search(line, 2)  # 从'e'的位置开始匹配，没有匹配
print("search, matchObj = {}".format(matchObj))

matchObj = pattern.search(line, 8)  # 从't'的位置开始匹配，没有匹配
print("search, matchObj = {}".format(matchObj))

"""
6、findall
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    注意： match 和 search 是匹配一次 findall 匹配所有。
    
    finditer 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
"""
line = "one 123 two 3.14 three 489 five 987 ..."

# 查找数字
pattern = re.compile(r"\d+.\d+")
digitals = pattern.findall(line)
print(digitals)

for i, number in enumerate(digitals):
    print("{} ==>> {}".format(i, number))

digitals = pattern.findall(line, 4, 20)
print(digitals)
for i, number in enumerate(digitals):
    print("{} ==>> {}".format(i, number))

print("*" * 30)
iter_digital = pattern.finditer(line)
for match in iter_digital:
    print(match.group())

"""
8、re.split
   split 方法按照能够匹配的子串将字符串分割后返回列表
"""
print("*" * 30)
line = "one,123,two 3.14,three 489, five 987, ..."
split_list = re.split(r",", line)
print(split_list)

split_list = re.split(r"[,|\s]\d+[,|\s]", line)
print(split_list)

split_list = re.split(r"[,|\s]\d+[,|\s]", line)
print(split_list)
