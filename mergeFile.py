import os,sys
from config import *
import shutil
class mergeFile():


    @staticmethod
    def start_merge_files():

        # --首先将ios_hdx里面的lua文件编译
        # --将编译后的差异文件、export一起合并到Resources中
        print("============begin %s compile src ==================="%(ioshd))
        export = 'export/'
        sourceSrcDir = projectPath + export

        ios_hd_path = projectPath + ioshd
        dstSrcDir = projectPath + 'Resources'


        if os.path.exists(dstSrcDir):
              for root, dirs, files in os.walk(dstSrcDir):
                  for dir in dirs:
                      shutil.rmtree(root+'/'+dir)
                      print('删除' + ' success')
        isExists = os.path.exists(current_dir)
        # 判断结果
        if not isExists:
            os.mkdir(current_dir)
            print(current_dir + ' success')
        else:
            print(current_dir + ' isexist')

        if os.path.exists(sourceSrcDir):
            # for root, dirs, files in os.walk(sourceSrcDir):
                # for dir in dirs:
                 shutil.copytree(sourceSrcDir, dstSrcDir)





if __name__ == '__main__':
    mergeFile.start_merge_files()
