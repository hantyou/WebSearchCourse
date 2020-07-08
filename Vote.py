num = input("请输入总的投票人数：")
num = int(num)
import getpass

vote_result = []
for i in range(num):
    get = getpass.getpass("这是第" + str(i + 1) + "个人的投票，请输入你的投票结果，输入 1 则通过，输入 2 则不通过（输入无显示，请放心输入）：")
    get = int(get)
    if get == 1:
        vote_result.append(True)
    else:
        vote_result.append(False)

if False in vote_result:
    print("\n任务失败")
else:
    print("\n任务成功")

while (True):
    flag = input("是否需要看某个人的牌？ 1 是看，2是不看退出。")
    flag = int(flag)
    if flag == 1:
        which = input("想看谁的牌，输入数字 1 到 " + str(num) + " 。")
        which = int(which)
        if vote_result[which - 1] == True:
            print("他/她投的是成功票。")
        else:
            print("他/她投的是失败票。")
    else:
        break

input("回车退出")
quit()
