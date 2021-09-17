from RobotArm import RobotArm;robotArm = RobotArm('exercise 12')
i = 0
x = 0
for i in range(1,10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        robotArm.grab()
        x = x + 1
        for i in range(1,15):
            robotArm.moveRight()
        robotArm.drop()
       
        for i in range(1,10-x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        x = x + 1
    robotArm.moveRight()


robotArm.operate()
robotArm.grab()
robotArm.moveRight()
robotArm.moveLeft()
robotArm.scan()
robotArm.drop()