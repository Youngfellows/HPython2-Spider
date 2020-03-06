"""
Python3 字典
    字典是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

    键必须是唯一的，但值则不必。
    值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""

# 1.定义字典
person = {"name": "杨过", "age": 18, "address": "蒙古"}
print(person)

# 2.访问字典元素
print("name: %s" % person["name"])
print("age: %s" % person["age"])
print("address: %s" % person["address"])
try:
    print("kongfu: %s" % person["kongfu"])
except KeyError:
    print("不存在键是kongfu的...")

# 3.修改字典元素
person["age"] = 24
person["address"] = "襄阳"
person["kongfu"] = "玄铁剑法"  # 添加一个新元素
print(person)

# 4.删除字典元素
student = {"name": "小龙女", "score": 99, "sex": "女", "hobby": "练武功"}
print(student)
# 删除键 'hobby'
del student["hobby"]
print(student)
# 清空字典
student.clear()
print(student)
# 删除字典
# del student
# print(student)

"""
二、字典键的特性
    字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
    
    两个重要的点需要记住：
    1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""
car = {"name": "奔驰", "color": "red", "price": 44000, "owner": {"owner_name": "郭靖", "age": 33}, "door": ["前门", "后门"]}
print(car)

"""
三、字典内置函数&方法  
"""
print("***************字典内置函数&方法*******************")
# 1.字典大小
print("car字典大小:size = %d" % len(car))

# 2.转换为json字符串
json_str = str(car)
print(type(car))
print(type(str(json_str)))
print(json_str)

# 3.清空字典
print("清空字典前大小: size = %d" % len(car))
# car.clear()
print("清空字典后大小: size = %d" % len(car))

# 4.字典的浅复制
new_car = car.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
print(new_car)
print("car     id is: %s" % id(car))
print("new_car id is: %s" % id(new_car))
# 修改字典元素
new_car["name"] = "玛莎拉蒂"
new_car["color"] = "白色"
print("car    字典: %s" % car)
print("new_car字典: %s" % new_car)

# 浅拷贝: 引用对象
my_car = car
print("car    id is: %s" % id(car))
print("my_car id is: %s" % id(my_car))
my_car["name"] = "奥迪"
my_car["color"] = "blank"
print("car   字典: %s" % car)
print("my_car字典: %s" % my_car)

# 5.字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
person_key = ("name", "age", "sex")
person = dict.fromkeys(person_key)
print(person)
person_value = ("赵敏", 24, "女")
person2 = dict.fromkeys(person_key, person_value)
print(person2)

# 6.获取字典元素
car = {"name": "奔驰", "color": "red", "price": 44000, "owner": {"owner_name": "郭靖", "age": 33}, "door": ["前门", "后门"]}
print("car name is: %s" % car["name"])
print("car color is: %s" % car.get("color"))
print("car speed is: %s" % car.get("speed", "NA"))  # 元素不存在,返回默认

# 7.键是否在字典中
if "speed" in car:
    print("键speed在字典中存在...")
else:
    print("键speed在字典中不存在...")

if "price" in car:
    print("键price在字典中存在...")
else:
    print("键price在字典中不存在...")

if "owner" not in car:
    print("键owner在字典中不存在...")
else:
    print("键owner在字典中存在...")

# 8.以列表返回可遍历的(键, 值) 元组数组
print("**********遍历字典1*************")
print(type(car.items()))
print(car.items())
for ele in car.items():
    print(ele)

print("**********遍历字典2*************")
car_info = []  # 将字典的 key 和 value 组成一个新的列表
for key, value in car.items():
    print("%s:%s" % (key, value))
    car_info.append(key)
    car_info.append(value)

print(car_info)

# 9.keys()返回一个可迭代对象，可以使用 list() 来转换为列表
print(type(car.keys()))
print(car.keys())

key_list = list(car.keys())  # 转换为列表
print("键的列表: ", key_list)

# 9.values()返回一个可迭代对象，可以使用 list() 来转换为列表
print(car.values())
print(type(car.values()))

value_list = list(car.values())
print("值的列表: ", value_list)

# 10.字典 setdefault() 方法和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
car.setdefault("size", "3米")
print(car.setdefault("color", "blue"))
print(car)

# 11.字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里
computer = {"name": "Lenovo", "os": "windows 10", "price": 4800}
owner = {"onwer_name": "韦小宝", "age": 18, "sex": "男"}
computer.update(owner)
print(computer)

# 12.字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
price = computer.pop("price")
pc_color = computer.pop("color", "黑色")
print("price: %s" % price)
print("pc_color: %s" % pc_color)
print(computer)

# 13.字典 popitem() 方法随机返回并删除字典中的最后一对键和值。
computer.popitem()
print(computer)
