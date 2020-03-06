import os

"""
一、Python3 标准库
"""

# 操作系统接口
print("当前工作目录: {}".format(os.getcwd()))
# 修改当前的工作目录
# os.chdir("C:\\Users\\f2847881\\Desktop\\push")
# print("当前工作目录: {}".format(os.getcwd()))
# 执行系统命令 mkdir
# os.system("mkdir today")

import shutil

shutil.copyfile("./today/test2.txt", "./today/coyp_test.txt")

import calendar

print(calendar.mdays)
