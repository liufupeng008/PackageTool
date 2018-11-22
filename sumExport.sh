#!/bin/sh

#  Script.sh
#  resourcesTest
#
#  Created by zhou on 2017/3/3.
#  Copyright © 2017年 jett.yu. All rights reserved.


#####工程路径
#渠道号
channelNo=""
#差异文件
ios_hd="$1"
#target
echo "${ios_hd}"
filePath="$2"
strA="long string"
strB="string"
result=$(echo $filePath | grep "gz-client_version")
if [[ "$result" != "" ]]
then

  ios_hd="ios_hd/${1}"
  echo "包含 ${ios_hd}"
else
  echo "不是国战"
fi

echo "---$(pwd)---"
#####project路径
projectPath=$filePath/frameworks/runtime-src/proj.ios_mac

#执行完xcodebuild编译之后，会自动产生一个build目录，这里指定.app目录所在位置，这里的意思是保存在当前项目目录的build下
releaseDir="/build/Release-iphoneos/"

build_path="${projectPath}/build"

cd "${filePath}/export" && svn up

cd "${filePath}"

#在cd到原来项目目录
cd "$filePath"
echo "当前目录:$(pwd)"

#####定义变量appname和ipaname还有资源文件
declare appname
declare isluac


cd ${projectPath}

ios_path=$filePath/Resources

#拷贝icon的目标文件路径
icon_path=$projectPath/ios

##拷贝资源的基路径
ios_base_path="$filePath/export/"

#echo "包名: ${appname[k]}--产品名: ${ipaname[k]}--渠道名:${ios_hd}"

echo "\033[31m正在清空资源文件\033[0m"

cleanPath="$filePath/kong/"
if [ ! -d "$cleanPath" ]; then
mkdir $cleanPath
fi

rsync  --delete-before -rlptD $cleanPath "$ios_path/"

#echo "\033[31m资源清空完毕，正在拷贝资源文件\033[0m"
##这里已清空工程资源路径，执行拷贝基资源
rsync -avu $ios_base_path $ios_path

echo "\033[31m资源拷贝完毕，开始拷贝差异文件\033[0m"


#拷贝资源的渠道差异文件路径
copy_path="$filePath/${ios_hd}/assets/"

echo "路径-------：，${copy_path}"

##这里复制需要差异化文件
cp -r $copy_path $ios_path

echo "合并差异文件完成"

#打印 开始清除
echo clean start

#xcode clean
if  [ -d ${build_path} ];then
rm -rf ${build_path}
echo clean build_path success.
fi
