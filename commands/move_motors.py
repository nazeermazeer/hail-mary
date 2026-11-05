import commands2


class MoveMotors(commands2.SequentialCommandGroup):
    def __init__(self, drivetrain, front_left_1, front_left_2, front_right_1, front_right_2, rear_left_1, rear_left_2, rear_right_1, rear_right_2):
        super().__init__()
        motors = [front_left_1, front_left_2, front_right_1, front_right_2, rear_left_1, rear_left_2, rear_right_1, rear_right_2]
        
        self.addRequirements(drivetrain)
        for motor in motors:
            self.addCommands(
                commands2.cmd.InstantCommand(lambda motor=motor: motor.set(0.5)),
                commands2.WaitCommand(3.2),
                commands2.cmd.InstantCommand(lambda motor=motor: motor.set(0.0)),
            )
