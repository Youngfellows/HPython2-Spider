# 1.指定utf-8格式写文件
# 写文件
file = open("./file/test.txt", "w", encoding="utf-8")

# 写文件
file.write("Python 很好玩,可以爬你喜欢的妹子图片...")

# 关闭文件流
file.close()

# 2.不需要关闭流
with open("./file/test1.txt", "w", encoding="utf-8") as  f:
    f.write("学习python还是有钱途的...")

# 3.不需要关闭流
import codecs

with codecs.open("./file/test3.txt", "w", encoding="utf-8") as f:
    f.write("学习python还是有钱途的...,你可以爬取你喜欢的妹子图片....")
