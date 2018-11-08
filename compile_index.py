import os
from config import *
import shutil
class compile_index():

    root_dir = projectPath
    current_dir = root_dir + ioshd + '/src_origin/'
    sourceDir = current_dir + "../assets/"
    dstSrcDir = root_dir + 'Resources/'
    exportDir = root_dir + 'export/'

    @staticmethod
    def encode_src():

        # --首先将ios_hdx里面的lua文件编译
        # --将编译后的差异文件、export一起合并到Resources中
        print("============begin %s %s compile src ==================="%(projectName,ioshd))
        key ='0181A5\(bdE'
        b = '76c[F25%03'
        if os.path.exists(compile_index.sourceDir + 'src'):
            shutil.rmtree(compile_index.sourceDir + 'src')
        cocos_cmd = 'cocos luacompile -s ' + compile_index.current_dir + " -d" + compile_index.sourceDir+'src/' + "/ -e -k %s -b %s --disable-compile" % (key, b)
        os.system(cocos_cmd)
        print("============ end compile src ===================")

    @staticmethod
    def copyfiletoResources():
        sourceDirList = os.listdir(compile_index.sourceDir)
        for source_dir in sourceDirList:
            if source_dir != '.DS_Store':
                if os.path.exists(compile_index.dstSrcDir+source_dir):
                            if os.path.exists(compile_index.dstSrcDir + source_dir):
                                if os.path.isdir(compile_index.dstSrcDir + source_dir):
                                    shutil.rmtree(compile_index.dstSrcDir + source_dir)
                            #export
                            if os.path.isfile(compile_index.exportDir + source_dir):
                                shutil.copyfile(compile_index.exportDir + source_dir, compile_index.dstSrcDir + source_dir)
                            elif os.path.isdir(compile_index.exportDir + source_dir):
                                shutil.copytree(compile_index.exportDir + source_dir, compile_index.dstSrcDir + source_dir)

                            if os.path.isfile(compile_index.sourceDir + source_dir):
                                shutil.copyfile(compile_index.sourceDir + source_dir, compile_index.dstSrcDir + source_dir)
                            # elif os.path.isdir(compile_index.sourceDir + source_dir):
                            #     shutil.copytree(compile_index.sourceDir +  source_dir, compile_index.dstSrcDir + source_dir)

    @staticmethod
    def copy_manifestToResources():
        fileName = 'project.manifest'
        manifest = compile_index.sourceDir + 'res/'+fileName
        dst  = projectPath + 'Resources/res/'
        if os.path.exists(compile_index.sourceDir + 'res/'):
           shutil.copyfile(manifest, dst+fileName)

    @staticmethod
    def copy_srcToResources():
        fileName = 'PlatformConfig.luac'
        file = compile_index.sourceDir + 'src/platform/' + fileName
        dst = projectPath + 'Resources/src/platform/'
        if os.path.exists(compile_index.sourceDir + 'src/platform/'):
            shutil.copyfile(file, dst + fileName)

        fileName_list = list(['Switch.luac','GameConfig.luac'])
        for fileName in fileName_list:
            file = compile_index.sourceDir + 'src/' + fileName
            dst = projectPath + 'Resources/src/'
            if os.path.exists(compile_index.sourceDir + 'src/'):
                shutil.copyfile(file, dst + fileName)



    @staticmethod
    def copyfileToResources():
        compile_index.copy_srcToResources()
        compile_index.copy_manifestToResources()

    @staticmethod
    def copy_ioshd_to_Resources():
        exec_sh_cmd = 'cd %s && ./sumExport.sh %s'%(projectPath,ioshd)
        print(exec_sh_cmd)
        os.system(exec_sh_cmd)





if __name__ == '__main__':
    compile_index.encode_src()
    # compile_index.copyfiletoResources()
