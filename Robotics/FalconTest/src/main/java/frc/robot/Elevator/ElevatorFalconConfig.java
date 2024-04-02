package frc.robot.Elevator;

import com.ctre.phoenix6.configs.CurrentLimitsConfigs;
import com.ctre.phoenix6.configs.FeedbackConfigs;
import com.ctre.phoenix6.configs.MotionMagicConfigs;
import com.ctre.phoenix6.configs.Slot0Configs;
import com.ctre.phoenix6.configs.TalonFXConfiguration;

public class ElevatorFalconConfig {
    // constant values for configuration
    private static final double mmCruiseVelocity = 5;   // 5 rpm cruise
    private static final double mmAcceleration   = 10;  // ~0.5 seconds to max vel.
    private static final double mmJerk           = 50;  // ~0.2 seconds to max accel.

    private static final double kP = 1.0;   // (P)roportional value
    private static final double kI = 0.0;   // (I)ntegral Value
    private static final double kD = 0.0;   // (D)erivative Value
    private static final double kV = 0.12;  // Volts/100 (?)
    private static final double kS = 0.05;  // (S)tiction Value: 

    private static final boolean enableCurrentLimitting = true;
    private static final double suppCurrent = 40;      // Max Amps allowed in Supply
    private static final double suppTimeThresh = 0.1;  // How long to allow unlimited Supply (s)

    public static TalonFXConfiguration getConfig() {
        // Initialize config object
        TalonFXConfiguration config = new TalonFXConfiguration();

        // Configure Motion Magic Values
        MotionMagicConfigs mm = config.MotionMagic;
        mm.MotionMagicCruiseVelocity = mmCruiseVelocity;
        mm.MotionMagicAcceleration = mmAcceleration;
        mm.MotionMagicJerk = mmJerk;

        // Configure PID Slot0 Values (PIDVS)
        Slot0Configs slot0Configs = config.Slot0;
        slot0Configs.kP = kP;
        slot0Configs.kI = kI;
        slot0Configs.kD = kD;
        slot0Configs.kV = kV;
        slot0Configs.kS = kS;
        
        // Feedback stuff
        // FeedbackConfigs fdb = config.Feedback;
        // fdb.

        // Configure Current Limits
        CurrentLimitsConfigs currentLimits = config.CurrentLimits;
        currentLimits.SupplyCurrentLimitEnable = enableCurrentLimitting;
        currentLimits.SupplyCurrentLimit = suppCurrent;
        currentLimits.SupplyTimeThreshold = suppTimeThresh;

        // finally return an object that will represent the configs we would like to 
        return config;
    }
}
