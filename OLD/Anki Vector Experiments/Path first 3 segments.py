import time
import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Vector drives off charger")
        robot.behavior.drive_off_charger() #This will do nothing, unless he is actually on charger

    print("Vector drives the first 60mm")
    robot.behavior.drive_straight(distance_mm(60), speed_mmps(50))

    print("Vector turns in place 45")
    robot.behavior.turn_in_place(degrees(45))

    print("Vector drives the next 130mm")
    robot.behavior.drive_straight(distance_mm(130), speed_mmps(50))

    print("Turn Vector in place 90")
    robot.behavior.turn_in_place(degrees(-90))

if __name__ == "__main__":
    main()