# Coordinate Frames

This file exists mainfly for Stephanie's sanity, and to make sure that she is getting the XIVO configuration file correct. It can be viewed in VS Code with the "Markdown All in One" plugin.

## Notation

Let $A$ and $B$ be two coordinate frames and $X$ be a point. Let $X_A$ and $X_B$ be the coordinates of $X$ resolved in frames $A$ and $B$, respectively. In Richard Murray's robotic manipulation textbook (and in XIVO):
$$
X_B = g_{BA}(X_A) = R_{BA}X_A + T_{BA} \\
X_A = g_{BA}^{-1}(X_B) = R_{BA}^{-1}(X_B - T_{BA})
$$
Which means...
$$
g_{AB} = g_{BA}^{-1} \\
R_{AB} = R_{BA}^{-1} \\
T_{AB} = - R_{BA}^{-1} \cdot T_{BA}
$$
In the equations above, $g_{AB}$ and $g_{BA}$ are elements of the $SE(3)$ group.


If frame $B$ is frame $A$ rotated by $\theta$ about one axis, then $R_{AB}$ takes one of the following forms:
1. About X (roll):
   $$
    R_{AB} = R^x(\theta) = \begin{bmatrix}
              1 & 0              &  0 \\
              0 & \cos(\theta)   & -\sin(\theta) \\
              0 & \sin(\theta)   & \cos(\theta)
              \end{bmatrix}
   $$
2. About Y (pitch):
   $$
    R_{AB} = R^y(\theta) = \begin{bmatrix}
              \cos(\theta)  & 0   & \sin(\theta) \\
              0             & 1   & 0 \\
              -\sin(\theta) & 0   & \cos(\theta)
              \end{bmatrix}
   $$  
3. About Z (yaw):
    $$
    R_{AB} = R^z(\theta) = \begin{bmatrix}
              \cos(\theta)  & -\sin(\theta)   & 0 \\
              \sin(\theta)  &  \cos(\theta)   & 0 \\
              0             & 0               & 1
              \end{bmatrix}
    $$

For Euler angles, doing matrix multiplication like this (roll, then pitch, then yaw):
$$
R_{AB} = R^z(\theta_z) \cdot R^y(\theta_y) \cdot R^x(\theta_x)
$$
is using **intrinsic** euler angles. **Extrinsic** euler angles means intrinsic euler angles applied backwards.


## In ROS configuration files
In ROS configuration files, coordiante transformations are defined at "joints" that hold two (usually?) rigid bodies together. The "joint" is located at the origin of the child link; the text below represents the "forward" movement of a frame coincident with the parent link's origin -> a frame coincident with the child link's origin.

(In URDF:)
```xml
<joint name="optical_joint" type="fixed">
  <parent link="linkA" />
  <child link="linkB" />
  <origin xyz="10.0 24.2 34.3" rpy="1.0 1.5 0.2" />
</joint>
```
The `rpy` field specifies extrinsic XYZ Euler angles.

Which then means...
$$
T_{AB} = [10.0, 24.2, 34.3]^\top \\
R_{AB} = \text{EulerXYZ}(1.0, 1.5, 0.2)
$$
where the Euler angles are in radians and the convention is extrinsic. The rotation order is roll (about x-axis), then pitch (about y-axis), then yaw (about z-axis). Robotics people pretty-much always use "XYZ" rotation order.

(I hope I'm reading [this tutorial](http://sdformat.org/tutorials?tut=specify_pose) correctly...)



## List of Coordinate Frames

(Joints written as "child from parent")

1. World Frame - fixed inertial frame that doesn't move. Z points up.
2. quadrotor `base_link`
3. quadrotor `base_stabilized` - only for low-level attitude stabilization -- IGNORE
4. quadrotor `base_footprint` - only for low-level control -- IGNORE
5. IMU Frame - same as `base_link`. in `hector_quadrotor_gazebo/urdf/quadrotor_sensors.gazebo.xacro`
6. `camera_link` from `base_link`: `<origin xyz="0.25 0.0 -0.05" rpy="0 ${M_PI/4} 0"/>`
7. `camera_depth_frame` from `camera_link`: `<origin xyz="0.0 -0.02 0.0" rpy="0 0 0" />`
8. `camera_depth_optical_frame` from `camera_depth_frame`: `<origin xyz="0 0 0" rpy="${-M_PI/2} 0.0 ${-M_PI/2}" />`
9. `camera_rgb_frame` from `camera_link`: `<origin xyz="0.0 -0.0125 0.0" rpy="0 0 0" />`
10. `camera_rgb_optical_frame` from `camera_rgb_frame`: `<origin xyz="0 0 0" rpy="${-M_PI/2} 0.0 ${-M_PI/2}" />`


Notes for XIVO:
- XIVO's "body" frame is `base_link`.
- XIVO's "spatial" frame is wherever `base_link` is initially is, will be a fixed offset from the World frame
- The "camera" frame is `camera_depth_optical_frame` (I think the Gazebo plugin is messed up).
- If we don't measure the direction of gravity, then `R_{sg} = W_g` can be zero rotation.
