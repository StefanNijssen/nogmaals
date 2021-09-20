from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

i = 0
x = 1

while True:
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        x += 1
        for i in range(1,x):
            robotArm.moveRight()
        robotArm.drop()
    else:
        break       
    for i in range(1,x):
        robotArm.moveLeft()

robotArm.wait()

