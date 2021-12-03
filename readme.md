# A SLAM demo for turtlebot in simulated world

## Setup simulation eviroment
### Single machine
```
roslaunch simulation gazebo_turtleworld.launch
roslaunch simulation gazebo_hospital.launch
```
### Multiple machine
#### Server
```
export GAZEBO_MASTER_URI=192.168.2.16:11345
export GAZEBO_IP=192.168.2.16
```
#### Client
```
export GAZEBO_MASTER_URI=192.168.2.16:11345
export GAZEBO_IP=192.168.2.39
```
#### Server
```
roslaunch simulation gzserver_turtleworld.launch
roslaunch simulation gzserver_hospital.launch
```
#### Client
```
roslaunch simulation gzclient.launch
```
---
## Telelop
### Joystick
```
roslaunch teleop teleop_joystick.launch
```
### Joystick
```
roslaunch teleop teleop_joystick.launch
```
### Keyboard
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
## SLAM
### Gmapping
```
roslaunch simulation slam_gmapping.launch 
```
### Hector
```
roslaunch simulation slam_hector.launch
```
### Cartographer
```
roslaunch simulation slam_cartographer.launch
```
