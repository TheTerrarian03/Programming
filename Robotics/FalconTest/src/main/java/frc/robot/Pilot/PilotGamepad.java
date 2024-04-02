package frc.robot.Pilot;

import frc.lib.gamepads.Gamepad;
import frc.robot.Elevator.ElevatorCommands;

public class PilotGamepad extends Gamepad {
    public PilotGamepad() {
        super("Pilot", 0);
    }

    // ----- `Gamepad` Lib Required Methods for Button Assignment -----
    public void setupTeleopButtons() {
        this.gamepad.xButton.onTrue(ElevatorCommands.elevToPos(-10));
        this.gamepad.aButton.onTrue(ElevatorCommands.elevToPos(0));
        this.gamepad.bButton.onTrue(ElevatorCommands.elevToPos(10));
        
        this.gamepad.startButton.onTrue(ElevatorCommands.elevResetPosition());
    }

    public void setupDisabledButtons() {}

    public void setupTestButtons() {}

    // ----- Getter Methods for Input -----

    public double getX() {
        return this.gamepad.leftStick.getX();
    }

    public double getY() {
        return this.gamepad.leftStick.getY();
    }
}
