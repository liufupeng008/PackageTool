# -*- coding: UTF-8 -*-
from config_game.lycq_config import *
from config_game.zbcq_config import *

debug = True


package_method = 2  #1 app-store, 2 ad-hoc,3  enterprise, 4 development。
#docker
BasePath= '/var/project'
#debug
if debug:
    BasePath = '/Users/yu/Desktop/gameProject'
ExportOptionsPath = BasePath + '/ipa'

projectName = 'zbcq'


PluginConfig = 'Error'
projectPath = 'Error'
projectInfo_dict = {}
ChannelSdk = ''
channelNo=''
if projectName == 'lycq':
    print('kakak')
    projectPath = BasePath +'/lycq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/ios_hd2/ios/PluginConfig.xml'
    projectInfo_dict = lyprojectInfo_dict
    ChannelSdk = lyChannelSdk
    channelNo = lychannelNo
elif projectName == 'zbcq':
    projectPath = BasePath + '/zbcq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + 'frameworks/runtime-src/proj.ios_mac/' + '/ios/PluginConfig.xml'
    projectInfo_dict = zbprojectInfo_dict
    ChannelSdk = zbChannelSdk
    channelNo = zbchannelNo

elif projectName == 'h5':
    projectPath = BasePath + '/H5_iOS/XFGame_WKWebView/XFGame_WKWebView/'


xcodeprojPath = projectPath + 'frameworks/runtime-src/proj.ios_mac/'

if projectName == 'h5':
    xcodeprojPath = projectPath

ioshd = ''
bundleid = ''
try:
    projectInfo = projectInfo_dict[ChannelSdk]['info'][channelNo]
    # print(projectInfo)
    targetName = projectInfo_dict[ChannelSdk]['targetName']
    displayName = projectInfo['displayName']
    bundleid = projectInfo['bundleid']
    ioshd = projectInfo['ios_hd']
    urlsechems = projectInfo['urlsechems']
except Exception as e:
    pass
# ioshd = 'ios_hd133'
try:
    TIANTUOAPPID = projectInfo['TIANTUOAPPID']
except Exception as e:
     pass

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
         'provisioningProfiles': {bundleid: "tushenh5_dis_20180730"},
         }



