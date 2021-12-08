from sys import argv
# read the WYSS section for how to run this
# 本实例需要在终端运行，例如：python LearnPython3theHardWay/ex13_parameters_unpacking_variable_20211207.py one two three
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
