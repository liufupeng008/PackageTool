# -*- coding: UTF-8 -*-
from config import *
from compile_index import compile_index
from modifyPlist import modifyPlist
from modifyXML import modifyXML
from modifyImage import modifyImage_cls

class Main():
      @staticmethod
      def start():
          # src res sum luac
          # compile_index.encode_src()
          compile_index.copy_manifestToResources()
          modifyPlist.start()
          modifyXML.start_modify_xml(channelNo)
          # modifyImage_cls.start()

          pass


if __name__ == '__main__':
    Main.start()
    pass