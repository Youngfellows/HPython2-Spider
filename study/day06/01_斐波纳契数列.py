# 斐波纳契数列
a = 0
b = 1
i = 0
while i < 20:
    print(b, end="\t")
    a = b
    b = a + b
    i += 1
