"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
"""

citys = ("北京", "深圳", "南京", "天津", False, 123, 3.14)
citys2 = ("广东", "湖北", "贵州", "新疆", False, 123, 3.14, ["apple", "google"])
fruits = ("apple",)  # 一个元素，需要在元素后添加逗号
empteTulp = ()  # 空元组

# 输出完整元组
print(citys)
print(citys2)
print(fruits)
print("size = %d" % len(fruits))
print("size = %d" % len(empteTulp))

# 输出元组的第一个元素
print(citys[0])
print(citys2[6])

# 输出从第2个元素开始到第4个元素
print(citys[1:4])
print(citys2[1:6])

# 输出从第三个元素开始的所有元素
print(citys[2:])
# 输出从第4个元素开始的到倒数第3元素
print(citys2[3:-2])

# 输出两次元组
print(citys * 2)

# 连接元组
new_citys = citys + citys2
print(new_citys)

# 修改元组元素的操作是非法的
# citys[1] = "贵阳"
