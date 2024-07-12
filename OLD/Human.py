import time


class Human:
    def __init__(self, first_name, last_name, char1, char2, char3):
        self.fname = first_name
        self.lname = last_name
        self.charlist = []
        self.charlist.append(char1)
        self.charlist.append(char2)
        self.charlist.append(char3)


time.sleep(1)

me = Human("Logan", "Meyers", "Annoying", "Funny", "Thoughtful")

print("[Creating Human]")

time.sleep(2)

print("[printing traits]")

time.sleep(1)

for variable in range(3):
    print(me.fname, me.lname, "is", me.charlist[variable])
    time.sleep(.25)

print(":D")
time.sleep(.25)
