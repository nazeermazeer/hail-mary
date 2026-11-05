import commands2
import rev
import wpilib
import wpimath

from commands.arcade_drive import ArcadeDrive
from commands.move_motors import MoveMotors
from commands.tank_drive import TankDrive
from subsystems.drivetrain import UselessDrivetrain
from constants import constants


class WestCoastRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        super().__init__()

        self.front_left_1 = rev.SparkMax(58, rev.SparkLowLevel.MotorType.kBrushless)
        self.front_left_2 = rev.SparkMax(57, rev.SparkLowLevel.MotorType.kBrushless)
        self.front_right_1 = rev.SparkMax(60, rev.SparkLowLevel.MotorType.kBrushless)
        self.front_right_2 = rev.SparkMax(59, rev.SparkLowLevel.MotorType.kBrushless)
        self.rear_left_1 = rev.SparkMax(54, rev.SparkLowLevel.MotorType.kBrushless)
        self.rear_left_2 = rev.SparkMax(53, rev.SparkLowLevel.MotorType.kBrushless)
        self.rear_right_1 = rev.SparkMax(51, rev.SparkLowLevel.MotorType.kBrushless)
        self.rear_right_2 = rev.SparkMax(50, rev.SparkLowLevel.MotorType.kBrushless)

        self.drivetrain = UselessDrivetrain(self.front_left_1, self.front_left_2, self.front_right_1, self.front_right_2, self.rear_left_1, self.rear_left_2, self.rear_right_1, self.rear_right_2)

        # self.driver_controller = commands2.button.CommandXboxController(0)


    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        command = MoveMotors(self.drivetrain, self.front_left_1, self.front_left_2, self.front_right_1, self.front_right_2, self.rear_left_1, self.rear_left_2, self.rear_right_1, self.rear_right_2)
        self.drivetrain.setDefaultCommand(
            command
        )

    def teleopPeriodic(self):
        pass
        # print(f"Current status of A button: {self.driver_controller.a()}")

    def testInit(self):
        # self.driver_controller.setRumble(GenericHID.RumbleType.kLeftRumble, 1.0)
        pass

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(WestCoastRobot)
