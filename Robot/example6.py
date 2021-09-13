   # Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
            # De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 6')
for i in range(1,8):
    robotArm.moveRight()
for i in range(1,9):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()





    

            # Jouw python instructies zet je vanaf hier:

            # Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.operate()
robotArm.moveLeft()
robotArm.moveRight()
robotArm.grab()
robotArm.drop()