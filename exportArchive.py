import os,sys
from config import *
import shutil
from modifyPlist import modifyPlist
import re

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
        a = re.split('\W+', bundleid, flags=0)
        print(a)
        p = re.sub("[A-Z]", "", a[len(a)-1])

        os.system('./sNextBuild.sh %s %s %s'%(targetName,projectPath,p))

        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('start archive ', localtime)
        print('finished archive ', endtime)
        pass




    @staticmethod
    def alter(old_str, new_str):
        dir = ''
        if projectName =='gzcq':
            dir = 'ios_hd/'
        current_dir = projectPath +dir+ ioshd + '/src_origin/'
        file = current_dir + 'platform/' + 'PlatformConfig.lua'

        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                if old_str in line:
                    f2.write(re.sub(line, old_str + new_str+'\n', line))
                    print(old_str + new_str+'\n')
                elif '_G_IAP_ITEM_GONFIG_ =' in line:
                    print(line)
                    f2.write(line)
                else:
                    f2.write(line)

            os.remove(file)

        os.rename("%s.bak" % file, file)


    # alter("_G_GAME_ID = ", "1442743856")


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