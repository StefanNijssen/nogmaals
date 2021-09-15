from RobotArm import RobotArm;robotArm = RobotArm('exercise 10')
for i in range(1,6):
    robotArm.grab()
    for i in range(1,6):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(1,5):
        robotArm.moveLeft()




robotArm.operate()
robotArm.grab()
robotArm.moveRight()
robotArm.moveLeft()

robotArm.drop()