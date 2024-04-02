// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import edu.wpi.first.wpilibj.Threads;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj2.command.CommandScheduler;
import frc.robot.Elevator.ElevatorCommands;
import frc.robot.Elevator.ElevatorSubSys;
import frc.robot.Pilot.PilotGamepad;

/**
 * The VM is configured to automatically run this class, and to call the functions corresponding to
 * each mode, as described in the TimedRobot documentation. If you change the name of this class or
 * the package after creating this project, you must also update the build.gradle file in the
 * project.
 */
public class Robot extends TimedRobot {
  public static ElevatorSubSys elev;
  public static PilotGamepad pilotGamepad;
  public static RobotTelemetry telem;

  /**
   * This function is run when the robot is first started up and should be used for any
   * initialization code.
   */
  @Override
  public void robotInit() {
    elev = new ElevatorSubSys();
    pilotGamepad = new PilotGamepad();
    telem = new RobotTelemetry();

    ElevatorCommands.setupDefaultCommand();
  }

  @Override
  public void robotPeriodic() {
    // Ensures that the main thread is the highest priority thread
    Threads.setCurrentThreadPriority(true, 99);
    CommandScheduler.getInstance().run();       // Make sure scheduled commands get run
    Threads.setCurrentThreadPriority(true, 10); // Set the main thread back to normal priority
  }

  @Override
  public void autonomousInit() {}

  @Override
  public void autonomousPeriodic() {}

  @Override
  public void teleopInit() {
    resetCommandsAndButtons();
  }

  @Override
  public void teleopPeriodic() {}

  @Override
  public void disabledInit() {
    resetCommandsAndButtons();
  }

  @Override
  public void disabledPeriodic() {}

  @Override
  public void testInit() {}

  @Override
  public void testPeriodic() {}

  @Override
  public void simulationInit() {}

  @Override
  public void simulationPeriodic() {}

  public void resetCommandsAndButtons() {
    pilotGamepad.resetConfig();
  }
}
