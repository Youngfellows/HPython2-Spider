"""
猜拳游戏使用ifelse代码实现
0为石头，1位剪刀，2为布
"""
import random

while True:
    wanjia = int(input("请玩家出拳，0为石头,1为剪刀,2为布:"))
    diannao = random.randint(0, 2)
    print("diannao: %d" % diannao)

    # 玩家获胜判断
    if (wanjia == 0 and diannao == 1) or (wanjia == 1 and diannao == 2) or (wanjia == 2 and diannao == 0):
        print("玩家获胜")
    elif wanjia == diannao:
        print("平局,再来一局...")  # 平局判断
    else:
        print("电脑获胜")
