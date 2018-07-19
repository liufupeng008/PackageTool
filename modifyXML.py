# -*- coding: UTF-8 -*-

# 导入xml包
import xml.etree.ElementTree as ET
class modify_xml():

    @staticmethod
    def start_modify_xml(val):
        # 解析dimen.xml
        # dir = '/var/project/lycq-client_version/CocosLuaGame/ios_hd2/ios/PluginConfig.xml'
        dir = ''
        try:
            dir = PluginConfig + '/ios/PluginConfig.xml'
        except NameError as e:
                dir = '/Users/yu/Desktop/gameProject/zbcq-client_version/CocosLuaGame/frameworks/runtime-src/proj.ios_mac/ios/PluginConfig.xml'

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
        else:
            print('error 没有可改变tag')



if __name__ == '__main__':
    import sys
    # print(sys.argv[1])
    val = sys.argv[1]
    # var = channelNo
    if val:
      modify_xml.start_modify_xml(val)