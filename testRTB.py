import roboticstoolbox as rtb
#from roboticstoolbox.backends.Swift import Swift  # instantiate 3D browser-based visualizer
from spatialmath import SE3
from swift.SwiftRoute import SwiftServer, SwiftSocket, start_servers
from swift.SwiftElement import SwiftElement, Slider, Select, \
    Checkbox, Radio, Button, Label
from swift.Swift import Swift

robot = rtb.models.URDF.Panda()  # load URDF version of the Panda
print(robot)    # display the model
T = SE3(0.7, 0.2, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = robot.ikine_LM(T)         # solve IK
# print(sol)
q_pickup = sol.q
qt = rtb.jtraj(robot.qz, q_pickup, 50)
# robot.plot(qt.q)

#print(robot.fkine(q_pickup))    # FK shows that desired end-effector pose was achieved
backend = Swift()
backend.launch()            # activate it
robot.q = q_pickup
backend.add(robot)          # add robot to the 3D scene

#for qk in qt.q:             # for each joint configuration on trajectory
#      robot.q = qk          # update the robot state
#      backend.step()        # update visualization
