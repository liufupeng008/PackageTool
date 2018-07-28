
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
excel_header_titles = []
version_dict = {'target_name':{'title':'版控标识',
                               },
                'package_name':{'title':'包名',
                               },
                'ios_hd':{'title':'差异文件夹名',
                               },
                'status':{'title':'状态',
                               },
                'channel_no':{'title':'渠道号'
                               },
                'channel':{'title':'渠道商'},
                    }
for i in range(0, row_num):

    row_data = sh.row_values(i)
    # 获取第i行的正行的数据
    if i == 0:
       channelNo_cl = row_data.index('渠道号')
       excel_header_titles.append(row_data)
    elif channelNo_cl is not None:
        _channelNof = sh.row_values(i, channelNo_cl, channelNo_cl+1)[0]
        _channelNo = "%.0f" % (_channelNof)
        if channelNo == _channelNo:
            # for col in range(1,sh.ncols):
            row_list.append(row_data)

print(excel_header_titles)
print(row_list)
