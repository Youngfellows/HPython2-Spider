# 1.python运算符
print("1+2=%d" % (1 + 2))
print("1-2=%d" % (1 - 2))
print("1*2=%d" % (1 * 2))
print("6/2=%d" % (6 / 2))
print("9//2=%d" % (9 // 2))  # 整除
print("9除以2=%d" % (9 % 2))  # 整除
print("2的4次方=%d" % (2 ** 4))  # 2*2*2*2=16
print((1 + 2) * 3)

# 2.python定义变量
age = 12
height, weight, name = 170, 130, "小明"
print("名字:%s,年龄:%d,身高:%d,体重:%d" % (name, age, height, weight))
a = b = c = d = 2
print("a=%d,b=%d,c=%d,d=%d" % (a, b, c, d))

# 3.复合运算符举例
a = 3
b = 4
a += b
print("a = %d" % a)  # a = a+b
a -= b
print("a = %d" % a)  # a = a-b
a *= b
print("a = %d" % a)  # a=a*b
a /= b
print("a = %d" % a)  # a = a/b
a **= b
print("a = %d" % a)  # a = a**b

c = 15
d = 4
c %= d
print("c = %d" % c)

# 4.比较运算符
a = 3
b = 4
print("3==4: %s" % (a == b))
print("3!=4: %s" % (a != b))
print("3>4: %s" % (a > b))
print("3>=4: %s" % (a >= b))
print("3<4: %s" % (a < b))
print("3<=4: %s" % (a <= b))

# 5.逻辑运算符
age = 18
size = 5
if age > 10 and size < 8:
    print("age,%d大于10,且size,%d小于8" % (age, size))
else:
    pass

if age > 10 or size < 4:
    print("age,%d大于10,或者size,%d小于4" % (age, size))
else:
    pass

result1 = a < 0
if not result1:
    print("age,%d不小于0" % age)
else:
    pass

# 6.数字之间的逻辑运算
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0的数字
a = 0  # 0000 0000
b = 1  # 0000 0001
c = 2  # 0000 0010
d = 3  # 0000 0011
print(a and b)  # 0
print(b and c)  # 2
print(c and d)  # 3
print(b and d)  # 3

# or运算符，只要所有的值为0结果才为0，否则结果为第一个非0数字
print("*" * 30)
print(a or b)
print(a or c)
print(a or d)
print(b or c)
print(b or d)
print(d or c)
print(c or d)
print(d or a)
