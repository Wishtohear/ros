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