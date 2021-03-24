for line in range(1,employee_number):
    content = table.row_values(rowx=line, start_colx=0, end_colx=None)
    # 将表头和员工数量重新组成一个新的文件
    new_content = []
    # 增加表头到要写入的内容中
    new_content.append(salary_header)
    # 增加员工工资到要写入的内容中
    new_content.append(content)
    # 调用自定义函数write_to_file()写入新的文件
    write_to_file(filename = content[1], cnt = new_content)