#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import inputs

VX_MAX = 0.5
VW_MAX = 1.5
DEAD_BAND = 20.0

if __name__=="__main__":
  rospy.init_node('teleop')
  pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
  
  try:
    gamepad = inputs.devices.gamepads[0]
  except IndexError:
    raise inputs.UnpluggedError("No gamepad found.")

  rospy.loginfo("Joystick name: {}".format(gamepad.name))

  v = .0
  w = .0

  while not rospy.is_shutdown():
    try:
      events = gamepad.read()
    except EOFError:
      events = []

    updated = False

    for event in events:
      if event.ev_type == 'Absolute':
        if event.code == 'ABS_Y':
          v = event.state
          v = -v + 127
          if abs(v) < DEAD_BAND:
            v = 0
          else:
            v -= (v/abs(v)) * DEAD_BAND
          v = v / (127 - DEAD_BAND) * VX_MAX
          updated = True
        elif event.code == 'ABS_X':
          w = event.state
          w = -w + 127
          if abs(w) < DEAD_BAND:
            w = 0
          else:
            w -= (w/abs(w)) * DEAD_BAND
          w = w / (127 - DEAD_BAND) * VW_MAX
          updated = True

    if updated:

      rospy.loginfo("%f %f" % (v, w))

      twist = Twist()
      twist.linear.x = v; twist.linear.y = 0.0; twist.linear.z = 0.0
      twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = w

      pub.publish(twist)
