import roboticstoolbox as rtb
from spatialmath import *
import numpy as np

robot = rtb.DHRobot(
    [rtb.RevoluteDH(alpha=np.pi/2, d=10),
     rtb.RevoluteDH(a=10, offset=np.pi/2),
     rtb.RevoluteDH(a=10),
     rtb.RevoluteDH(a=5)],
    name="Px_DH")
print(robot)
# 
# robot.plot(np.array([0, 0, .25, 0]))
robot.teach(np.array([0, 0, .25, 0]))
a = robot.fkine(np.array([0, 0, .25, 0]))
a.plot(color='red', label='2')
T = SE3(0.5, 0.0, 0.0) * SE3.RPY([0.1, 0.2, 0.3], order='xyz') * SE3.Rx(-90, unit='deg')
T.plot(color='red', label='2')
input()