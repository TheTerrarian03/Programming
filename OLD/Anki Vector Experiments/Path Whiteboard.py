import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Vector drives off charger")
        robot.behavior.drive_off_charger()

        print("Drive straight 65mm")
        robot.behavior.drive_straight(distance_mm(65), speed_mmps(50))

        print("Turns right 90")
        robot.behavior.turn_in_place(degrees(-90))

        print("Drive straight 85mm")
        robot.behavior.drive_straight(distance_mm(85), speed_mmps(50))

        print("Turns left 50")
        robot.behavior.turn_in_place(degrees(50))

        print("Drive straight 70mm")
        robot.behavior.drive_straight(distance_mm(70), speed_mmps(50))

        print("Turns left 40")
        robot.behavior.turn_in_place(degrees(40))

        print("Drive straight 90mm")
        robot.behavior.drive_straight(distance_mm(90), speed_mmps(50))

        print("Turns left 90")
        robot.behavior.turn_in_place(degrees(90))

        print("Drive straight 150mm")
        robot.behavior.drive_straight(distance_mm(150), speed_mmps(50))

        print("Turns right 90")
        robot.behavior.turn_in_place(degrees(-90))

        print("Drive straight 90mm")
        robot.behavior.drive_straight(distance_mm(90), speed_mmps(50))

        print("Turns left 45")
        robot.behavior.turn_in_place(degrees(45))

        print("Drive straight 40mm")
        robot.behavior.drive_straight(distance_mm(40), speed_mmps(50))


if __name__ == "__main__":
    main()