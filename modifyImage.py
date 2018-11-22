import os
import shutil
from PIL import Image
from config import *
class modifyImage_cls():

      @staticmethod
      def start_main_image(path=''):
            project_root_path = projectPath
            dir = ''
            if projectName == 'gzcq':
                dir = 'ios_hd/'
            dir_name_ioshd = project_root_path +dir+ ioshd + '/assets/res/big'
            dir_name = project_root_path +'Resources/res/big'

            def modify_images(dir,var,dstdir=''):
                  for root, dirs, files in os.walk(dir):
                        _files = list(filter(lambda x:x!='.DS_Store',files))
                        for img_name in _files:
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
                  _files = list(filter(lambda x: x != '.DS_Store', files))
                  for img_name in _files:
                        path = os.path.join(root, img_name)
                        img = Image.open(path)
                        width, height = img.size
                        if width!=780 and height != 401:
                              out = img.resize((780, 401))
                              out.save(path, 'png')
                        shutil.copyfile('%s/%s' % (logo_dir, img_name), '%s/%s' % (dir_name, logo_lylc_name))
                        shutil.copyfile('%s/%s' % (logo_dir, img_name), '%s/%s' % (dir_name_ioshd, logo_lylc_name))

            print('图片处理 finished')

      pass

      @staticmethod
      def modify_images(dir_name,yfy_dir,isIcon=True):
            arr = [20,29,40,60,58,76,80,87,120,180,152,167,1024]
            launchimage_arr = ['640x960','640x1136','750x1334','768x1024','828x1792','1024x768',
                               '1125x2436','1242x2208','1242x2688','1536x2048','1792x828',
                               '2048x1536','2208x1242','2436x1125','2688x1242']
            needless = []
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
                                      # os.rename('%s/%s' % (yfy_dir, img_name), '%s/%dx%d-1.png' % (yfy_dir, img_name))
                                      if width == 40:
                                          shutil.copyfile('%s/%s' % (yfy_dir, img_name),
                                                          '%s/%dx%d-2.png' % (dir_name, width, height))
                                          # os.rename('%s/%s' % (yfy_dir, img_name),'%s/%dx%d-2.png' % (yfy_dir, img_name))
                                  # if width == 1024:
                                  #     img = img.convert('RGBA')
                                  #     img_blender = Image.new('RGBA', img.size, (0, 0, 0, 0))
                                  #     img = Image.blend(img_blender, img, 1)
                                  #     out = img.resize((1024, 1024))
                                  #     out.save(path, 'png')


                                  shutil.copyfile('%s/%s' % (yfy_dir, img_name),'%s/%dx%d.png' % (dir_name, width,height))
                                else:
                                    needless.append(width)
                                    if os.path.exists('%s/%s' % (yfy_dir, img_name)):
                                        os.remove('%s/%s' % (yfy_dir, img_name))

                              else:
                                      src_img_name = '%s/%s' % (yfy_dir, img_name)
                                      launchimage_name = '%dx%d'% (width, height)
                                      if launchimage_name in launchimage_arr:
                                        shutil.copyfile(src_img_name,
                                                      '%s/%dx%d.png' % (dir_name, width, height))
                                      else:
                                          if os.path.exists(src_img_name):
                                              os.remove(src_img_name)

            print('尺寸不对个数:',len(needless), needless,)

            print('尺寸应该是:', len(arr), arr, )

      @staticmethod
      def start_icon_image(yfy_path):
          appicon_dirname = 'AppIcon_defualt.appiconset'

          asset = 'Assets.xcassets/'
          if projectName == 'zbcq':
              asset = 'DTQCQHZB/Images.xcassets/'
          elif projectName == 'lycq':
               asset = '/ios/Images.xcassets/'
          elif projectName == 'h5':
                appicon_dirname = 'AppIcon_%s.appiconset' % (targetName)
          elif projectName == 'gzcq':
              asset = '/ios/Images.xcassets/'
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
          asset = 'Assets.xcassets/'
          appicon_dirname = 'LaunchImage_defualt.launchimage'

          if projectName == 'zbcq':
            asset = 'DTQCQHZB/Images.xcassets/'
          elif projectName == 'lycq':
              asset = '/ios/Images.xcassets/'
          elif projectName == 'gzcq':
              asset = 'ios/Images.xcassets/'
          elif projectName == 'h5':
            appicon_dirname ='LaunchImage_%s.launchimage'%(targetName)
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
          dir = ''
          if projectName == 'gzcq':
              dir = 'ios_hd/'
          basePath = projectPath + dir + ioshd + '/images/'
          # basePath = '/Users/yu/Documents/FangCloudSyncSvn/协作_出包排期/优洽/屠神H5/【优洽】-新包】-iOS《屠龙单机》/2、出包素材（必须）/'
          # basePath = '/Users/yu/Documents/FangCloudSyncSvn/协作_出包排期/优洽/屠神H5/【优洽】-新包-iOS《帝指沙城》/2、出包素材（必须）/'
          # basePath = '/Users/yu/Documents/FangCloudSyncSvn/协作_出包排期/2.仙峰/4.H5/20181011-新包-(复古霸业)/'
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
          if projectName != 'h5':
             modifyImage_cls.start_main_image(basePath)
          
if __name__ == '__main__':
    modifyImage_cls.start()