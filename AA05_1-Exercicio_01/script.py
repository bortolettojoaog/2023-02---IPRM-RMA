#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from math import floor
from geometry_msgs.msg import Twist
import time

def callback_laser(msg):
   
   laser_raw = msg.ranges
   laser_float = [float(r) for r in laser_raw]
   esquerda = 0
   direita = 0
  
 
   for i in range(len(laser_float)):

      if i >= 0 and i < 278:
         direita = direita + laser_float[i]
      elif i == 279:
         direita = direita + laser_float[i]
         print("diteita total" , direita)
         direita = direita/280
         print("Direita" , direita)

      if i >= 439  and i < 719:
         esquerda = esquerda + laser_float[i]
      elif i == 719:
         esquerda = esquerda + laser_float[i]
         print("esquerda total" , esquerda)
         esquerda = esquerda/280
         print("Esquerda" , esquerda)
   
      #if esquerda == direita:
      #   walk()
      if esquerda > direita:     
         turncc()
         time.sleep(0.1)
         stop()
         walk()
         time.sleep(0.5)
         stop()
      elif esquerda < direita:
         turn()
         time.sleep(0.1)
         stop()
         walk()
         time.sleep(0.5)
         stop()

   esquerda = 0
   direita = 0
   
   
      
 
# Stop robot
def stop():
   pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0
   pub.publish(t)

# turn robot
def turn():
   pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0.1
   pub.publish(t)

# turn robot counterclockwise
def turncc():
   pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = -0.1
   pub.publish(t)

# move robot forward
def walk():
   pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=10)
   t = Twist()
   t.linear.x = 0.5
   t.linear.y = 0
   t.linear.z = 0
   t.angular.x = 0
   t.angular.y = 0
   t.angular.z = 0
   pub.publish(t)




if __name__ == '__main__':
   rospy.init_node("obstacle_check_node")
   rospy.Subscriber("/scan", LaserScan, callback_laser)
   print("Entrei")
   
   rospy.spin()
