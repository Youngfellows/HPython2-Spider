"""
Python 的字符串内建函数
Python 的字符串常用内建函数如下：

序号	方法及描述

capitalize()
将字符串的第一个字符转换为大写

center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常.

isalnum()
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False

isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False

isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

islower()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False

isspace()
如果字符串中只包含空白，则返回 True，否则返回 False.

istitle()
如果字符串是标题化的(见 title())则返回 True，否则返回 False

isupper()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

len(string)
返回字符串长度

ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

lower()
转换字符串中所有大写字符为小写.

lstrip()
截掉字符串左边的空格或指定字符。

maketrans()
创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)
返回字符串 str 中最大的字母。

min(str)
返回字符串 str 中最小的字母。

replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

rfind(str, beg=0,end=len(string))
类似于 find()函数，不过是从右边开始查找.

rindex( str, beg=0, end=len(string))
类似于 index()，不过是从右边开始.

rjust(width,[, fillchar])
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

rstrip()
删除字符串字符串末尾的空格.

split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

strip([chars])
在字符串上执行 lstrip()和 rstrip()

swapcase()
将字符串中大写转换为小写，小写转换为大写

title()
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

translate(table, deletechars="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中

upper()
转换字符串中的小写字母为大写

zfill (width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0

isdecimal()

检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
"""

str1 = "welcome to china,welcome to beijing"
print(str1.capitalize())
print(str1.center(50, "*"))
print("字符c出现的次数:%d" % (str1.count("c")))
print("字符串to出现的次数:%d" % (str1.count("to")))

address = "中国北京,美国洛杉矶,韩国首尔,日本东京"
addr_utf8 = address.encode("UTF-8")  # UTF-8编码
addr_gbk = address.encode("GBK")  # GBK编码
print("origin: ", address)
print("UTF-8编码: ", addr_utf8)
print("GBK编码: ", addr_gbk)
print("UTF-8解码: ", addr_utf8.decode("UTF-8", "strict"))
print("GBK解码: ", addr_gbk.decode("GBK", "strict"))

if (address.startswith("中国")):
    print("字符串以\'中国\'开始...")

if (address.endswith("北京")):
    print("字符串以\'北京\'结尾...")
else:
    print("字符串没有以\'北京\'结尾...")

index = address.find("国")
index2 = address.find("美")
print("查找的索引: %d" % index)
print("查找的索引: %d" % index2)
print("右边开始查找索引: %d" % address.rfind("北京", 2))
print("右边开始查找索引: %d" % address.rindex("日本", 2))

index3 = address.index("北")
print("查找的索引: %d" % index3)

try:
    index4 = address.index("苹")  # 查找不到抛出异常
    print("查找的索引: %d" % index4)
except ValueError:
    print("没查找到字符")

str = "hellolaowang"
str1 = "hello beijing"
print("是否至少有一个数字或字符:%s" % (str.isalnum()))
print("是否至少有一个字符:%s" % (str.isalpha()))

print("是否至少有一个数字或字符:%s" % (str1.isalnum()))
print("是否至少有一个字符:%s" % (str1.isalpha()))

str2 = "3.14"
str3 = "679"
print("是否是数字:%s" % str2.isdigit())
print("是否是数字:%s" % str3.isdigit())

price = "4.78"
length = "327"
print("是否只包含数字字符: %s" % price.isnumeric())
print("是否只包含数字字符: %s" % length.isnumeric())

company = "google"
emptyStr = "\t\n"
emptyStr2 = "                    "
print("是否只包含空白字符: %s" % company.isspace())
print("是否只包含空白字符: %s" % emptyStr.isspace())
print("是否只包含空白字符: %s" % emptyStr2.isspace())

introduc = "This Is My Hometowm!"
print("是否每个单词的开头大写,其他的小写:%s" % introduc.istitle())

welcom = "WELCOM TO CHINA"
print("是否都是大写的:%s" % introduc.isupper())
print("是否都是大写的:%s" % welcom.isupper())

fruit = "Banana hao chi"
city = "shenzhen nihao,xiao ming"
print("是否都是小写的:%s" % fruit.islower())
print("是否都是小写的:%s" % city.islower())

print("字符串的长度:%d" % len(city))

country = "England"
print(country.ljust(12, "*"))  # 左边对齐,*号填充
print(country.rjust(12, "+"))  # 右边对齐,+号填充

welcom = "WELCOM TO BEIJIN AND shenzhen"
print("转换大写为小写：%s" % welcom.lower())

welcom = "  ni hao,huan yin xue xi Python       "
print("转换小写为大写：%s" % welcom.upper())

print("去除空格:%s" % welcom.strip())

welcom = "      WELCOM TO BEIJIN AND shenzhen,你好乖乖   "
print("去除左边空格:%s" % welcom.lstrip())
print("去除右边空格:%s" % welcom.rstrip())

company_str = "baidu,tencent,google,xiaomi,meituan,taobao"
print("替换前:%s" % company_str)
print("替换后:%s" % company_str.replace(",", " "))

hobby = "唱歌,跳舞,乒乓球,篮球,羽毛球"
hobby_list = hobby.split(",")
print(hobby_list)  # 拆分字符串为列表

sentences = "春天来了\n小草绿了\r花儿开了\r鸟儿欢乐了"
print(sentences.splitlines())

companys = "BAIDUI,tencent,Google,xiaomi,MEITUAN,taobao"
print("原字符串:%s" % companys)
print("大写转换为小写，小写转换为大写:%s" % companys.swapcase())
