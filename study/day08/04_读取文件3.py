# 1.按行读取
# 打开一个文件
file = open("./file/test2.txt", "r", encoding="utf-8")

# 返回该文件中包含的所有行,是一个列表
content_list = file.readlines()
print("内容大小: size = %d" % len(content_list))
print(content_list)
for line in content_list:
    print(line,end=" ")

# 关闭打开的文件
file.close()
