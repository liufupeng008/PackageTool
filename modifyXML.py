# -*- coding: UTF-8 -*-

# 导入xml包
import xml.etree.ElementTree as ET
from config import *
import os
import shutil
class modifyXML():

    @staticmethod
    def start_modify_xml(val,dir=PluginConfig):
        ioshd_dir = ''

        if projectName == 'gzcq':
            ioshd_dir = 'ios_hd/'
        print(dir)
        # try:
        #     dir = PluginConfig
        # except NameError as e:
        #         dir = '/Users/yu/Desktop/gameProject/zbcq-client_version/CocosLuaGame/frameworks/runtime-src/proj.ios_mac/ios/PluginConfig.xml'

        tree = ET.parse(dir)
        root = tree.getroot()  # 获取根节点
        flag = False
        for common in root.iter('common'):
            for id in common.iter('id'):
                 id.text = str(val)
                 flag = True
             # rank.set('updated', 'yes')
        if flag:
            tree.write(file_or_filename=dir,xml_declaration=True, encoding='utf-8')
            print('succeeded channelNo:',val)
            current_dir = projectPath + ioshd_dir +ioshd + '/ios/PluginConfig.xml'
            if os.path.exists(dir):
                shutil.copyfile(dir, current_dir)

        else:
            print('error tag')



if __name__ == '__main__':
    import sys
    # print(sys.argv[1])
    # val = sys.argv[1]
    val = channelNo
    if val:
        modifyXML.start_modify_xml(val)