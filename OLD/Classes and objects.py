class Enemy:
    life = 3

    def attack(self):
        print("OUCH!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print("Enemy has " + (str(self.life)) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.checkLife()
enemy2.attack()
enemy2.checkLife()