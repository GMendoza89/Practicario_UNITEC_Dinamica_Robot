import coppeliaRobots as cp
import time         

myRobot = cp.simple3GDM()

ID = cp.simConnect(19999)

myRobot.robotInit(ID)
print(myRobot.getDummyPosition())

while True:
    for i in range(-45,45):
        phi_Base = i
        myRobot.moveBase(phi_Base)
        print(phi_Base)
        time.sleep(0.01)
    for i in range(45,-45,-1):
        phi_Base = i
        myRobot.moveBase(phi_Base)
        print(phi_Base)
        time.sleep(0.01)
        