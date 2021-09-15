from RobotArm import RobotArm          
robotArm = RobotArm('exercise 7')
for i in range(1,6):
   for i in range(1,7):
      robotArm.moveRight()
      robotArm.grab()
      robotArm.moveLeft()
      robotArm.drop()
   robotArm.moveRight()
   robotArm.moveRight()
            # Jouw python instructies zet je vanaf hier:

            # Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.operate()
robotArm.moveLeft()
robotArm.moveRight()
robotArm.grab()
robotArm.drop()