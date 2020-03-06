# 1.基本数据类型
a = 7
b = 3.14
c = False
d = 1 + 2j
str = "hello python"
print(a)
print(b)
print(c)
print(d)

# 2.查看数据类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 3.多行语句
str = "中国广东" \
      "深圳南山" \
      "软件产业基地"
print(str)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
fruits = ["apple", "banana",
          "lemon", "orange"]  # 列表
companys = ("tencent", "baidu", "aili",
            "meituan", "xiaomi", "google", "apple")  # 元组
print(fruits)
print(companys)

# 4.字符串
name = "字符串"
sentence = "这是一个字符串"
paragraph = '''广东深圳
南山区
蛇口港口岸'''

# 输出字符串
print(name)
print(sentence)
print(paragraph)

# 输出第2个到倒数第二个的所有字符
print(sentence[1:-1])
# 输出字符串第一个字符
print(name[0])
# 输出1行字符串
print(name[0:])
# 输出从第三个开始到第五个的字符
print(sentence[2:5])
# 输出从第三个开始后的所有字符
print(sentence[2:])
# 输出字符串两次
print(name * 2)
# 连接字符串
print(name + "你好")
# 使用反斜杠(\)+n转义特殊字符
print("hello\npython")
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(r"hello\npython")

# 等待用户输入
user_input = input("请输入你想说的话:")
print("你输入的是:%s" % user_input)
