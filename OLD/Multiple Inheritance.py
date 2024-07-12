class Mario():
    def move(self):
        print("I am moving!")


class Shroom():
    def eat_shroom(self):
        print("Now I am big!")


class Flower():
    def shoot_fire(self):
        print("SHOOTING FIRE!!!!")


class BigMario(Mario, Shroom, Flower):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
bm.shoot_fire()