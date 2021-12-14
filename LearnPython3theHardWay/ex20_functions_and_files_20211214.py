from sys import argv
# 解包，脚本和输入文件
script, input_file = argv
# 定义打印所有内容的函数


def print_all(f):
    print(f.read())


"""
重新打印所有内容，seek() 函数用于将文件指针移动至指定位置，格式fileObject.seek(offset[, whence]),
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

"""
def rewind(f):
    f.seek(0)

# 定义打印每一行的函数：关键词：行数，内容，readline（）逐行读取文件
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 打开当前文件
current_file = open(input_file)
# 加上/n可以让readline()停止扫描这个文件，并回到\n所在位置，以保证每次调用readling()维持文件当前位置，可以阅读到每一行
print("First let's print the whole file:\n")
# 打印所有文件内容
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# 重新打印所有内容
rewind(current_file)

print("Let's print three lines:")
# 打印三行内容
current_line = 1
print_a_line(current_line, current_file)
# current_line += 1
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

