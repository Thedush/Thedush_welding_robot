#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from geometry_msgs.msg import Pose
from scipy.interpolate import RegularGridInterpolator
from numpy import linspace, zeros, array
import time
from actionlib_msgs.msg import GoalStatusArray
from geometry_msgs.msg import PoseStamped
import subprocess
from std_msgs.msg import String

def check_workspace(x,y,z):
	if (x > -1 and x <= 1) and (y >= -0.35 and y <= 0.35) and (z >= 0 and z <= 1.5):
		return True
	else:
		return False


if __name__ == '__main__':
	print('Enter x:')
	x1 = input()
	print('Enter y:')
	y1 = input()
	print('Enter z:')
	z1 = input()
	print'The coordinates given is ' +  str(x1),str(y1),str(z1) 

	valid=check_workspace(x1,y1,z1)
	if valid == True:
		print('The point lies inside the Workspace  :) ') 

	else :
	 	print('The Point was outside the workspace :( ')

# current pose 

# 
	x = linspace(0,x1,3)
	y = linspace(0,y1,3)
	z = linspace(0,z1,3)
	print x,y,z
	# for i in range(len(x)):

	# # print z
	# V = zeros((3,3,3))
	# for i in range(3):
	#     for j in range(3):
	#         for k in range(3):
	#             V[i,j,k] = 10*x[i] + 1*y[j] + z[k]

	# # print V
	# fn = RegularGridInterpolator((x,y,z), V)
	# pts = array([[2,6,8],[3,5,7]])
	# print(fn(pts))