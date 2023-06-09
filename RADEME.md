# ros机器人期末操作
上机没有操作环境就去安装，要的文件U盘里有
vmvare Ubuntu.14.0.4.iso
## 安装ros
使用Ubuntu14.0.4安装ros开发环境

CTRL + alt + T打开Termial（终端）
切换软件源（中科大软件源）
```bash
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
```
设置公钥
```bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```
更新软件缓存
```bash
sudo apt update
```
安装ros（Ubuntu14.0.4用indigo版本）
```bash
sudo apt-get install ros-indigo-desktop-full
```
## 使用ros
初始化操作环境
```bash
sudo rosdep init
```
```bash
rosdep update
```
这里可能会出很多问题,导致初始化失败
最好就是用手机wifi,如果失败的话,多尝试几次,有可能是网络问题.

设置环境
```bash
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
```
```bash
source ~/.bashrc
```
测试ros是否安装成功
```bash
roscore
```
## 使用ros
### 小乌龟
 打开新的Termial

新建一个小乌龟画面
```bash
rosrun turtlesim turtlesim_node
```
 打开新的Termial，输入以下命令，可以在Termial中通过键盘上的方向键控制小乌龟的移动
 ```bash
 rosrun turtlesim turtle_teleop_key
 ```
 ### 创建ros程序
 创建catkin工作空间

 创建一个目录
 ```bash
 mkdir -p ~/catkin_ws/src
 ```
 进入目录,生成工作空间的相关文件
 ```bash
 cd ~/catkin_ws
 catkin_make
 ```
创建ros包

修改包的信息

在包目录下有个package.xml文件，记录的包原始数据信息

修改包的名称，版本等信息
```xml
<name>myrobot</name><!-->包名-->
<version>0.0.0.0</version><!-->版本信息-->
<description></description><!-->包的描述-->
<license>TODO</license><!-->许可-->
```
加入ros包路径

列出与ros有关的环境变量
```bash
env|greb ROS
```
新建的catkin工作空间加入包的搜索路径
```bash
source ~/catkin_ws/devel/setup.bash
```
编译包
```bash
cd ~/catkin_ws
catkin_make
```
### ros图形工具
安装rqt工具
```bash
sudo apt-get install ros-indigo-rqt
sudo apt-get install ros-indigo-rqt-common-plugins
```
运行rqt
```bash
rqt
```
### action程序编写
创建action

定义action文件，一般在action目录中，扩展名也是一样
```bash
roscd myrobot
mkdir action
vi action/test.action
```
输入以下内容
```bash
#goal time to wait
int64 goal_time
---
#result
#final time
int 64 finished_time
---
#feedback
int 64 remained_time
```
编译

在CMakelist.txt文件中加入以下内容
```js
find_package(
    catin REQUIRED
    genmsg
    actionlib_msgs
    actionlib
)
add_action_files(
    DIRECTORY action
    FILES
    test.action
)
genrate_messages(
    DEPENDENCIES
    actionlib_msgs
    std_msgs
)
catkin_package(
    CATKIN_DEPENDS
    actionlib_msgs
)
```
在package.xml文件中加入以下内容
```xml
<build_depend>actionlib</build_depend>
<build_depend>actionlib_msgs</build_depend>
<exec_depend>actionlib</exec_depend>
<wxwc_depend>actionlib_msgs</exec_depend>
```
用下面命令编译
```bash
cd ~/cakin_ws
catkin_make
```
