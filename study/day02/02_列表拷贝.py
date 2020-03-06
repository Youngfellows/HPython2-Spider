# 1.Python的中拷贝
# 用id()函数来查看对象的唯一识别号,发现a,b是一样的,原因是因为b只是a的引用，都是同一个地址，并没有实现真正的copy
a = [1, 2, 3]
b = a
b.append(4)
print(id(a))
print(id(b))
print(a)
print(b)
print("*" * 30)

# 2.浅拷贝
import copy

c = [4, 5, 6, 7]
d = copy.copy(c)
d.append(8)
print("id(c) = %s" % id(c))
print("id(d) = %s" % id(d))
print(c)
print(d)

# 当然若你已经知道了拷贝对象的类型，对于列表L,直接list(L)做浅拷贝,或者L[:],
# 对于字典d,调用dict(d),对于集合拷贝集合s,调用set(s)
f = [12, 34, 56, 78]
g = list(f)
print("id(f) = %s" % id(f))
print("id(g) = %s" % id(g))
g.append(90)
print(f)
print(g)

print("*" * 30)
i = {"apple": 33, "orange": 23.4, "banana": 35.8}
j = set(i)
print("id(i) = %s" % id(i))
print("id(j) = %s" % id(j))

# 2.多行语句
str = "中国广东省" \
      "深圳市南山区" \
      "软件产业基地"
print(str)
