# 定义函数奶酪和饼干（参数：奶酪数量，饼干盒数）
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印奶酪数量
    print(f"You have {cheese_count} cheeses!")
    # 打印饼干盒数
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 直接给出参数，奶酪数量20， 饼干盒数30
print("We can just give the function numbers directly:")
# 调用函数
cheese_and_crackers(20, 30)

# 自行给变量赋值
print("OR, we can use variables from our script:")
# 与函数中的变量名不同
amount_of_cheese = 10
amount_of_crackers = 50
# 调用函数，使用刚刚赋过值的变量名称：amount_of_cheese, amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 在调用函数过程中进行算术运算
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 在调用函数中进行变量和数字运算
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
