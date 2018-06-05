import os
import shutil
class Test():

      @staticmethod
      def start():

            dir_name = 'res/big'
            current_dir = 'image'
            login_image_name = 'backgroud_login.jpg'
            backgroud_loading_name = 'backgroud_loading.jpg'
            backgroudiphonex_login_name = 'backgroudiphonex_login.jpg'
            backgroundiphonex_loading_name = 'backgroudiphonex_loading.jpg'
            folder = 'res'
            isExists = os.path.exists(folder)


            if  isExists:
                  os.system('rm -rf ./%s'%(folder))

            os.mkdir(folder)
            os.mkdir(dir_name)

            shutil.copyfile('%s/%s'%(current_dir,login_image_name),'%s/%s'%(dir_name,login_image_name))
            shutil.copyfile('%s/%s'%(dir_name,login_image_name),'%s/%s'%(dir_name,backgroud_loading_name))

            shutil.copyfile('%s/%s'%(current_dir,backgroundiphonex_loading_name),'%s/%s'%(dir_name,backgroundiphonex_loading_name))
            shutil.copyfile('%s/%s'%(dir_name,backgroundiphonex_loading_name),'%s/%s'%(dir_name,backgroudiphonex_login_name))
      pass

if __name__ == '__main__':
    Test.start()