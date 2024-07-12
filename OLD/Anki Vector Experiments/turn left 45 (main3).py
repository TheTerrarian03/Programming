import time
import anki_vector
from anki_vector.util import degrees


def main3():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        print("Turn Vector in place 45")
        robot.behavior.turn_in_place(degrees(45))

main3()