# -*- coding: UTF-8 -*-
from biplist import *

import sys
class whitePlist():
    import sys
    # sys.reload()
    sys.getdefaultencoding()  # 查看设置前系统默认编码

    # sys.setdefaultencoding('utf8')
    @staticmethod
    def start_modify_plist(targetName,path='/Users/yu/Desktop/whiteProject/'):
        try:
            channel = targetName[len(targetName)-4:len(targetName)]
            dict = {'4031':{'com.148owcv.sstl':'sstl_dis'},
                    '4030': {'com.135mok.bycq': 'bycq_dis'},
                    '4039': {'com.rxzr': 'rxzr_dis'},
                    '4040': {'com.sbkry': 'sbkry_dis'},
                    '4038': {'com.ms.hmydz': 'hmydz_dis_20180419'},
                    '4041': {'lieyde.chuanq.xianfen': 'Dis_lieyantulong'},
                    '4042': {'com.luyiwen': 'cycq_dis_20180420'},
                    '4044': {'com.oale258.dzz': 'badaoyurongyao2018_dis'},
                    '4046': {'com.zhuikangbang05y.cqby': 'bayu_dis'},
                    '4048': {'com.nd8N98k.ydhm': 'ydhm_dis_20180607'},
                    '4050': {'com.idang4896.sbkcq': 'sbkcq_dis_20180704'},
                    '4053': {'com.wanrengongsha.xf151dpa': 'wanrengongsha_dis_20180718'},
                    }
            4042

            provisioningProfiles = dict[channel]
            appstoreplist = {'compileBitcode': False,
                             'method': "app-store",  # app-store, ad-hoc, enterprise, development。
                             'provisioningProfiles': provisioningProfiles,
                             }
            writePlist(appstoreplist, "%s/ExportOptions.plist"%(path))
            print('plist write success',appstoreplist)
        except (InvalidPlistException, NotBinaryPlistException) as e:
            print("Something bad happened:", e)

if __name__ == '__main__':
   val = sys.argv[1]
   if val:
      whitePlist.start_modify_plist(val)