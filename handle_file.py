# -*- coding: UTF-8 -*-
import time
import os
from config import *
import json
class Handle_file():


          @staticmethod
          def random_name():
              import random
              import string
              salt = ''.join(random.sample(string.ascii_letters + string.digits, 10))
              salt = salt + '.png'
              print(salt)
              return salt

          @staticmethod
          def get_launchimage_path():
              isExists = os.path.exists(xcassets_path)
              if isExists == True:
                  return xcassets_path + '/LaunchImage_defualt.launchimage/'
              return ''
          @staticmethod
          def get_icon_path():
              isExists = os.path.exists(xcassets_path)
              if isExists == True:
                  return xcassets_path+ 'AppIcon_defualt.appiconset'
              return ''


          @staticmethod
          def handle_launchimage():


              def handle_file(file_path,folder_path):
                  with open(file_path, "r", encoding="utf-8") as f, open("%s.bak" % file_path, "w",
                                                                         encoding="utf-8") as f2:
                      _list = list(f)
                      _list = list(filter(lambda x: x != '' and x != ' ', _list))
                      str_list = list()
                      for index, line in enumerate(_list, start=1):
                          str_list.append(line)
                          # print(line)

                      test_str = "".join(str_list)
                      dictinfo = json.loads(test_str)
                      images = list(dictinfo['images'])
                      for image_info in images:
                          filename = Handle_file.random_name()
                          sourceDirList = os.listdir(folder_path)
                          files = list(filter(lambda x: x != '.DS_Store' and '.png' in x, sourceDirList))
                          print('1')
                          for fi in files:
                              if fi == image_info['filename']:
                                 image_info['filename'] = filename
                                 os.rename("%s/%s" % (folder_path,fi), "%s/%s" % (folder_path,filename))
                              # print(fi)
                              pass
                      #时间复杂度O(n^2)

                      b = str(dictinfo)
                      b = b.replace("'",'"')
                      f2.write(b)
                      print('ll')

                    #     f2.writelines(str(Handle_file.launchimage_dict))
                      os.rename("%s.bak" % file_path, '%s/Contents.json' % folder_path)

              launchimagefilepath =Handle_file.get_launchimage_path() + '/Contents.json'
              launchimage_path = Handle_file.get_launchimage_path()
              iconimagefilepath =  Handle_file.get_icon_path() +  '/Contents.json'
              iconimage_path = Handle_file.get_icon_path()
              handle_file(launchimagefilepath,launchimage_path)
              handle_file(iconimagefilepath,iconimage_path)


          @staticmethod
          def start():
                path = 'files/'
                # path = '/Users/yu/Desktop/zbcq/tiantuo_yxm_zb/CocosLuaGame/frameworks/runtime-src/Classes/'
                path = exportProjectPath
                def gci(filepath):
                    # 遍历filepath下所有文件，包括子目录
                    sourceDirList = os.listdir(filepath)
                    files = list(filter(lambda x: x != '.DS_Store', sourceDirList))
                    for fi in files:
                        fi_d = os.path.join(filepath, fi)
                        if fi == 'protobuf-lite' or fi == 'basetool' or fi == 'scbyCode' or fi == 'resources' \
                                or fi == 'recursive' or fi == 'yxm' or fi == 'YVsdk' \
                                or fi == 'runtime' or fi ==  'userdata' or fi ==  'common' or fi == 'libSdk':
                            continue
                        if os.path.isdir(fi_d):
                            gci(fi_d)
                        elif fi.endswith('.m'):
                            if 'Lib' in fi_d or '.framework' in fi_d or 'AllTool' in fi_d:
                                continue
                            # file_path = os.path.join(filepath, fi_d)
                            print(fi_d)
                            Handle_file.start_handle_file(fi_d)

                gci(path)

          @staticmethod
          def start_handle_file(file_path):
              with open(file_path, "r", encoding="utf-8") as f, open("%s.bak" % file_path, "w",
                                                                     encoding="utf-8") as f2:
                  code_lines = 0  # 代码行数
                  comment_lines = 0  # 注释行数
                  blank_lines = 0  # 空白行数  内容为'\n',strip()后为''
                  is_comment = False
                  start_comment_index = 0  # 记录以'''或"""开头的注释位置
                  _list = list(f)
                  _list = list(filter(lambda x: x != '' and x != ' ', _list))
                  for index, line in enumerate(_list, start=1):
                      # line = line.strip()  # 去除开头和结尾的空白符

                      # 判断多行注释是否已经开始　
                      if not is_comment:
                          # 单行注释
                          if '//' in line:
                              line = line.strip()
                              if line.startswith('//'):
                                  pass
                          # 空白行
                          elif line == '':
                              blank_lines += 1
                              # _list.pop(index)
                          elif line == '\n':
                              pass
                          # 多行注释已经开始
                          elif "/*" in line:
                              line = line.strip()

                              if line.startswith('/*'):
                                  if line.endswith('*/'):
                                      comment_lines = 0
                                  else:
                                      comment_lines = index
                              else:
                                  f2.writelines(line)

                          elif '*/' in line and '/*' not in line:
                              line = line.strip()
                              # if line.endswith('*/') or line.startswith('*/'):
                              # if '/*' in line:
                              #     f2.writelines(line)
                              comment_lines = 0
                          # 代码行
                          else:
                              if comment_lines == 0:
                                  print(line)
                                  f2.writelines(line)
                              pass
                  os.rename("%s.bak" % file_path, file_path)





if __name__ == '__main__':
    Handle_file.handle_launchimage()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localtime)
    pass