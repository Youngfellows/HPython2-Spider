import os
import re

# 1. 获取制定路径下 的所有文件名
allFileName = os.listdir("./png")  # 列表
print(allFileName)

# 2. 循环的方式 依次进行重命名
for fileName in allFileName:
    index = fileName.rfind(".png")
    name = fileName[0:index]
    file_suffix = fileName[index:]

    # print(fileName)
    # print("index = {}".format(index))
    # print("文件名:{},后缀:{}".format(name, file_suffix))
    new_name = re.sub(r"_\[.*\]_", "_[浪漫巴厘岛]_", name)
    # print(new_name)
    os.rename("./png/" + fileName, "./png/" + new_name + file_suffix)

print("批量修改文件名成功....")
