import os
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
        current_dir = root_dir + ioshd + '/src_origin/'
        sourceSrcDir = current_dir  + "../assets/src/"
        dstSrcDir =root_dir +'Resources/src/'

        key ='0181A5\(bdE'
        b = '76c[F25%03'
        # s = 'cocos luacompile -s ' + current_dir + " -d" + sourceSrcDir + "/ -e -k %s -b %s --disable-compile" % (key, b)
        # os.system(s)

        # isExists = os.path.exists(dstSrcDir)
        # if not isExists:
        #     # os.mkdir(dstSrcDir)
        #     print(current_dir + ' success')
        # else:
        #     print(current_dir + ' isexist')

        if os.path.exists(dstSrcDir):
            alllist = os.listdir(sourceSrcDir)
            for i in alllist:
                print(i)
                if i != '.DS_Store':
                    print('laile0')
                    if os.path.exists(dstSrcDir + i):
                        if os.path.isdir(dstSrcDir + i):
                            shutil.rmtree(dstSrcDir+i)
                        # elif os.path.isdir(dstSrcDir + i):
                        #     shutil.rmtree(dstSrcDir+i)
                    if os.path.isfile(sourceSrcDir+i):
                        shutil.copyfile(sourceSrcDir+i, dstSrcDir+i)
                    elif os.path.isdir(sourceSrcDir+i):
                        shutil.copytree(sourceSrcDir + i, dstSrcDir + i)

        print("============end compile src ===================")


if __name__ == '__main__':
    compile_index.encode_src()
