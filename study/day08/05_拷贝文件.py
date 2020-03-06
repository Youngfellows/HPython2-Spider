# 1.拷贝文件

# 打开文件
fr = open("./file/test2.txt", "r", encoding="utf-8")
fw = open("./file/copy_test2.txt", "w", encoding="utf-8")

# 读文件
read_list = fr.readlines()

# 拷贝文件
for line in read_list:
    fw.write(line)

# 关闭流
fr.close()
fw.close()

print("恭喜你,拷贝文件完成...")
