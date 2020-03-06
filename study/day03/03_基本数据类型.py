'''
Python3 基本数据类型
'''
# 一.基本数据类型
count = 100
miles = 34.7
name = "google"
print(str(count) + "," + str(miles) + "," + name)
print("%d,%f,%s" % (count, miles, name))

# 多个变量赋值
a = b = c = 3
print("a:%d,b:%d,c:%d" % (a, b, c))
d, e, f = 3.14, 7, "python"
print("d:%f,e:%d,f:%s" % (d, e, f))

'''
二.标准数据类型
    Python3 中有六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）
    
    Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
# 1.Number（数字）
print("*" * 30)
age = 18
price = 5.4
isDel = False
distance = 3 + 4j
length = 2.0e+1  # 2*10的1次方
weight = 2.0E-1  # 2*10的-1次方
print("type(age): %s" % type(age))
print("type(price): %s" % type(price))
print("type(isDel): %s" % type(isDel))
print("type(distance): %s" % type(distance))
print(length)
print(weight)

# 删除对象
book = "英语"
print("book: %s" % book)
del book
# 抛出异常,NameError: name 'book' is not defined
# print("del after book is %s" % book)


# 2.数值运算
print("**************数值运算******************")
print("3+4=%d" % (3 + 4))
print("23-12=%d" % (23 - 12))
print("3*4=%d" % (3 * 4))
print("13/4=%f" % (12 / 4))
print("13//4=%d" % (12 // 4))
print("12取余5=%d" % (12 % 5))
print("2**3=%d" % (2 ** 3))

# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
a = 13 / 4
b = 13 // 4
print(a)
print(b)
