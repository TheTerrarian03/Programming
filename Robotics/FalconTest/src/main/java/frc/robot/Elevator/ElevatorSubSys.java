package frc.robot.Elevator;

import com.ctre.phoenix6.controls.MotionMagicVoltage;
import com.ctre.phoenix6.hardware.TalonFX;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class ElevatorSubSys extends SubsystemBase {
    public final TalonFX m_motor;
    private MotionMagicVoltage mmCtrlr;

    private double targetPosition = 0;

    // by speed:
    // private DutyCycleOut targetSpeed = new DutyCycleOut(0);

    // ----- Constructor -----
    public ElevatorSubSys() {
        m_motor = new TalonFX(16);
        mmCtrlr = new MotionMagicVoltage(0);

        configureMotors();
    }

    // ----- Subsystem Periodic -----
    @Override
    public void periodic() {
        // tell motor to run my MotionMagic, and go to target position
        m_motor.setControl(mmCtrlr.withPosition(targetPosition).withSlot(0));
    }

    // ----- Motor Setup and Resetting -----
    public void configureMotors() {
        m_motor.getConfigurator().apply(ElevatorFalconConfig.getConfig());
    }

    public void resetPosition() {
        m_motor.setPosition(0);
    }

    // ----- Setters for Motor and Position Control -----

    public void stopMotor() {
        m_motor.stopMotor();
    }

    public void setTargetPosition(double newPosition) {
        targetPosition = newPosition;
    }

    public void setTargetPositionByAdjust(double adjustByAmnt) {
        targetPosition += adjustByAmnt;
    }

    // ----- Getters for Motor Position and Targets-----
    public double getMotorSpeed() {
        return m_motor.get();
    }

    public double getTargetPos() {
        return targetPosition;
    }

    public String getCurrentPos() {
        return m_motor.getPosition().toString();
    }
}
