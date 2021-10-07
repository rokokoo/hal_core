#!/usr/bin/env python3
import rospy
import subprocess
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100) # 10000hz
    while not rospy.is_shutdown():
        information = subprocess.run(['halcmd','getp','lcec.0.7.enc-0-pos'], capture_output=True).stdout.decode('utf-8').strip() 
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(information)
        pub.publish(information)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
