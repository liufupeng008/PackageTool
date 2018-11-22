#!/bin/sh

#  Script.sh
#  resourcesTest
#
#  Created by zhou on 2017/3/3.
#  Copyright © 2017年 liufupeng. All rights reserved.




#更改ExportOptions


filePath="$2"
echo "---${filePath}---"
######project路径
projectPath=$filePath/frameworks/runtime-src/proj.ios_mac
#

#产生的ipa目录，签名完之后将ipa保存到哪里 我写的保存在桌面。

#targetName="zbcq_tt_yxm_yy"
#targetName="tiantuo_leyou"
#targetName="xianfeng_shcs"
targetName="$1"
echo "---${targetName}---"
echo "---"$3"---"
#####定义需要打包的target
echo "开始clean"

#更改ExportOptions 需要传入ExportOptionsPlist 文件的目录（也是项目所在目录）
#cd $pythonPath && source activate MyPython && python modifyPlist.py

cd ${projectPath} && rm -rf archive && mkdir archive
configuration="Release"

xcodebuild clean -configuration ${configuration}
xcodebuild build -configuration ${configuration}
nowtime=$(date "+%Y-%m-%d-%H:%M:%S")

echo "start archive ${nowtime}"

time=$(date "+%Y%m%d%H%M%S")



archivePath="archive/${targetName}.xcarchive"

xcodebuild archive -project "CocosLuaGame.xcodeproj" -scheme ${targetName} -configuration ${configuration} -archivePath ${archivePath}

nowtime=$(date "+%Y-%m-%d-%H:%M:%S")
echo "start exportArchive ${nowtime}"

nowtime=$(date "+%Y-%m-%d-%H:%M:%S")
exportPath="/Users/yu/Desktop/ipa/${targetName}/${nowtime}"

xcodebuild -exportArchive -archivePath ${archivePath} -exportPath ${exportPath}  -exportOptionsPlist ExportOptions.plist -allowProvisioningUpdates

echo "finish exportArchive"

time=$(date "+%Y%m%d%H%M%S")

ipaname="$3"
cd ${exportPath} && mv "${targetName}.ipa" "${targetName}${ipaname}${time}.ipa"

#cd ${projectPath} && rm -rf archive

open ${exportPath}



