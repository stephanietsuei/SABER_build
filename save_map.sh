#!/usr/bin/env bash
export TURTLEBOT3_MODEL="waffle"
mkdir -p `pwd`/src/SABR/maps
rosrun map_server map_saver -f `pwd`/src/SABR/maps/world4
rosnode kill -a; killall -9 rosmaster; killall -9 roscore
roslaunch sabr_pkg sabr_gazebo_collect.launch
