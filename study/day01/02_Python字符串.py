# 1.字符串的连接
str1 = '加油'
str2 = "武汉..."
str3 = str1 + str2
print(str3)

# 2.字符串的合并
# Join将序列中的多个字符串，合并成一个字符串
# 语法：任意字符串.join(多字符串组成的序列)
urlList = ['www', 'google', 'com']
url = '.'.join(urlList)
print(url)

# 3.字符串相乘
line = "*" * 30
print(line)

# 4.字符串切片
# 字符串、列表、元组都支持切片操作，主要是在对象中截取一部分元素的操作
# 序列切片语法：序列[开始下标位置:结束下标位置:步长]
# 步长：步长的意思就是选取数据的间隔，默认为1，如果为负数，那么就是从后往前面开始截取,也就是有一个倒序开始截取

# 正数步长操作
str4 = "apple orange banana china ben"
subStr1 = str4[0:9]  # 取第1個到第9個字符你
print(subStr1)
subStr2 = str4[-6:]
print(subStr2)  # 从倒数第6个字符到字符串结束的字符
subStr3 = str4[-6:-4]
print(subStr3)  # 从倒数第6个字符到倒数第4个字符
subStr4 = str4[-6:-9]  # 从倒数第6个字符到倒数第9个字符,向右边开始截取,无法截取到字符
print(subStr4)

# 注意：截取的数据是不包含结束位置下标的数据
str5 = '0123456789'
subStr5 = str5[2:11:1]
print(subStr5)
subStr6 = str5[2:11:2]
print(subStr6)
subStr7 = str5[2:11]
print(subStr7)
subStr8 = str5[::2]
print(subStr8)
subStr9 = str5[2::]
print(subStr9)

# 负数步长操作
# 注意：如果选取方向（下标开始到结束的方向）和步长的方向冲突，将无法截取数据
str6 = "0123456789"
print(str6[11:0:-1])
print(str6[8:3:-2])
print(str6[-5:-1])

# 5.字符串的分割
# 普通的分割，用split
# split只能做非常简单的分割，而且不支持多个分隔
phone = '400-800-8888-1345'
phoneResult = phone.split('-')  # 分割结果是列表
print(phoneResult)

# 复杂的分割,正则表达式
# r表示不转义,分隔符可以是;或者,或者空格后面跟0个多个额外的空格，然后按照这个模式去分割
import re

line = "hello world;python, I ,like,     it"
reResult = re.split(r'[;,\t]+', line)
print(reResult)

line1 = 'abc aa;bb,cc | dd(xx).xxx 12.12        ssssss'
# 按空格切
# split(分割符，分割次数[可以省略])
# 分割，返回一个列表，但是分割符会丢失
print(re.split(r' +', line1))
# 加将空格放可选框内[]内
print(re.split(r'[ ]+', line1))

# 按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[^\t\n\r\f\v]
print(re.split(r'[\s]+', line1))

# 多字符匹配
print(re.split(r'[\s;,.]+', line1))

# 使用括号捕获分组，默认保留分割符
print(re.split(r'([;])', line1))

# 去掉分隔符，加?:
print(re.split(r'(?:;)', line1))

# 6.字符串的开头和结尾的处理
fileName = 'apple.java'
print(fileName.startswith('apple2'))
print(fileName.endswith('.java'))

# 7. 字符串的查找和匹配
# 一般查找
# 我们可以很方便的在长的字符串里面查找子字符串，会返回子字符串所在位置的索引, 若找不到返回-1
title = 'python can be easy to pick up and powerful languages'
print(title.find("pick up"))

# 复杂的匹配,正则匹配
dateTime = "11/27/2020"
if re.match(r'^\d+/\d+/\d+$', dateTime):
    print("ok,match..")
else:
    print('not match...')

# 8.字符串的替换
# 普通的替换//用replace就可以
text = 'python can be easy to study, powerful languages'
print(text.replace("study", "learn"))

# 复杂的替换//若要处理复杂的或者多个的替换，需要用到re模块的sub函数
students = "Boy 103,girl 105"
print(re.sub(r'[0-9]+', "120", students))
print(re.sub(r'\d+', "122", students))

# 9.字符串中去掉一些字符
# 去除空格//对文本处理的时候比如从文件中读取一行，然后需要去除每一行的两侧的空格，table或者是换行符
# 注意:字符串内部的空格不能去掉，若要去掉需要用re模块
line = "     恭喜你,   你  通 过了...   "
print(line.strip())
print(re.sub(r'\s+', "", line))

# 常用操作方法
# find():监测某个子串是否包含在这个字符串中，如果存在将返回下标位置，不存在则返回-1
# 语法：字符串.find(字符串，开始下标位置，结束下标位置)
# 注意：开始下标和结束下标的位置如果省略就表示在整个字符串中查找
# index() 与上面的find()操作一致，只是没有找到将会抛出异常

str1 = "学习Python使用快乐...Python很简单..."
print(str1.find("Py"))
print(str1.find("Py", 1, 9))
print(str1.index("Py"))
print(str1.index("Py", 1, 9))
print(str1.find("Py2"))
try:
    print(str1.index("Py2"))
except ValueError:
    print("没找到Py2")

print("统计Python个数:%d" % str1.count("Python"))
# rfind(),返回最后一个出现的位置下标
print(str1.rfind("Python"))

# replace()替换字符串
# 字符串.replace(旧子串，新子串，替换次数)
# 注意：替换次数如果查找到子串出现的次数，则替换次数为该子串出现的次数,默认替换所有

str2 = "我是Java,Java可以做很多东西，你喜欢Java吗"
newStr = str2.replace("Java", "C++")
print(newStr)
newStr1 = str2.replace("Java", "php", 2)  # 只修改2次java子串
print(newStr1)


#一些不常用的字符串函数
str1 = "    python python python python "
# capitalize将第一个字符大写
print(str1.capitalize())
# title() 将所有的单词首字符大写
print(str1.title())
# lower() 将所有字符转成小写
print(str1.lower())
# upper 将所有字符转成大写
print(str1.upper())
# lstrip 删除左则空字符,rstrip 删除右侧空字符
print(str1.lstrip().rstrip())
# strip删除2侧空字符
print(str1.strip())

# ljust不够10个字符使用点来填充左对齐
str1 = "hello"
print(str1.ljust(10,"."))
print(str1.ljust(10))#空格填充

# rjust不够10个字符使用点来填充右对齐
print(str1.rjust(10,"."))
print(str1.rjust(10))

# 判断子串是否在字符串中开头或者结尾
str1 = "pythonwqewqrwqrqwrerewdsfgdsfghello"
# 字符串.startswith(子串,开始位置,截止位置) 判断该子串是否在字符串开始位置
print(str1.startswith("python"))
# 字符串.endswith(子串,开始位置,截止位置) 判断该子串是否在字符串结尾位置
print(str1.endswith("hello2"))

# isalpha/isdigit/isalnum/isspace
# isalpha判断是否是字符串中所有的字符是不是字母,如果不是全部字母返回False
# isdigit判断字符串中是不是只包含数字,如果是则返回True
# isalnum只要字符中包含数字即返回True
# isspace 判断是否全部是空字符

str1 = "hello1234"
str2 = "hello"

# isalpha判断是否是字符串中所有的字符是不是字母,如果不是全部字母返回False
print(str1.isalpha())
print("*"*30)
print(str2.isalpha())
# isdigit判断字符串中是不是只包含数字,如果是则返回True
str3 = "44444"
print(str3.isdigit())
# isalnum只要字符中包含数字即返回True
print(str1.isalnum())
# isspace 判断是否全部是空字符
str4 = " "
print(str4.isspace())