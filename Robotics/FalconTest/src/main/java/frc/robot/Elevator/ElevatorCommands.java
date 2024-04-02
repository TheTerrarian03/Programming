package frc.robot.Elevator;

import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.InstantCommand;
import edu.wpi.first.wpilibj2.command.RunCommand;
import frc.robot.Robot;

public class ElevatorCommands {
    public static void setupDefaultCommand() {
        // Robot.elev.setDefaultCommand(elevByJoystickCmd());
    }
    
    public static Command elevByJoystickCmd() {
        return new RunCommand(() -> Robot.elev.setTargetPositionByAdjust(Robot.pilotGamepad.getY()), Robot.elev);
    }

    public static Command elevToPos(double newPosition) {
        return new InstantCommand(() -> Robot.elev.setTargetPosition(newPosition), Robot.elev);
    }

    public static Command elevResetPosition() {
        return new InstantCommand(() -> Robot.elev.resetPosition(), Robot.elev);
    }
}
