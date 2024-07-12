import time
import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        # Tell Vector to drive forward at 50 mmps (millimeters per second),
        print("Set Vector's wheel motors...")
        robot.motors.set_wheel_motors(50, 50)

        # Wait for 10 seconds (the wheels will move while we wait)
        time.sleep(10)

        # Stop the motors, which unlocks the tracks
        robot.motors.set_wheel_motors(0, 0)


if __name__ == "__main__":
    main()