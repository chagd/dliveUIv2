#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PointStamped

import utm

from geometry_msgs.msg import Pose2D

def callback(msg):
    #print msg
    x = float(msg.point.x) + 714244.59
    y = float(msg.point.y) + 3159474.69
    point = utm.to_latlon(x, y, 43, 'R')
    print point
    print ""

rospy.init_node('set_goal_rviz', anonymous=True)

rospy.Subscriber('clicked_point', PointStamped, callback = callback)

rospy.spin()