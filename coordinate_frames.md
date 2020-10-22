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

In the aerospace industry, $R_{AB}$ and $R_{BA}$ are called **transformation matrices**. Their transposes are called **rotation matrices**, which physically move vectors. Both appear in the aerospace and robotics literature.

If $R_{AB}$ is a transformation matrix about a single axis $(X, Y, Z)$ then it takes one of the following forms.

1. About X (roll):
   $$
    R_{AB} = R^x(\theta) = \begin{bmatrix}
              1 & 0              & 0 \\
              0 & \cos(\theta)   & \sin(\theta) \\
              0 & -\sin(\theta)  & \cos(\theta)
              \end{bmatrix}
   $$
2. About Y (pitch):
   $$
    R_{AB} = R^y(\theta) = \begin{bmatrix}
              \cos(\theta) & 0   & -\sin(\theta) \\
              0            & 1   & 0 \\
              \sin(\theta) & 0   & \cos(\theta)
              \end{bmatrix}
   $$  
3. About Z (yaw):
    $$
    R_{AB} = R^z(\theta) = \begin{bmatrix}
              \cos(\theta)  & \sin(\theta)   & 0 \\
              -\sin(\theta) & \cos(\theta)   & 0 \\
              0             & 0              & 1
              \end{bmatrix}
    $$


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

Then,
$$
T_{AB} = [10.0, 24.2, 34.3]^\top \\
R_{AB} = R^z(0.2) \cdot R^y(1.5) \cdot R^x(1.0)
$$
where the Euler angles are in radians. The rotation order is roll (about x-axis), then pitch (about y-axis), then yaw (about z-axis).
