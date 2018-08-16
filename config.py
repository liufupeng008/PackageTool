# -*- coding: UTF-8 -*-
debug = False


package_method = 2  #1 app-store, 2 ad-hoc,3  enterprise, 4 development。
#docker
BasePath= '/var/project'
#debug
if debug:
    BasePath = '/Users/yu/Desktop/gameProject'
ExportOptionsPath = BasePath + '/ipa'

projectName = 'lycq'


PluginConfig = 'Error'
projectPath = 'Error'
if projectName == 'lycq':
    projectPath = BasePath +'/lycq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/ios_hd2/ios/PluginConfig.xml'
elif projectName == 'zbcq':
    projectPath = BasePath + '/zbcq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + 'frameworks/runtime-src/proj.ios_mac/' + '/ios/PluginConfig.xml'

elif projectName == 'h5':
    projectPath = BasePath + '/H5_iOS/XFGame_WKWebView/XFGame_WKWebView/'


xcodeprojPath = projectPath + 'frameworks/runtime-src/proj.ios_mac/'

if projectName == 'h5':
    xcodeprojPath = projectPath


channelNo='20813'

projectInfo_dict = {
    #zbcq
    '5060':{'displayName':'赤焰沙城',
            'bundleid':'com.yxm.chiyanshacheng',
            'targetName':'zbcq_tt_yxm_yy',
            'ios_hd':'ios_hd119',
             'yxm_gameId':'xingtuo_chiyanshacheng_1'
            },

    '5062': {'displayName': '霸刀战魂',
             'bundleid': 'com.yxm.badaozhanhun',
             'targetName': 'zbcq_tt_yxm_yy',
             'ios_hd': 'ios_hd121',
             'yxm_gameId':'xingtuo_badaozhanhun_1'},

    '5064': {'displayName': '决战龙城',
             'bundleid': 'com.yxm.longchengjuezhan',
             'targetName': 'zbcq_tt_yxm_yy',
             'ios_hd': 'ios_hd122',
             'yxm_gameId':'xingtuo_longchengjuezhan_1'},

    '12030': {'displayName': '雷霆战神',
             'bundleid': 'com.ltzs.jjyx',
             'targetName': 'zbcq_tt_yxm_yy',
             'ios_hd': 'ios_hd117',
             'yxm_gameId':'xingtuo_longchengjuezhan_1'},
    #lycq
    '20813': {'displayName': '烈焰武尊',
             'bundleid': 'com.xf.lywz.tz',
             'targetName': 'tzlywz27',
             'ios_hd': 'ios_hd27',
             'yxm_gameId':'xingtuo_longchengjuezhan_1'}



}
projectInfo = projectInfo_dict[channelNo]
targetName = projectInfo['targetName']
displayName = projectInfo['displayName']
bundleid = projectInfo['bundleid']
ioshd = projectInfo['ios_hd']
# print(projectInfo)

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



