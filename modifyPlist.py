# -*- coding: UTF-8 -*-
from biplist import *
from config import *

import sys
class modifyPlist():
    import sys
    # sys.reload()
    sys.getdefaultencoding()  # 查看设置前系统默认编码

    # sys.setdefaultencoding('utf8')
    def start_modify_plist(self,path):
        try:
            plist = {}
            if package_method == 1:
                plist = appstoreplist
            elif package_method == 2:
                plist = xfplist
            elif package_method == 4:
                plist = devplist

            writePlist(plist, "%s/ExportOptions.plist"%(path))
            print('plist 写入成功',plist)
        except (InvalidPlistException, NotBinaryPlistException) as e:
            print("Something bad happened:", e)

    def read_modify_plist(self,path):
        try:
            plist = readPlist("%s/ios/info.plist"%(path))
            print(plist)

        except InvalidPlistException as e:
            print  ("Not a Plist or Plist Invalid:", e)



if __name__ == '__main__':
    import sys
    # print(sys.argv[1])
    val = sys.argv[1]
    # val = xcodeprojPath
    if val:
       modifyPlist().start_modify_plist(val)
       # modifyPlist().read_modify_plist(val)