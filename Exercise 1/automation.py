#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
 
# Time in ROS
def time():
   return rospy.get_rostime().secs + (rospy.get_rostime().nsecs/1e9)
 
# Stop robot
def stop():
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0
   pub.publish(t)
 
# Move robot
def move():
   # Topic to move
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
   rospy.init_node('movement_robot', anonymous=True)
   rospy.sleep(1)
   # Initialize counter
   tempo = time()
   # Will send message until stop the code
   while not rospy.is_shutdown():
       if time() - tempo <= 3:
           t = Twist()
           t.linear.x = 1
           t.linear.y = 0
           t.linear.z = 0
           t.angular.x = 0
           t.angular.y = 0
           t.angular.z = 0
           pub.publish(t)
       elif time() - tempo > 3 and time() - tempo <= 5:
           stop()
       elif time() - tempo > 5 and time() - tempo <= 7:
            t = Twist()
            t.linear.x = 0
            t.linear.y = 1
            t.linear.z = 0
            t.angular.x = 0
            t.angular.y = 0
            t.angular.z = 1
            pub.publish(t)
       elif time() - tempo > 7 and time() - tempo <= 8:
            stop()
       elif time() - tempo > 8 and time() - tempo <= 11:
            t = Twist()
            t.linear.x = -0.5
            t.linear.y = 0
            t.linear.z = 0
            t.angular.x = 0
            t.angular.y = 0
            t.angular.z = 0
            pub.publish(t)
       elif time() - tempo > 11:
            stop()
       else:
           tempo = time()   
 
if __name__ == '__main__':
   try:
       move()
   except rospy.ROSInterruptException:
       pass
