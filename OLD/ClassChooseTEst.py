nnf = 0
name_list1 = []
name_list2 = []


class Something:
    def __init__(self, name):
        self.name = name
        self.active = True

    def draw(self):
        print("+-" + len(self.name) + "-+")
        print("+-" + self.name + "-+")
        print("+-" + len(self.name) + "-+")

    def become_inactive(self):
        self.active = False


def create():
    input1 = input("Choose a name: ")
    name_list1.append(input1)
    name_list2.append(input1)
    name_list2[nnf] = Something(name_list1[nnf])


create()
