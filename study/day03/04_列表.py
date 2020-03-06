'''
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：
变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 + 是列表连接运算符，星号 * 是重复操作
'''

citys = ["北京", "深圳", 123, True, "google", 3.14]
fruits = ["apple", "banana", "orange", 32.35, False, ["中国", "日本"]]

# 输出完整列表
print(citys)
print(fruits)
# 输出列表第3个元素
print(citys[2])
print(fruits[5])
# 从第2个开始输出到第4个元素
print(citys[1:4])
# 输出从第三个元素开始的所有元素
print(fruits[2:])
print(citys * 2)

# 列表连接
new_list = citys + fruits
print(new_list)

# 1.修改列表元素
names = ["小明", "老王", "老五", "老李", "老白"]
print(names)
names[1] = "老吴"  # 修改第2个元素
print(names)
names.append("老张")  # 添加元素
print(names)

# 将对应的元素值设置为 []
names[2:5] = []
print(names)


# 2.字符串反转
def reverseWords(input):
    inputwords = input.split(" ")
    print(inputwords)

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputwords = inputwords[-1::-1]

    # 重新组合字符串
    output = " ".join(inputwords)
    return output


if __name__ == "__main__":
    input = "I live python"
    result = reverseWords(input)
    print("origin: %s" % input)
    print("result: %s" % result)
