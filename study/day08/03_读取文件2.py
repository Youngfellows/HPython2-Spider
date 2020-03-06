# 1.按行读取
# 打开一个文件
file = open("./file/test2.txt", "r", encoding="utf-8")
while True:
    content = file.readline()
    print(content, end=" ")
    if content == "":
        break

# 关闭打开的文件
file.close()
