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
