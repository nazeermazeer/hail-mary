import commands2
from rev import SparkMax
import wpilib
import wpilib.drive


class UselessDrivetrain(commands2.SubsystemBase):
    def __init__(self, front_left_1, front_left_2, front_right_1, front_right_2, rear_left_1, rear_left_2, rear_right_1, rear_right_2):        
        self.front_left_1 = front_left_1
        self.front_left_2 = front_left_2
        self.front_right_1 = front_right_1
        self.front_right_2 = front_right_2
        self.rear_left_1 = rear_left_1
        self.rear_left_2 = rear_left_2
        self.rear_right_1 = rear_right_1
        self.rear_right_2 = rear_right_2

        self.front_left_1.setInverted(True)
        self.front_left_2.setInverted(True)
        self.front_right_1.setInverted(True)
        self.front_right_2.setInverted(True)
        self.rear_left_1.setInverted(True)
        self.rear_left_2.setInverted(True)
        self.rear_right_1.setInverted(True)
        self.rear_right_2.setInverted(True)
        
    def setSpeed(self, front_left_1, front_left_2, front_right_1, front_right_2, rear_left_1, rear_left_2, rear_right_1, rear_right_2):
        self.front_left_1.set(front_left_1)
        self.front_left_2.set(front_left_2)
        self.front_right_1.set(front_right_1)
        self.front_right_2.set(front_right_2)
        self.rear_left_1.set(rear_left_1)
        self.rear_left_2.set(rear_left_2)
        self.rear_right_1.set(rear_right_1)
        self.rear_right_2.set(rear_right_2)
        
    # def arcadeDrive(self, speed_perc, turn_angle_perc):
    #     self.speed = speed_perc * .5
    #     self.turn = turn_angle_perc * .5
    #     return self.drive.arcadeDrive(self.speed, self.turn)
