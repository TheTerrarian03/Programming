package frc.robot;

import edu.wpi.first.wpilibj.DriverStation;
import edu.wpi.first.wpilibj.Timer;
import frc.lib.telemetry.Alert;
import frc.lib.telemetry.Alert.AlertType;
import frc.lib.telemetry.TelemetrySubsystem;
import frc.lib.util.Network;
import frc.lib.util.Util;
import frc.robot.pilot.PilotGamepadTelemetry;
import frc.robot.swerve.SwerveTelemetry;

import java.util.Map;

public class RobotTelemetry extends TelemetrySubsystem {
    private static boolean disablePrints = false;

    // Additional Shuffleboard Tabs
    
    //public static IntakeTelemetry          m_IntakeTelemetry;
    public static SwerveTelemetry          m_SwerveTelemetry;
    public static PilotGamepadTelemetry    m_PilotTelemetry;
    //public static OperatorGamepadTelemetry m_OperatorTelemetry;

    // Alerts
    private static Alert batteryAlert = new Alert("Low Battery < 12v", AlertType.WARNING);
    private static Alert FMSConnectedAlert = new Alert("FMS Connected", AlertType.INFO);

    private String IPaddress = "UNKOWN";

    // ------------- Constructor --------------
    public RobotTelemetry() {
        // Call Super constuctor first - 
        super("Robot");     // Set tab name to Robot

        layoutRobotTelemtryTab();   // Fill This Tab with data

        // Setup the rest of the Shuffleboard Tabs
       
        //m_IntakeTelemetry =         new IntakeTelemetry(Robot.intake);
        m_SwerveTelemetry =         new SwerveTelemetry(Robot.swerve);
        m_PilotTelemetry =          new PilotGamepadTelemetry(Robot.pilotGamepad); ;
        //m_OperatorTelemetry =       new OperatorGamepadTelemetry(Robot.operatorGamepad); ;
    }

    @Override
    public void periodic() {
        checkFMSalert();
        checkBatteryWhenDisabledalert();
    }

    // public static void createTab(String name) {
    //     Shuffleboard.getTab(name);
    // }

    public void layoutRobotTelemtryTab(){
        



        tab.addNumber("Match Time", () -> Timer.getMatchTime())
                .withPosition(10, 0)
                .withSize(2, 2)
                .withWidget("Simple Dial")
                .withProperties(Map.of("Min", 0, "Max", 135));

        tab.add("Speed Selection",    Robot.pilotGamepad.speedChooser)  .withPosition(10, 3).withSize(3, 1);
        // tab.add("Aliance Selection",  Auto.allianceChooser)             .withPosition(10, 5).withSize(3, 1);

        //tab.add("Test Selection", Auto.testChooser)             .withPosition(20, 8).withSize(3, 2);

        // tab.addBoolean("Connected?", () -> flash())
        //         .withPosition(2, 0)
        //         .withSize(1, 1)
        //         .withProperties(
        //                 Map.of("Color when true", "#300068", "Color when false", "#FFFFFF"));

        // tab.add("Alerts", SmartDashboard.getData("Alerts")).withPosition(4, 0).withSize(2, 2);
        // tab.add("MAC Address", Robot.MAC).withPosition(4, 2).withSize(2, 1);
        // tab.addString("IP Address", () -> getIP()).withPosition(4, 3).withSize(2, 1);
    }

    public String getIP() {
        if (IPaddress == "UNKOWN") {
            IPaddress = Network.getIPaddress();
        }
        return IPaddress;
    }

    public void checkFMSalert() {
        FMSConnectedAlert.set(DriverStation.isFMSAttached());
    }

    public void checkBatteryWhenDisabledalert() {
        batteryAlert.set(DriverStation.isDisabled() && Util.checkBattery(12.0));
    }

    public boolean flash() {
        return (int) Timer.getFPGATimestamp() % 2 == 0;
    }

    public static void print(String output) {
        if (!disablePrints) {
            System.out.println(output);
        }
    }
}
