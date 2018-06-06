import os
import shutil
from PIL import Image
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

            print ('开始处理图片....')
            if  isExists:
                  os.system('rm -rf ./%s'%(folder))

            os.mkdir(folder)
            os.mkdir(dir_name)


            for root, dirs, files in os.walk(current_dir):
                  for img_name in files:
                        path = os.path.join(root, img_name)
                        img = Image.open(path)
                        # print (img.format) # PNG
                        width, height = img.size
                        if width == 1280 and height == 720:
                           shutil.copyfile('%s/%s' % (current_dir, img_name),'%s/%s' % (dir_name, login_image_name))
                           shutil.copyfile('%s/%s' % (current_dir, img_name),'%s/%s' % (dir_name, backgroud_loading_name))
                        elif width == 1558 and height == 720:
                            shutil.copyfile('%s/%s'%(current_dir,img_name),'%s/%s'%(dir_name,backgroundiphonex_loading_name))
                            shutil.copyfile('%s/%s'%(current_dir,img_name),'%s/%s'%(dir_name,backgroudiphonex_login_name))
            print ('图片处理完成....')

      pass

if __name__ == '__main__':
    Test.start()