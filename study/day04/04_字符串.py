"""
一、Python3 字符串
    字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
    创建字符串很简单，只要为变量分配一个值即可。
"""
# 1.定义字符串
print("*************定义字符串******************")
str1 = "hello python"
str2 = '深圳市南山区'
str3 = "wecome to china," \
       "欢迎来到广州"
print(str1)
print(str2)
print(str3)

"""
1、Python 访问字符串中的值
    Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
    Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
"""
print(str1[7])
print(str2[0:])
print(str2[2:5])
print(str2[2:-2])
print(str2[:4])

"""
2、Python字符串运算符
    下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
    
    操作符	描述	                实例
    +	    字符串连接	            a + b 输出结果： HelloPython
    *	    重复输出字符串	        a*2 输出结果：HelloHello
    []	    通过索引获取字符串中字符	a[1] 输出结果 e
    [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
    in	    成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
    not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
    r/R	    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
    print( r'\n' )
    print( R'\n' )
    %	    格式字符串	            请看下一节内容。
"""

strA = "welcome to beijing! "
strB = r"hello google\n"
print(strA + strB)
print(strB * 2)
print(strA[3])
print(strB[1:4])

if ("come" in strA):
    print("come在strA中...")
else:
    pass

if ("shenzhen" not in strA):
    print("shenzhen不在strA中...")
else:
    pass

"""
3、Python字符串格式化
    python字符串格式化符号:
      符号	 描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
"""
name = "小明"
price = 3.14
number = 4
print("今天%s去超市买了%d个苹果,每斤%.2f元" % (name, number, price))
