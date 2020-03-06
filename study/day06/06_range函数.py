# range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for num in range(3, 10):
    print(num, end=" ")

print("\n****************")

# 步长2
for num in range(1, 20, 2):
    print(num, end=" ")

print("\n****************")
# 遍历列表
companys = ("Tencent", "Baidu", "Google", "MicroSoft")
for i in range(len(companys)):
    print("%d %s" % (i, companys[i]))
