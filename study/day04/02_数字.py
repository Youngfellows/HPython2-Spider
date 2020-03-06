# Python3 数字(Number)
'''
1、Python 支持三种不同的数值类型：
    整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
    浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
'''
age = 28
radius = 23.57
dotA = 3 + 4j
dotB = complex(5, 7)

print("type(age): %s" % type(age))
print("type(radius): %s" % type(radius))
print("type(dotA): %s" % type(dotA))
print("type(dotB): %s" % type(dotB))
print(age)
print(radius)
print(dotA)
print(dotB)

# 我们可以使用十六进制和八进制来代表整数：
number = 0xA0FF  # 十六进制
count = 0o37  # 八进制
print(number)
print(count)

# 科学计数法
carPrice = 1.875e3
print(carPrice)

'''
2、Python 数字类型转换
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    int(x) 将x转换为一个整数。
    float(x) 将x转换到一个浮点数。
    complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
    complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''
print("\n*************数字类型转换********************")
distance = "3.14"
number = 4.78
size = 7
print(float(distance))
print(int(number))
print(str(size))

# 3、Python 数字运算
print("*****************Python 数字运算**************************")
a = 3
b = 4
c = 13

print(a + b)
print(c - a)
print(a * b)
print(c / a)
print(c // a)
print(c % a)

# Python 可以使用 ** 操作来进行幂运算
print("5 的平方: %d" % (5 ** 2))  # 5 的平方
print("2的7次方: %d" % (2 ** 7))  # 2的7次方

# 不同类型的数混合运算时会将整数转换为浮点数
print(7 / 4.8)
print(1.3 * 3 / 2.5)


