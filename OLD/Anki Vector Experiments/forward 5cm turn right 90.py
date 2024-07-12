import time
import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        # Tell Vector to drive forward at 50 mmps (millimeters per second),
        print("Set Vector's wheel motors...")
        robot.motors.set_wheel_motors(75, 75)

        # Wait for 1 second (the wheels will move while we wait)
        time.sleep(5)

        # Stop the motors
        robot.motors.set_wheel_motors(0, 0)

        print("Turn Vector in place 90")
        robot.behavior.turn_in_place(degrees(-90))

if __name__ == "__main__":
    main()