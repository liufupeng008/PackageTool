import os
import shutil
from PIL import Image
from config import *
class Test():

      #处理logo图 login图 loading图
      @staticmethod
      def start_main_image():
            def modify_images(dir,var):
                  for root, dirs, files in os.walk(dir):
                        for img_name in files:
                              path = os.path.join(root, img_name)
                              img = Image.open(path)
                              # print (img.format) # PNG
                              width, height = img.size
                              if width == 1280 and height == 720:
                                    if var == 0 :
                                          shutil.copyfile('%s/%s' % (dir, img_name),'%s/%s' % (dir_name, backgroud_loading_name))
                                    else:
                                          shutil.copyfile('%s/%s' % (dir, img_name), '%s/%s' % (dir_name, login_image_name))

                              elif width == 1558 and height == 720:
                                    if var == 0:
                                          shutil.copyfile('%s/%s'%(dir,img_name),'%s/%s'%(dir_name,backgroundiphonex_loading_name))
                                    else:
                                          shutil.copyfile('%s/%s'%(dir,img_name),'%s/%s'%(dir_name,backgroudiphonex_login_name))


            project_root_path = projectPath
            # dir_name = project_root_path + 'ios_hd'+'10' '/assets/res/big'
            dir_name = project_root_path +'Resources/res/big'
            login_dir = 'login'
            loading_dir = 'loading'
            logo_dir = 'logo'


            login_image_name = 'backgroud_login.jpg'
            backgroud_loading_name = 'backgroud_loading.jpg'
            backgroudiphonex_login_name = 'backgroudiphonex_login.jpg'
            backgroundiphonex_loading_name = 'backgroudiphonex_loading.jpg'
            folder = 'res'
            isExists = os.path.exists(folder)
            logo_lylc_name = 'logo_lylc.png'
            print ('开始处理图片....')
            if  isExists:
                  # os.system('rm -rf ./%s'%(folder))
                  os.system('rm -rf ./%s/.DS_Store'%(dir_name))
                  os.system('rm -rf ./%s/.DS_Store' % (login_dir))
                  os.system('rm -rf ./%s/.DS_Store' % (loading_dir))


            modify_images(loading_dir,0)
            modify_images(login_dir,1)
            for root, dirs, files in os.walk(logo_dir):
                  for img_name in files:
                        path = os.path.join(root, img_name)
                        img = Image.open(path)
                        width, height = img.size
                        if width!=780 and height != 401:
                              out = img.resize((780, 401))
                              out.save(path, 'png')
                        shutil.copyfile('%s/%s' % (logo_dir, img_name), '%s/%s' % (dir_name, logo_lylc_name))

            print('图片处理完成....')

      pass

      @staticmethod
      def modify_images(dir_name,yfy_dir,isIcon=True):
            arr = [20,29,40,60,58,76,80,87,120,180,152,167,1024]
            for root, dirs, files in os.walk(yfy_dir):
                  for img_name in files:
                              path = os.path.join(root, img_name)
                              img = Image.open(path)
                              # print (img.format) # PNG
                              width, height = img.size
                              if isIcon:
                                if width in arr:
                                  if width == 120 or  width == 40 or width == 58 or width == 80:
                                      shutil.copyfile('%s/%s' % (yfy_dir, img_name),
                                                      '%s/%dx%d-1.png' % (dir_name, width, height))
                                      if width == 40:
                                          shutil.copyfile('%s/%s' % (yfy_dir, img_name),
                                                          '%s/%dx%d-2.png' % (dir_name, width, height))

                                  shutil.copyfile('%s/%s' % (yfy_dir, img_name),'%s/%dx%d.png' % (dir_name, width,height))
                              else:
                                      shutil.copyfile('%s/%s' % (yfy_dir, img_name),
                                                      '%s/%dx%d.png' % (dir_name, width, height))

      @staticmethod
      def start_icon_image(yfy_path):

          asset = 'Assets.xcassets/'
          asset = 'DTQCQHZB/Images.xcassets/'
          appicon_dirname = 'AppIcon_%s.appiconset'%(targetName)
          path = xcodeprojPath + asset + appicon_dirname
          isExists = os.path.exists(path)
          # 判断结果
          if not isExists:
              os.mkdir(path)
              print(path + ' 创建成功')
          else:
              print(path + ' 目录已存在')
          # 把contents.json copy 到项目中对应的目录中
          for root, dirs, files in os.walk('icon_json'):
              for json_name in files:
                  shutil.copyfile('%s/%s' % (root, json_name), '%s/%s' % (path, json_name))

          Test.modify_images(path, yfy_path)
          pass


      @staticmethod
      def start_launchimage(yfy_path,isIcon = False):
          asset = 'Assets.xcassets/'
          asset = 'DTQCQHZB/Images.xcassets/'

          appicon_dirname = 'LaunchImage_%s.launchimage'%(targetName)
          path = xcodeprojPath + asset + appicon_dirname
          isExists = os.path.exists(path)
          # 判断结果
          if not isExists:
             os.mkdir(path)
             print(path + ' 创建成功')
          else:
             print(path + ' 目录已存在')
          #把contents.json copy 到项目中对应的目录中
          for root, dirs, files in os.walk('launchimage_json'):
                for json_name in files:
                    shutil.copyfile('%s/%s' % (root, json_name), '%s/%s' % (path, json_name))

          Test.modify_images(path,yfy_path,isIcon)
          pass


if __name__ == '__main__':

    basePath = '/Users/yu/Documents/FangCloudSync/协作_出包排期/2.仙峰/3.正版传奇/20180718-新包-4052(开天霸业)/'
    yfy_launchimage_path = basePath + '闪屏-20180505_02(已用)'
    yfy_icon_path =basePath +'20171213-icon-1024'
    isExists = os.path.exists(yfy_launchimage_path)
    Test.start_main_image()
    Test.start_launchimage(yfy_launchimage_path)
    Test.start_icon_image(yfy_icon_path)