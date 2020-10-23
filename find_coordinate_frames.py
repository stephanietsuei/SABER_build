"""This is a quick little script that computes the values of Wbc and Tbc for
the hector quadcoptor so that it can be input to XIVO's configuration file."""

import numpy as np
from scipy.spatial.transform import Rotation


R_BaseLink_CameraLink = Rotation.from_euler('XYZ', [0, np.pi/4, 0])
T_BaseLink_CameraLink = np.array([0.25, 0, -0.05])

R_CameraLink_DepthFrame = Rotation.identity()
T_CameraLink_DepthFrame = np.array([0, -0.02, 0])

R_DepthFrame_DepthOpticalFrame = \
  Rotation.from_euler('XYZ', [-np.pi/2, 0, -np.pi/2])
T_DepthFrame_DepthOpticalFrame = np.zeros(3)

R_CameraLink_RGBFrame = Rotation.identity()
T_CameraLink_RGBFrame = np.array([0, -0.0125, 0])

R_RGBFrame_RGBOpticalFrame = \
  Rotation.from_euler('XYZ', [-np.pi/2, 0, -np.pi/2])
T_RGBFrame_RGBOpticalFrame = np.zeros(3)


R_bc = R_BaseLink_CameraLink * R_CameraLink_DepthFrame \
  * R_DepthFrame_DepthOpticalFrame
T_bc = \
  (R_BaseLink_CameraLink * R_CameraLink_DepthFrame).apply(T_DepthFrame_DepthOpticalFrame) + \
  R_BaseLink_CameraLink.apply(T_CameraLink_DepthFrame) + \
  T_BaseLink_CameraLink


R_bc2 = R_BaseLink_CameraLink * R_CameraLink_RGBFrame \
  * R_RGBFrame_RGBOpticalFrame
T_bc2 = \
  (R_BaseLink_CameraLink * R_CameraLink_RGBFrame).apply(T_RGBFrame_RGBOpticalFrame) + \
  R_BaseLink_CameraLink.apply(T_CameraLink_RGBFrame) + \
  T_BaseLink_CameraLink


print("Result:")
print("Wbc: {}".format(R_bc.as_rotvec()))
print("Tbc: {}".format(T_bc))
