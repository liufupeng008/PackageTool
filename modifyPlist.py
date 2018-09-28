# -*- coding: UTF-8 -*-
from biplist import *
from config import *

import sys
class modifyPlist():
    import sys
    # sys.reload()
    sys.getdefaultencoding()  # 查看设置前系统默认编码

    # sys.setdefaultencoding('utf8')
    @staticmethod
    def start_modify_plist(path):
        try:
            plist = {}
            if package_method == 1:
                plist = appstoreplist
            elif package_method == 2:
                plist = xfplist
            elif package_method == 4:
                plist = devplist

            writePlist(plist, "%s/ExportOptions.plist"%(path))
            print('plist write success',plist)
        except (InvalidPlistException, NotBinaryPlistException) as e:
            print("Something bad happened:", e)

    @staticmethod
    def read_modify_plist():
        try:
            LSApplicationQueriesSchemes = ['alipays','alipayshare','weixin','wechat','alipayqr','alipay','GameMall']
            if channelNo == '12030':
                LSApplicationQueriesSchemes.remove('GameMall')
            plistPath = xcodeprojPath+targetName+'-info.plist'


            try:
                plist = readPlist(plistPath)
            except FileNotFoundError as e:
                plistPath = xcodeprojPath + targetName + '.plist'
                plist = readPlist(plistPath)
            plist['CFBundleDisplayName']= displayName
            plist['CFBundleIdentifier'] = bundleid
            plist['LSApplicationQueriesSchemes'] = LSApplicationQueriesSchemes
            try:
                plist['TIANTUOAPPID']=TIANTUOAPPID
            except Exception as e:
              pass
            CFBundleURLTypes = plist['CFBundleURLTypes']
            d = CFBundleURLTypes[0]
            CFBundleURLSchemes = d['CFBundleURLSchemes']
            CFBundleURLSchemes[0]=urlsechems
            print(plist)
            writePlist(plist, plistPath)

            # print(plist)
        except InvalidPlistException as e:
            print  ("Not a Plist or Plist Invalid:", e)

    @staticmethod
    def read_modify_YXMListplist():
        try:
            if ChannelSdk == 'tiantuo_yxm':
                YXMPlist_path =  xcodeprojPath + '../Classes/plugins/sdk/tiantuo_yxm/YXMList.plist'
                plist = readPlist(YXMPlist_path)
                plist['gameID'] =  projectInfo['yxm_gameId']
                print(plist)
                writePlist(plist, YXMPlist_path)

            # print(plist)
        except InvalidPlistException as e:
            print("Not a Plist or Plist Invalid:", e)

    @staticmethod
    def start():
        val = xcodeprojPath
        if projectName == 'h5':
            val = val + '../'
        if val:
           modifyPlist.start_modify_plist(val)
           modifyPlist.read_modify_YXMListplist()
           modifyPlist.read_modify_plist()

if __name__ == '__main__':
    modifyPlist.start()