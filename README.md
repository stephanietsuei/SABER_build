# SABER\_build

This work is currently under review, and use of this code is permitted but requires citation.

## SABER: Data-Driven Motion Planner for Autonomously Navigating Heterogeneous Robots
Authors: Alexander Schperberg, Stephanie Tsuei, Stefano Soatto, and Dennis Hong

This is the catkin environment for the SABER project. It contains the [SABER repository](https://github.com/AlexS28/SABER) and [XIVO ROS](https://github.com/ucla-vision/xivo_ros) as submodules and the [Hector Quadrotor](http://wiki.ros.org/hector_quadrotor) packages as subtrees.

All development on the SABER project can and should be done after cloning this repository.


## Dependencies

1. Ubuntu 18.04
2. ROS Melodic `apt install ros-melodic-desktop-full`
3. Other ROS Packages/Metapackages (Might be incomplete):
    - `apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`
    - `apt install ros-melodic-hardware-interface ros-melodic-controller-interface ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control`
    - `apt install ros-melodic-slam-gmapping`
    - `apt install ros-melodic-turtlebot3`
    - `apt install ros-melodic-geographic-msgs`
4. [SABER repository](https://github.com/AlexS28/SABER)
5. [XIVO ROS wrapper](https://github.com/ucla-vision/xivo_ros) (requires installation of [XIVO](https://github.com/ucla-vision/xivo))

## Build Instructions

Clone all repositories (including submodules)
```
git clone --recursive git@github.com:stephanietsuei/SABER_build.git 
```

Build:
```
cd /path/to/SABER_build
catkin_make
source devel/setup.bash
```

Pull changes, including those to submodules:
```
cd /path/to/SABER_build
git pull --recurse-submodules
```

## DQN installation
```
cd /path/to/SABER_build/src/SABR/DQN_SABR_PREV/gym-dqnprev
pip install -e . 
```


## Commiting Changes to SABR Submodule

1. From the directory `src/SABER`, use git to add and commit the files:
```
cd /path/to/SABER_build/src/SABER
git ...
```

2. Leave the submodule and update the reference. The reference does not need to be updated at every single commit.
```
cd /path/to/SABER_build
git add src/SABER
git commit -m "update reference"
```

## Commiting Changes Hector Quadrotor Packages (subtrees)

Just pretend the subtree is not actually there and work as usual. :)


## Running Turtlebot for data collection (particle-filter SLAM)

Each command in a different terminal, from `SABER_build` directory:
1. `roscore`
2. `./play1.sh`
3. `rosrun sabr_pkg play2.py`
4. (After Terminal 3 is done) `rosrun sabr_pkg play3.py`


## Running Hector Quadrotor (VIO SLAM)

Each command in a different terminal, from `SABER_build` directory:
1. `roscore`
2. `./play_drone.sh`

If Gazebo hangs and you see something like this in the terminal:
```
AttributeError: 'NoneType' object has no attribute 'buff_size'
```
then you have encountered a race condition error that comes from launching too many nodes at once (or just the right number of nodes at any given time). Here is a way around it:
1. `roscore`
2. `rosrun gazebo_ros gazebo world_name:="src/SABER/worlds/world_drone"`
3. `roslaunch hector_quadrotor_gazebo/launch/spawn_quadrotor_with_kinect_SABR.launch`

## Training/Testing the DQN

1. `cd /path/to/SABER_build/src/SABR/DQN_SABR_PREV/`
2. for training: `python dqn_main.py`
3. for testing: `python DQN_test.py'

## Training the RNN
1. `cd /path/to/SABER_build/src/SABR/DQN_SABR_PREV/`
2. python rnn.py (note, the RNN code requires the data_collection directory including the collected datasets from SLAM. Collect data first, before running this code). 

## Running SABER (Turtlebot + Hector Quadrotor)
1. `roscore`
2. `./play_uav_ugv.sh`
3. `rosrun sabr_pkg SABER.py`
