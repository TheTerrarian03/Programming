import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Say 'Hello World'...")
        robot.behavior.say_text("Hello World")


main()