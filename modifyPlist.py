# -*- coding: UTF-8 -*-
from biplist import *
from config import *
class modifyPlist():

    def start_modify_plist(self,path):
        try:
            plist = {}
            if isxfad_hoc == True:
                plist = xfplist
            else:
                plist = otherplist

            writePlist(plist, "%s/ExportOptions.plist"%(path))
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
    print(sys.argv[1])
    val = sys.argv[1]
    if val:
       # modifyPlist().start_modify_plist(val)
       modifyPlist().read_modify_plist(val)