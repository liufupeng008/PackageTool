isxfad_hoc = True

BasePath= '/Users/yu/Desktop/gameProject'
ExportOptionsPath = '/Users/yu/Desktop/'

# projectPath = BasePath +'/lycq-client_version/CocosLuaGame/'
projectPath = BasePath + '/H5_iOS/XFGame_WKWebView/XFGame_WKWebView/'

targetName = 'H5LYSC'






xfplist = {'compileBitcode': False,
         'method': "ad-hoc", #app-store, ad-hoc, enterprise, development。
         'provisioningProfiles': {"com.game.shengshiwuzun": "xfyx_neibu_adhoc_20170408"},
         'signingCertificate': "iPhone Distribution",
         'signingStyle': "manual",
         "stripSwiftSymbols": True,
         "teamID": "ML2L65XZJL",
         "thinning": '<none>'
         }
otherplist = {'compileBitcode': False,
         'method': "ad-hoc",
         'provisioningProfiles': {"com.game.shengshiwuzun": "xfyx_neibu_adhoc_20170408"},
         'signingCertificate': "iPhone Distribution",
         'signingStyle': "manual",
         "stripSwiftSymbols": True,
         "teamID": "ML2L65XZJL",
         "thinning": '<none>'
         }

