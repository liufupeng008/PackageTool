import os,sys
from config import *
import shutil
from modifyPlist import modifyPlist


import os
class exportArchive():

    @staticmethod
    def start_archive():
        modifyPlist.start_modify_plist(xcodeprojPath)
        import time
        # archivePath = xcodeprojPath+'archive'
        # if os.path.exists(archivePath):
        #     shutil.rmtree(archivePath)
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('start archive ',localtime)
        os.system('./sNextBuild.sh %s %s'%(targetName,projectPath))

        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('start archive ', localtime)
        print('finished archive ', endtime)
        pass





if __name__ == '__main__':
    exportArchive.start_archive()


# nowtime=$(date "+%Y-%m-%d-%H:%M:%S")
#
# echo "start archive ${nowtime}"
#
# time=$(date "+%Y%m%d%H%M%S")
#
# ipaname="${targetName}_${time}"
#
# archivePath="archive/${ipaname}.xcarchive"
#
# xcodebuild archive -project "CocosLuaGame.xcodeproj" -scheme ${targetName} -configuration ${configuration} -archivePath ${archivePath}
#
# nowtime=$(date "+%Y-%m-%d-%H:%M:%S")
# echo "start exportArchive ${nowtime}"
#
# nowtime=$(date "+%Y-%m-%d-%H:%M:%S")
# exportPath="/Users/yu/Desktop/ipa/${targetName}/${nowtime}"
#
# xcodebuild -exportArchive -archivePath ${archivePath} -exportPath ${exportPath}  -exportOptionsPlist ExportOptions.plist -allowProvisioningUpdates
#
# echo "finish exportArchive"
#
# time=$(date "+%Y%m%d%H%M%S")
#
# cd ${exportPath} && mv "${targetName}.ipa" "${targetName}${time}.ipa"
#
# cd ${projectPath} && rm -rf archive