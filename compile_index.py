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

        fileName = 'Switch.luac'
        file = compile_index.sourceDir + 'src/' + fileName
        dst = projectPath + 'Resources/src/'
        if os.path.exists(compile_index.sourceDir + 'src/'):
            shutil.copyfile(file, dst + fileName)

    @staticmethod
    def copyioshdToResources():
        #source
        for dir in ['res','src']:
            assets = compile_index.sourceDir + dir
            resources = compile_index.dstSrcDir + dir
            if (os.path.exists(resources)):
                shutil.rmtree(resources, onerror=readonly_handler);
            shutil.copytree(assets,resources)
        #dst
        # compile_index.sourceDir
        # for root, dirs, files in os.walk(assets):
        #     files = list(filter(lambda x: x != '.DS_Store', files))
        #     dirs = list(filter(lambda x: x != '.DS_Store', dirs))
        #     print(root)
        #     print(files)
        #     for file in files:
        #
        #
        #     for dir in dirs:
        #         for file_name in files:
        #             dst = compile_index.dstSrcDir + dir + '/' + file_name
        #             file = root+'/' + file_name
        #             # shutil.copyfile(file, dst)
        #             pass



if __name__ == '__main__':
    compile_index.encode_src()
    # compile_index.copyfiletoResources()
