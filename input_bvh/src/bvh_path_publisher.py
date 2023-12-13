#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import os

def path_publisher():
    rospy.init_node('path_publisher', anonymous=True)
    path_pub = rospy.Publisher('bvh_path_topic', String, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Get path input from the command line
        path = input("Enter full path to your bvh file: ")

        # Check if the file path exists, sends path if valid
        if os.path.exists(path):
            rospy.loginfo("Publishing file path: {}".format(path))
            path_pub.publish(path)
        else:
            rospy.logwarn("File path does not exist: {}".format(path))
        rate.sleep()

if __name__ == '__main__':
    try:
        path_publisher()
    except rospy.ROSInterruptException:
        pass

