   # Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
            # De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 4')
for i in range(1,3):
    robotArm.grab()
    for i in range(1,3):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(1,3):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(1,3):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()



    

            # Jouw python instructies zet je vanaf hier:

            # Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.operate()
robotArm.moveLeft()
robotArm.moveRight()
robotArm.grab()
robotArm.drop()