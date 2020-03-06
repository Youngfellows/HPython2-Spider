# 1.在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
hero = {"name": "杨过", "age": 23, "sex": "男", "girl_friend": "小龙女"}
for key, value in hero.items():
    print("%s: %s" % (key, value))

# 2.在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
print("*********************")
citys = ["首尔", "东京", "墨尔本", "北京", "伦敦"]
for index, value in enumerate(citys):
    print("%d %s" % (index, value))

# 3.同时遍历两个或更多的序列，可以使用 zip() 组合
questrions = ["name", 'quest', "hobby"]
answers = ["郭靖", "你有女朋友么?", "打太极"]
for q, a in zip(questrions, answers):
    print("{0},{1}".format(q, a))

# 反向遍历列表
print("*" * 30)
fruits = ['apple', 'banana', 'orange', 'pear', "apple", "lemon"]
print(fruits)
for fruit in reversed(fruits):
    print(fruit, end=",")

print("\n********************")

# 列表排序
print(fruits)
fruits = set(fruits)
for fruit in sorted(fruits):
    print(fruit, end=",")
