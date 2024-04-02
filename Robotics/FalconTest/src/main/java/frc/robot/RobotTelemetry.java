package frc.robot;

import frc.lib.telemetry.TelemetrySubsystem;

public class RobotTelemetry extends TelemetrySubsystem {
    public RobotTelemetry() {
        super("Robot");

        tab.addDouble("Pilot X", () -> Robot.pilotGamepad.getX());
        tab.addDouble("Pilot Y", () -> Robot.pilotGamepad.getY());
        tab.addDouble("Elevator Speed", () -> Robot.elev.getMotorSpeed());
        tab.addDouble("Elevator Target Pos", () -> Robot.elev.getTargetPos());
        tab.addString("Elevator Current Pos", () -> Robot.elev.getCurrentPos());
    }
}
