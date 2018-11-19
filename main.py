# -*- coding: UTF-8 -*-
from config import *
from compile_index import compile_index
from modifyPlist import modifyPlist
from modifyXML import modifyXML
from modifyImage import modifyImage_cls
from exportArchive import exportArchive
import time
class Main():
      @staticmethod
      def start():
          # src res sum luac
          # compile_index.copyfileToResources()
          compile_index.copy_ioshd_to_Resources()
          modifyPlist.start()
          modifyXML.start_modify_xml(channelNo)
          modifyImage_cls.start()
          #  '/Users/yu/Library/Developer/Xcode/DerivedData'
          # exportArchive.start_archive()
          pass


if __name__ == '__main__':
    Main.start()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(localtime)
    pass