
debug = False


package_method = 2  #1 app-store, 2 ad-hoc,3  enterprise, 4 development。
#docker
BasePath= '/var/project'
#debug
if debug:
    BasePath = '/Users/yu/Desktop/gameProject'
ExportOptionsPath = BasePath + '/ipa'

projectName = 'lycq'

targetName = 'lthtaw115'

channelNo="20935"

ioshd = 'ios_hd10test'

PluginConfig = 'Error'
projectPath = 'Error'
if projectName == 'lycq':
    projectPath = BasePath +'/lycq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/ios_hd2/ios/PluginConfig.xml'
elif projectName == 'zbcq':
    projectPath = BasePath + '/zbcq-client_version/CocosLuaGame/'
    PluginConfig = projectPath + '/ios/PluginConfig.xml'

elif projectName == 'h5':
    projectPath = BasePath + '/H5_iOS/XFGame_WKWebView/XFGame_WKWebView/'


xcodeprojPath = projectPath + 'frameworks/runtime-src/proj.ios_mac/'




bundleid = "com.lhlt.xhtt.i4"

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
         'provisioningProfiles': {bundleid: "ktby_dis20180705"},
         }




