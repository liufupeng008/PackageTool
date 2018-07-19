
# coding=utf-8
from config import *
import xlrd

# 文件的名字
file_name = projectPath + "版本.xlsx"
# 打开文件
bk = xlrd.open_workbook(file_name)
# 代开sheet1
sh = bk.sheet_by_name("版本")
# 获取行数
row_num = sh.nrows
row_list = []
for i in range(1, row_num):
    # 获取第i行的正行的数据
    row_data = sh.row_values(i)
    channelNof = sh.row_values(0, 8, 9)[0]
    channelNo = str(channelNof)
    if '5038' in channelNo:
        for col in range(1,sh.ncols):
            print(sh.row_values(i, 1, sh.ncols))
    row_list.append(row_data)

# 打印每一行的内容，打印出的为列表的形式
for row in row_list:
    channelNo = row[8]
    if  channelNo == 5038.0:
        print (row)