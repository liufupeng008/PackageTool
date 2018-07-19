import os,sys
from config import *
import shutil
class compile_index():

    @staticmethod
    def encode():
        print('请输入ios——hd index')
        idx = input("input:")
        compile_index.encode_src(idx)



    @staticmethod
    def encode_src():

        # --首先将ios_hdx里面的lua文件编译
        # --将编译后的差异文件、export一起合并到Resources中
        print("============begin %s compile src ==================="%(ioshd))

        root_dir = projectPath
        current_dir = root_dir + ioshd
        sourceSrcDir = root_dir  + "/ios_hd24"
        dstSrcDir =current_dir

        isExists = os.path.exists(current_dir)
        # 判断结果
        if not isExists:
            os.mkdir(current_dir)
            print(current_dir + ' success')
        else:
            print(current_dir + ' isexist')

        if os.path.exists(dstSrcDir):
            shutil.rmtree(dstSrcDir)

        shutil.copytree(sourceSrcDir, dstSrcDir)

        os.system("cocos luacompile -s " + sourceSrcDir + " -d" + dstSrcDir +'/assets/src'+"/ -e -k 0181A5bdE -b 76cF25%03 --disable-compile")
        print("============end compile src ===================")


if __name__ == '__main__':
    compile_index.encode_src()
