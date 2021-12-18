from sys import exit
import random


def room1():
    print("欢迎来到1号房，你可以选择宝箱了：")

    choice = input("请选择序号：1，2，或者3：")
    if choice == "1":
        print("恭喜你获得一条眼镜蛇！")
        die("你被眼镜蛇咬死了！")
    elif choice == "2":
        print("恭喜你获得一只老鼠！请继续游戏！")
        start()
    elif choice == "3":
        print("恭喜你收获一束鲜花！请继续游戏！")
        start()
    else:
        print("选错了，你完了！")
        die("你没有按规定选择宝箱！")


def room2():
    print("欢迎来到2号房，这里有三瓶水，你要选一瓶喝了。")

    choice = input("请选择颜色：red，blue，或者yellow：")
    if choice == "red":
        print("恭喜你获得了能量水！继续游戏！")
        start()
    elif choice == "blue":
        print("不好意思！这是毒药！")
        die("你中毒了，没救了！")
    elif choice == "yellow":
        print("恭喜你收获一瓶唐僧液！请继续游戏！")
        start()
    else:
        print("完了，你完了！")
        die("你没有按规定喝水！")


# 创建房间1 房间2列表，用于随机调用，游戏中的随机穿越
room = [room1, room2]


def room3():
    print("欢迎来到3号房，这里有四个道具，你必须选择一个进行游戏。")

    while True:
        choice = input("请选择序号：a，b，c或者d：")
        if choice == "a" or choice == "c":
            print("恭喜你获得月光宝盒！你将直接随机穿越到别的房间。")
            # 随机调用函数房间1和房间2
            random.choice(room)()
        elif choice == "b":
            print("恭喜你获得重生机会！游戏重新开始！")
            start()
        elif choice == "d":
            print("恭喜你收获一把宝剑！这居然是国家文物，你被逮捕了！")
            die("你因非法占有国家文物，被判死刑！")
        else:
            print("选错了吗，那你完了！")
            die("你没有按规定选择道具！")


def die(why):
    print(why, "游戏结束！")
    exit(0)


def start():
    print("欢迎来到大厅，现在你的面前有三个门，分别是1，2，3，请选择一个门进行游戏.")

    choice = input("请直接输入门号：")

    if choice == "1":
        room1()
    elif choice == "2":
        room2()
    elif choice == "3":
        room3()
    else:
        die("你没有按照规定选择！你完了，死神叫你去打麻将！！！")


start()
