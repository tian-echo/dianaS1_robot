#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import moveit_commander
from math import pi


class MoveItFkDemo:
    def __init__(self):

        # 初始化move_group的API,出现roscpp是因为底层是通过C++进行实现的
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点，节点名为'moveit_fk_demo'
        rospy.init_node('moveit_fk_demo', anonymous=True)

        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('dianaS1_arm')

        # 设置机械臂运动的允许误差值，单位弧度
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度，范围0~1
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)


        joint_goal = arm.get_current_joint_values()
        joint_goal[0] = pi/6
        joint_goal[1] = -pi/4
        joint_goal[2] = pi/2
        joint_goal[3] = -pi/2
        joint_goal[4] = pi/4
        joint_goal[5] = pi/3
        joint_goal[6] = 0


        arm.go(joint_goal)
        rospy.sleep(1)
    # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)

    # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)


if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
