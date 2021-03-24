
import xlwt

dst_file = '/Users/edz/Desktop/文章1/result/结果.xlsx'

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

# 写入内容,假设取出的内容是value
xlsheet.write(0, 0, value)

# 保存文件
workbook.save(dst_file)