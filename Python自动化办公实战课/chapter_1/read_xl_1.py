import xlrd

file = r'C:\Users\Administrator\Desktop\test.xlsx'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=4, colx=4)