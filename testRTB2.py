import roboticstoolbox as rtb
from spatialmath import SE3

robot = rtb.DHRobot([rtb.RevoluteDH(a=1),rtb.RevoluteDH(a=1)],name="2R")
print(robot)
robot.plot([0.75,0.26])
input()

