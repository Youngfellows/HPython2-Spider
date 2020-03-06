# 一、Python算术运算符
'''
+	加 - 两个对象相加				                a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数		        a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	    a * b 输出结果 210
/	除 - x 除以 y				                    b / a 输出结果 2.1
%	取模 - 返回除法的余数			                    b % a 输出结果 1
**	幂 - 返回x的y次幂				                a**b 为10的21次方
//	取整除 - 向下取接近除数的整数
'''
a = 13
b = 3
c = 0

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(b ** 2)
# print(a / c)


# 二、Python比较运算符
print("\n**************Python比较运算符***********************")
'''
==	等于 - 比较对象是否相等	                (a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	        (a != b) 返回 True。
>	大于 - 返回x是否大于y	                (a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	        (a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	        (a <= b) 返回 True。
'''
if (a == b):
    print("a等于b")
else:
    print("a不等于b")

if (a != b):
    print("a不等于b")
else:
    print("a等于b")

if (a != b):
    print("a不等于b")
else:
    print("a等于b")

if (a > b):
    print("a大于b")
else:
    print("a不大于b")

if (a >= b):
    print("a大于等于b")
else:
    print("a小于b")

if (a < b):
    print("a小于b")
else:
    print("a不小于b")

if (a <= b):
    print("a小于等于b")
else:
    print("a大于b")

# 三、Python赋值运算符
'''
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c *= a 等效于 c = c * a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	    c **= a 等效于 c = c ** a
'''
print("\n****************Python赋值运算符********************")
a = 1
b = 2
c = 3
d = 8
e = 33

c = a + b
print(c)
a += b
print("a = %d" % a)
a -= b
print("a = %d" % a)
a *= c
print("a = %d" % a)
c /= b
print("c = %f" % c)
e // b
print("e == %f" % e)
d %= 3
print("d = %d" % d)
a **= 2
print("a = %d" % a)

# 四、 Python位运算符
'''
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13二进制格式如下：
a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011
'''
'''
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0			        (a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。				                    (a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1						                        (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1			        (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数		    a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''

print("\n**************Python位运算符******************")
a = 60
b = 13
c = 0

# 转化为二进制数
print("a为60的二进制数: %s" % bin(a).replace("0b", "").rjust(8, "0"))
print("b为13的二进制数: %s" % bin(b).replace("0b", "").rjust(8, "0"))
print("c为0 的二进制数: %s" % bin(c).replace("0b", "").rjust(8, "0"))

d = a & b
print("a&b = %d,二进制: %s" % (d, bin(d).replace("0b", "").rjust(8, "0")))
e = a | b
print("a|b = %d,二进制: %s" % (e, bin(e).replace("0b", "").rjust(8, "0")))
f = a ^ b
print("a^b = %d,二进制: %s" % (f, bin(f).replace("0b", "").rjust(8, "0")))
g = ~a
print("~a = %d" % g)
h = a << 2
print("a << 2 = %d,二进制: %s" % (h, bin(h).replace("0b", "").rjust(8, "0")))
i = a >> 2
print("a >> 2 = %d,二进制: %s" % (i, bin(i).replace("0b", "").rjust(8, "0")))

# 五、Python逻辑运算符
print("********************Python逻辑运算符************************")
'''
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
运算符	逻辑表达式	描述	                                                             实例
and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	 (a and b) 返回 20。
or	    x or y	    布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	     (a or b) 返回 10。
not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	 not(a and b) 返回 False
'''
a = 10
b = 20

c = a and b
print("c = %d" % c)
if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

d = a or b
print("d = %d" % d)
if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

e = not (a and b)
print("e = %s" % e)
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

# 六、Python成员运算符
'''
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。

运算符	描述									                实例
in	    如果在指定的序列中找到值返回 True，否则返回 False。			x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。		x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
'''
print("********************Python成员运算符*************************")
address = "香港"
hometown = "南宁"
citys = ["澳门", "北京", "香港", "深圳", "南山", "厦门"]

if address in citys:
    print(f"{address}在列表: %s" % citys)
else:
    print(f"{address}不在列表: %s" % citys)

if hometown not in citys:
    print(f"{hometown}不在列表: %s" % citys)
else:
    print(f"{hometown}在列表: %s" % citys)

# 七、Python身份运算符
'''
运算符	描述								        实例
is	is 是判断两个标识符是不是引用自一个对象				x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象		x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。

注： id() 函数用于获取对象内存地址。
'''
a = 20
b = 20

print("******************Python身份运算符*************************")
if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有有相同的标识")

b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有有相同的标识")

if (id(a) == id(b)):
    print("4 - a 和 b 有相同的标识")
else:
    print("4 - a 和 b 没有有相同的标识")

if (a is not b):
    print("5 - a 和 b 没有有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
province = ("北京", "香港", "广州", "苏州")
new_province = province
print(id(province))
print(id(new_province))


