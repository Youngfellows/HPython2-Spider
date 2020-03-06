# 1.基本数据类型
a = 1
b = 2000
c = -234
d = 0
e = 3.14
f = 0xff00
h = -9.8
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))

# 2.字符串类型
str1 = 'sheng zheng'
str2 = "china bei jing"
str3 = '''
你好,欢迎来深圳
这里是你的家
'''
print(type(str1))
print(str1)
print(str2)
print(str3)

# 字符串转义
str4 = '小明说\"我很好\"'
print(str4)

# 使用%操作符,和.format,使字符串格式化
name = "晓丽"
age = 18
size = 6
print("%s今天%d岁生日,哥哥给她买%d个蛋糕" % (name, age, size))
print("{0}今天{1}岁生日,哥哥给她买{2}个蛋糕".format(name, age, size))

# 3.布尔类型
isDel = True
isHot = False
print(type(isDel))
print(type(isHot))
print(isDel)
print(isHot)

# 4.空值
print(type(None))
print(type(0))
print(type(''))
print(None == 0)
print(None == '')
print(None == False)

# 5.格式化字符串
# %d,有符号的十进制整数（有符号意思为：就是前面可以加上正负号的意思，无符号也就是只能是正整数了）
# %03d表示显示3位数，不够3位的在前面用0补全
# %s,字符串
# %f,浮点数

# 使用%操作符,和.format,使字符串格式化
name = "晓丽"
age = 18
size = 6
print("%s今天%d岁生日,哥哥给她买%d个蛋糕" % (name, age, size))
print("{0}今天{1}岁生日,哥哥给她买{2}个蛋糕".format(name, age, size))

age = 20
print("Tom今年%d岁" % age)

name = "汤姆"
print("Tom的中文名字是%s" % name)

weight = 63.5
print("Tom的体重是%f千克" % weight)
print("Tom的体重是%.2f千克" % weight)

number = 1
print("Tom的学号是%03d" % number)

print("Tom的中文名是%s,体重是%.2f,年龄是%d,学号是%03d" % (name, weight, age, number))

# 也可以全部使用%s,都以字符串形式输出
print("Tom的中文名是%s,体重是%s,年龄是%s,学号是%s" % (name, weight, age, number))

print("是否存在:%s" % False)

# 也嵌套f'',%s,%d,%f
print(f"Tom的中文名是{name},体重是%.2f,年龄是%d,学号是%03d" % (weight, age, number))
print(f"是否大于0:{False}")

# 7.转义字符
print("欢迎来到\n广东深圳")
print("武汉\t加油!")

# 8.print结束符
# print结束符,用4个等号隔开
print("hello", end="=========")
print("world")

# 使用空字符结束
print("你好", end="")
print("北京")

# 使用\t隔开
print("广东", end="\t")
print("广州")
