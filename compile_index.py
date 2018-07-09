import os,sys

class compile_index():

    @staticmethod
    def encode():
        print('请输入ios——hd index')
        idx = input("input:")
        compile_index.encode_src(idx)

    @staticmethod
    def encode_src(index):

        # --首先将ios_hdx里面的lua文件编译
        # --将编译后的差异文件、export一起合并到Resources中
        print("============begin compile src ===================", index)
        if index == 1:
            index = ""
            # 获取脚本路径
        path = sys.path[0]
        # current_dir=io.popen"cd":read'*l'
        root_dir = '/Users/yu/Desktop/'
        project_dir = 'sgameProject/lycq-client_version/CocosLuaGame'
        current_dir = root_dir
        os.system('cd '+current_dir)
        # current_dir = os.getcwd()
        os.system("mkdir -p " + "ios_hd" + index + "/assets/src")
#        os.system("rd /s/q " + "ios_hd" + index+ "assets\\src")
        # print(current_dir)
        os.system("cocos luacompile -s " + current_dir + "/ios_hd" + index+ "/src_origin -d" + current_dir + "/ios_hd" + index+ "/assets/src -e True -k 0181A5(bdE -b 76c[F25%03 --disable-compile")
        print("============end compile src ===================")


        print("============begin copy  ios_hd===" + index+"==src==and export src to Resources============")

        os.system("mkdir " + "Resources/src")
        os.system("rd /s/q " + "Resources\\src")
        os.system("xcopy export\\src Resources\\src/e/y/i")
        os.system("xcopy " + "ios_hd" + index+ "\\assets\\src/e/y " + "Resources\\src")

        print("============end copy src ===================")


        print("============begin copy res ===================" + index)
        os.system("md " + "Resources\\res")
        os.system("rd /s/q " + "Resources\\res")
        os.system("xcopy export\\res Resources\\res /e/y/i")
        os.system("xcopy " + "ios_hd" + index+ "\\assets\\res/e/y " + "Resources\\res")
        print("============end copy res ===================")








if __name__ == '__main__':
    compile_index.encode()
