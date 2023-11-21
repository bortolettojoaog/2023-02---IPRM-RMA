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

   radius = float(2.2)

   # Will send message until stop the code
   while not rospy.is_shutdown():
       if time() - tempo <= 6:
           t = Twist()
           t.linear.x = 1
           t.linear.y = 0
           t.linear.z = 0
           t.angular.x = 0
           t.angular.y = 0
           t.angular.z = 0
           pub.publish(t)
       elif time() - tempo > 6 and time() - tempo <= 7:
           stop()
       elif time() - tempo > 7:
            t = Twist()
            t.linear.x = 1
            t.linear.y = 0
            t.linear.z = 0
            t.angular.x = 0
            t.angular.y = 0
            t.angular.z = radius

            rospy.loginfo("Radius = %f", radius)
            
            pub.publish(t)
       else:
           tempo = time()   
 
if __name__ == '__main__':
   try:
       move()
   except rospy.ROSInterruptException:
       pass
