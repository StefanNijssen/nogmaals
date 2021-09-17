from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

i = 0
x = 1
robotArm.grab()
color = robotArm.scan()
color
for i in range(1,10):
    if color == "red" or "white" or "green" or "blue" or "yellow":
        robotArm.grab()
        x += 1
        for i in range(1,x):
            robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.wait()
    for i in range(1,x):
        robotArm.moveLeft()





robotArm.operate()
robotArm.grab()
robotArm.moveRight()
robotArm.moveLeft()
robotArm.scan()
robotArm.drop()