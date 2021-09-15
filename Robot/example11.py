from RobotArm import RobotArm;robotArm = RobotArm('exercise 11')
for i in range(1,10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop()
    robotArm.moveRight()




robotArm.operate()
robotArm.grab()
robotArm.moveRight()
robotArm.moveLeft()
robotArm.scan()
robotArm.drop()