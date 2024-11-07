import coppeliaRobots as cp

myRobot = cp.plannarRobot()

ID = cp.simConnect(19999)

myRobot.robotInit(ID)
print(myRobot.getDummyPosition())

while True:
    for i in range(-90,90):
            myRobot.moveRobot(i,i,i)
            print(myRobot.getDummyPosition())
    for i in range(90,-90,-1):
            myRobot.moveRobot(i,i,i)
            print(myRobot.getDummyPosition())