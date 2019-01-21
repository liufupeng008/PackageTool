# -*- coding: UTF-8 -*-
from config_game.lycq_config import *
from config_game.zbcq_config import *
from config_game.gzcq_config import *
package_method = 1  #1 app-store, 2 ad-hoc,3  enterprise, 4 development。
#docker
BasePath= '/var/project'
#debug
import os
if os.path.exists(BasePath) ==False:
    # BasePath = '/Users/lindada/Documents/MyWork'
    BasePath = '/Users/yu/Desktop/gameProject'
ExportOptionsPath = BasePath + '/ipa'



projectName = 'lycq'


PluginConfig = 'Error'
projectPath = 'Error'
projectInfo_dict = {}
ChannelSdk = ''
channelNo=''

asset = 'Assets.xcassets/'




if projectName == 'lycq':
    print('kakak')
    projectPath = BasePath +'/lycq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/ios_hd2/ios/PluginConfig.xml'
    projectInfo_dict = lyprojectInfo_dict
    ChannelSdk = lyChannelSdk
    channelNo = lychannelNo
    asset = '/ios/Images.xcassets/'

elif projectName == 'zbcq':
    projectPath = BasePath + '/zbcq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + 'frameworks/runtime-src/proj.ios_mac/' + '/ios/PluginConfig.xml'
    projectInfo_dict = zbprojectInfo_dict
    ChannelSdk = zbChannelSdk
    channelNo = zbchannelNo
    asset = 'DTQCQHZB/Images.xcassets/'


elif projectName == 'gzcq':
    projectPath = BasePath + '/client/gz-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/frameworks/runtime-src/Classes/plugins/bridge/plugin/official/PluginConfig.xml'
    projectInfo_dict = gzprojectInfo_dict
    ChannelSdk = gzChannelSdk
    channelNo = gzchannelNo
    asset = 'ios/Images.xcassets/'


elif projectName == 'h5':
    projectPath = BasePath + '/H5_iOS/XFGame_WKWebView/XFGame_WKWebView/'

versionPath = BasePath +'/version/'+ projectName + '/version/'
xcodeprojPath = projectPath + 'frameworks/runtime-src/proj.ios_mac/'

if projectName == 'h5':
    xcodeprojPath = projectPath

ioshd = ''
bundleid = ''
xcassets_path = xcodeprojPath + asset

try:
    projectInfo = dict(projectInfo_dict[ChannelSdk]['info'][channelNo])
    # print(projectInfo)
    targetName = projectInfo_dict[ChannelSdk]['targetName']
    displayName = projectInfo['displayName']
    bundleid = projectInfo['bundleid']

    ioshd = projectInfo['ios_hd']
    urlsechems = projectInfo['urlsechems']
except Exception as e:
    pass
try:
    TIANTUOAPPID = projectInfo['TIANTUOAPPID']
except Exception as e:
     pass

provisioningProfile = ''
if 'provisioningProfiles' in projectInfo.keys():
    provisioningProfile = projectInfo['provisioningProfiles']
# targetName = 'H5TLDJ'
# targetName = 'H5DZSC'
# targetName = 'H5FGBY'
xfplist = {'compileBitcode': False,
         'method': "ad-hoc", #app-store, ad-hoc, enterprise, development。
         'provisioningProfiles': {bundleid: "xfyx_neibu_adhoc_20170408"},
         }
devplist = {'compileBitcode': False,
         'method': "development",#app-store, ad-hoc, enterprise, development。
         'provisioningProfiles': {bundleid: "425_hh_cqsf_dev"},
         }
appstoreplist = {'compileBitcode': False,
         'method': "app-store",#app-store, ad-hoc, enterprise, development。
         'provisioningProfiles': {bundleid: provisioningProfile},
         }


#配置导出的工程目录
exportProjectPath = '/Users/lindada/Documents/MyStudy/CocosTest/CocosLuaGame/frameworks/runtime-src/Classes'