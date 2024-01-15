package frc.robot;

import edu.wpi.first.wpilibj.Threads;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj2.command.CommandScheduler;
// import frc.lib.util.Network;
import frc.robot.pilot.PilotGamepad;
import frc.robot.pilot.commands.PilotGamepadCmds;
 import frc.robot.swerve.Swerve;
 import frc.robot.swerve.commands.SwerveCmds;

// ------------------- Constructor -----------------
public class Robot extends TimedRobot {
    //public static RobotConfig config;
    public static Swerve swerve;
    public static PilotGamepad pilotGamepad;
    public static RobotTelemetry telemetry;
    public static String MAC = "";

    // -----------------  Robot General Methods ------------------
    @Override
    public void robotInit() {
        Timer.delay( 2.0 );         // Delay for 2 seconds for robot to come fully up
        //MAC = Network.getMACaddress();
       
        intializeSubsystems();
    }

    @Override
    public void robotPeriodic() {
        // Ensures that the main thread is the highest priority thread
        Threads.setCurrentThreadPriority(true, 99);
        CommandScheduler.getInstance().run();       // Make sure scheduled commands get run
        Threads.setCurrentThreadPriority(true, 10); // Set the main thread back to normal priority
    }

    private void intializeSubsystems() {
         // Initialize Subsystems
         swerve = new Swerve();
         pilotGamepad = new PilotGamepad();
         telemetry = new RobotTelemetry();  

     // Set Default Commands, this method should exist for each subsystem that has commands
         SwerveCmds.setupDefaultCommand();
         PilotGamepadCmds.setupDefaultCommand();
     }

    
    // -----------------  Robot Disabled Mode Methods ------------------
    @Override
    public void disabledInit() {
        resetCommandsAndButtons();
    }

    @Override
    public void disabledPeriodic()  { }

    @Override
    public void disabledExit()  { }


    // -----------------  Autonomous Mode Methods ------------------
    @Override
    public void autonomousInit() {
        System.out.println("Starting Auto Init");
        resetCommandsAndButtons();
        swerve.setLastAngleToCurrentAngle();
    }

    @Override
    public void autonomousPeriodic() {}

    @Override
    public void autonomousExit() {}


    // -----------------  TeleOp Mode Methods ------------------
    @Override
    public void teleopInit() {
        resetCommandsAndButtons();
        pilotGamepad.setMaxSpeeds(pilotGamepad.getSelectedSpeed());
        swerve.resetFalconAngles();     // Set falcon angle motors to absolute encoder
    }

    @Override
    public void teleopPeriodic() {}

    @Override
    public void teleopExit() {}

    // -----------------  Test Mode Methods ------------------
    @Override
    public void testInit() {
        resetCommandsAndButtons();
    }

    @Override
    public void testPeriodic() {}


    // -----------------  Simulation Mode Methods ------------------
    public void simulationInit() {}

    public void simulationPeriodic() {}

    // ------------------------  Misc Methods ---------------------
    public static void resetCommandsAndButtons() {
        CommandScheduler.getInstance().cancelAll(); // Disable any currently running commands
        CommandScheduler.getInstance().getActiveButtonLoop().clear();
        pilotGamepad.resetConfig();     // Reset Config for all gamepads and other button bindings
    }
}
