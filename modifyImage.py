import os
import shutil
from PIL import Image
from config import *
class modifyImage_cls():

      @staticmethod
      def start_main_image(path=''):
            project_root_path = projectPath
            dir_name_ioshd = project_root_path + ioshd + '/assets/res/big'
            dir_name = project_root_path +'Resources/res/big'

            def modify_images(dir,var,dstdir=''):
                  for root, dirs, files in os.walk(dir):
                        for img_name in files:
                            if img_name != '.DS_Store':
                              path = os.path.join(root, img_name)
                              img = Image.open(path)
                              if dstdir == '':
                                _dstdir = dir_name
                              else:
                                _dstdir = dstdir

                              # print (img.format) # PNG
                              width, height = img.size
                              if width == 1280 and height == 720:
                                    if var == 0 :
                                          shutil.copyfile('%s/%s' % (dir, img_name),'%s/%s' % (_dstdir, backgroud_loading_name))
                                    else:
                                          shutil.copyfile('%s/%s' % (dir, img_name), '%s/%s' % (_dstdir, login_image_name))

                              elif width == 1558 and height == 720:
                                    if var == 0:
                                          shutil.copyfile('%s/%s'%(dir,img_name),'%s/%s'%(_dstdir,backgroundiphonex_loading_name))
                                    else:
                                          shutil.copyfile('%s/%s'%(dir,img_name),'%s/%s'%(_dstdir,backgroudiphonex_login_name))



            login_dir = path +'login'
            loading_dir = path +'loading'
            logo_dir = path + 'logo'


            login_image_name = 'backgroud_login.jpg'
            backgroud_loading_name = 'backgroud_loading.jpg'
            backgroudiphonex_login_name = 'backgroudiphonex_login.jpg'
            backgroundiphonex_loading_name = 'backgroudiphonex_loading.jpg'
            folder = 'res'
            isExists = os.path.exists(folder)

            logo_lylc_name = 'logo_lylc.png'
            if projectName == 'zbcq':
                logo_lylc_name = 'logo_tdcj.png'
            print ('loading....')
            if  isExists:
                  # os.system('rm -rf ./%s'%(folder))
                  os.system('rm -rf ./%s/.DS_Store'%(dir_name))
                  os.system('rm -rf ./%s/.DS_Store' % (login_dir))
                  os.system('rm -rf ./%s/.DS_Store' % (loading_dir))

            #'/assets/res/big'
            modify_images(loading_dir, 0,dir_name_ioshd)
            modify_images(login_dir, 1,dir_name_ioshd)
            #'Resources/res/big'
            modify_images(loading_dir, 0)
            modify_images(login_dir, 1)

            for root, dirs, files in os.walk(logo_dir):
                  for img_name in files:
                        path = os.path.join(root, img_name)
                        img = Image.open(path)
                        width, height = img.size
                        if width!=780 and height != 401:
                              out = img.resize((780, 401))
                              out.save(path, 'png')
                        shutil.copyfile('%s/%s' % (logo_dir, img_name), '%s/%s' % (dir_name, logo_lylc_name))
                        shutil.copyfile('%s/%s' % (logo_dir, img_name), '%s/%s' % (dir_name_ioshd, logo_lylc_name))

            print('image finish....')

      pass

      @staticmethod
      def modify_images(dir_name,yfy_dir,isIcon=True):
            arr = [20,29,40,60,58,76,80,87,120,180,152,167,1024]
            for root, dirs, files in os.walk(yfy_dir):
                  for img_name in files:
                        if img_name != '.DS_Store':
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
                                  # if width == 1024:
                                  #     img = img.convert('RGBA')
                                  #     img_blender = Image.new('RGBA', img.size, (0, 0, 0, 0))
                                  #     img = Image.blend(img_blender, img, 1)
                                  #     out = img.resize((1024, 1024))
                                  #     out.save(path, 'png')


                                  shutil.copyfile('%s/%s' % (yfy_dir, img_name),'%s/%dx%d.png' % (dir_name, width,height))
                              else:
                                      shutil.copyfile('%s/%s' % (yfy_dir, img_name),
                                                      '%s/%dx%d.png' % (dir_name, width, height))

      @staticmethod
      def start_icon_image(yfy_path):

          asset = 'Assets.xcassets/'
          if projectName == 'zbcq':
              asset = 'DTQCQHZB/Images.xcassets/'
          elif projectName == 'lycq':
               asset = '/ios/Images.xcassets/'
          appicon_dirname = 'AppIcon_defualt.appiconset'
          path = xcodeprojPath + asset + appicon_dirname
          isExists = os.path.exists(path)
          if not isExists:
              os.mkdir(path)
              print(path + ' creat success')
          else:
              print(path + ' isexist')
              shutil.rmtree(path)
              os.mkdir(path)
          for root, dirs, files in os.walk('icon_json'):
              for json_name in files:
                    shutil.copyfile('%s/%s' % (root, json_name), '%s/%s' % (path, json_name))

          modifyImage_cls.modify_images(path, yfy_path)
          pass


      @staticmethod
      def start_launchimage(yfy_path,isIcon = False):
          asset = '\Assets.xcassets/'
          if projectName == 'zbcq':
            asset = 'DTQCQHZB/Images.xcassets/'
          elif projectName == 'lycq':
              asset = '/ios/Images.xcassets/'

          appicon_dirname = 'LaunchImage_defualt.launchimage'
          path = xcodeprojPath + asset + appicon_dirname
          isExists = os.path.exists(path)
          if not isExists:
             # shutil.rmtree(path)
             os.mkdir(path)
             print(path + ' creat success')
          else:
             print(path + ' isexist')
             shutil.rmtree(path)
             os.mkdir(path)

          #contents.json copy project dir
          for root, dirs, files in os.walk('launchimage_json'):
                for json_name in files:
                    shutil.copyfile('%s/%s' % (root, json_name), '%s/%s' % (path, json_name))

          modifyImage_cls.modify_images(path,yfy_path,isIcon)
          pass

      @staticmethod
      def start():
          basePath = projectPath + '/' + ioshd + '/images/'
          # basePath = '/Users/yu/Documents/FangCloudSync/协作_出包排期/游戏猫/正版传奇/20180802-5060/烈火雷霆_游戏猫越狱出包需求/烈火雷霆_游戏猫越狱出包需求/打包素材/'
          yfy_launchimage_path = basePath + 'launchimage'
          yfy_icon_path = basePath + 'icon'
          isExists = os.path.exists(yfy_launchimage_path)
          if isExists:
              modifyImage_cls.start_launchimage(yfy_launchimage_path)
          else:
              print(yfy_launchimage_path, 'dir is not exist')
          if os.path.exists(yfy_icon_path):

              modifyImage_cls.start_icon_image(yfy_icon_path)
          else:
              print(yfy_icon_path, 'dir is not exist')
          modifyImage_cls.start_main_image(basePath)
          
if __name__ == '__main__':
    modifyImage_cls.start()