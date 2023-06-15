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
最好就是用手机wifi,如果失败的话,多尝试几次,有可能是网络问题.或者加上GitHub加速器
```bash
curl https://ghproxy.com/https://github.com/dotnetcore/FastGithub/releases/download/2.1.4/fastgithub_linux-x64.zip
```

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
创建ros包,第一个参数是包的名称，后面的是项目的依赖包，可以给很多个
```bash
cd ~/catkin_ws/src
catkin_create_pkg myrobot std_msgs rospy roscpp
```
修改包的信息

在包目录的src/myrobot下有个package.xml文件，记录的包原始数据信息

修改包的名称，版本等信息
```xml
<name>myrobot</name><!-->包名-->
<version>0.0.0.0</version><!-->版本信息-->
<description></description><!-->包的描述-->
<license>TODO</license><!-->许可-->
```
修改包的依赖信息
```xml
<build_depend>roscpp</build_depend>
<build_depend>rospy</build_depend>
<build_depend>std_msgs</build_depend>
<build_export_depend>roscpp</build_export_depend>
<build_export_depend>rospy</build_export_depend>
<build_export_depend>std_msgs</build_export_depend>
<exec_depend>roscpp</exec_depend>
<exec_depend>rospy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```
加入ros包路径

列出与ros有关的环境变量,其中ROS_PACKAGE_PATH变量是ROS的包路径
```bash
env|grep ROS
```
要将新建的catkin工作空间加入包的搜索路径
```bash
source ~/catkin_ws/devel/setup.bash
```
编译包，python语言需要给文件添加权限
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
cd ~/catkin_ws
catkin_make
```
编译结果产生以下信息就表示成功了
```c++
testAction.msg;
testGoal.msg;
testResult.msg;
testFeedback.msg;
testActionFeedback.msg;
testActionResult.msg;
testActionGoal.msg;
```
### 编写action服务端和客户端
编写服务端

创建testserver.py文件，内容如下
```python
# ! /usr/bin/env python
#testserver.py
import rospy
import time
import actionlib
from myrobot.msg import testAction,testGoal,testResult,testFeedBack

def do_time(goal):
    fineshed_time = 0
    if goal.goal_time>60:
       #如果 goal_time)60则不提供服务
        result = testResult()
        result. finished_time = finished_time
#创建一个结果类
        server. set_aborted(result,"The goal num must less then 60")#把状态设为终止，两个参数，一个结果类，一个返回的字符串信息return
    while finished_time<goal. goal_time :
#任务处理循环
        if server. is_preempt_requested():
#判断任务是否被其他客户抢占，如果被抢占，则
            result = testResult()
            result. finished_time = finished_time
#创建一个结果类
            server. set_preempted(result,"server is preempted")
#设为被抢占状态，返回一个字符串信息
        return
    time. sleep(1.0)
    finished_time += 1
#睡眠1秒，finished_time加1
    feedback = testFeedback()
    feedback. remained_time = goal. goal_time-finished_time
#创建反馈类
    server. publish_feedback(feedback)
#发布反馈状态，参数是一个反馈类变量
#任务处理循环结束后，处理最后的结果
result = testResult()
result. finished_time = finished_time
#创建一个结果类
server. set_succeeded(result,"completed")
#设置服务状态为成功
if__name__=="__mian__":
rospy.init_node("testserve")
server= actionlib.SimpleActionServer("test",testAction,do_time,False)
server.start()
rospy.spin()

```
编写客户端

创建testclient.py文件，内容如下
```python
# ! /usr/bin/env python
#testlient.py
import rospy 
import time 
import actionlib#引入actionlib库
from myrobot.msg import testAction, testGoal, testResult, testFeedback
#引入action编译产生的消息类
def feedback_cb(feedback):
#定义一个回调函数，处理服务端的中间反馈，参数feedback是testFeedback类型的变量
    rospy. loginfo("Feedback"+str(feedback. remained time))
rospy. init_node("testclient")
client = actionlib. SimpleActionClient("test",testAction)
client. wait_for_server()
#连接服务器
goal = testGoal()
goal. goal_time = 10#构造一个目标
client. send_goal(goal,feedback_cb=feedback_cb)
#发送目标到服务端，并设置一个回调函数用于处理服务返回的中间状态
client. wait_for_result()
#等待服务端结束
rospy. loginfo("finished test action")
```
运行

运行前先设置好权限
```bash
chmod +x test*.py
```
然后依次运行
```bash
roscore
rosrun myrobot testserver.py
rosrun myrobot testlient.py
```