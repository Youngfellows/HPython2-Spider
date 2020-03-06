# 1.读取文件
# 打开文件
file = open("./file/test1.txt", "r", encoding="utf-8")

# 读取文件内容
content = file.read()
print(content)

# 关闭文件
file.close()


