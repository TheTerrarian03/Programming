import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        print("Say 'My name is Vector'...")
        robot.behavior.say_text("My name is Vector")

        print("Drive Vector straight...")
        robot.behavior.drive_straight(distance_mm(2000), speed_mmps(100))

        print("Turn Vector in place...")
        robot.behavior.turn_in_place(degrees(180))

        print("Drive Vector straight...")
        robot.behavior.drive_straight(distance_mm(2000), speed_mmps(100))

if __name__ == "__main__":
    main()