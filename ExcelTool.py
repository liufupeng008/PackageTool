
# coding=utf-8
import xlrd

# 文件的名字
file_name = "not_get_app.xlsx"
# 打开文件
bk = xlrd.open_workbook(file_name)
# 代开sheet1
sh = bk.sheet_by_name("Sheet1")
# 获取行数
row_num = sh.nrows
row_list = []
for i in range(1, row_num):
    # 获取第i行的正行的数据
    row_data = sh.row_values(i)
    row_list.append(row_data)

# 打印每一行的内容，打印出的为列表的形式
for row in row_list:
    print (row)