import pyxel

SCREEN_WIDTH = 64
SCREEN_HEIGHT = 64


class App:
    def __init__(self):
        pyxel.init(SCREEN_HEIGHT, SCREEN_WIDTH, title='Tamagotchi',
                   fps=30, quit_key=pyxel.KEY_SPACE,)
        pyxel.load("./13_tamagotchi.py.pyxres")
        self.life = 10
        self.level = 0
        self.food = 10
        self.drink = 10
        self.amusement = 0
        self.compteur_moral = 0
        self.morale = 0
        self.p_blue = 10
        self.p_red = 10
        self.death = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.death:
            self.update_player()
            self.check_death()
            self.compteur_moral += 1
            if self.compteur_moral > 300:
                self.morale += 1
                print(f" moral = {self.morale}")
                self.compteur_moral -= self.compteur_moral
        else:
            return (f" mort ? = {self.death}")

    def update_player(self):
        if self.life > 0:
            if pyxel.btnp(pyxel.KEY_Q):
                "manger"
                if self.food > 0:
                    self.food -= 1
                    print(f" nourriture = {self.food}")
            elif pyxel.btnp(pyxel.KEY_A):
                "boire"
                if self.drink > 0:
                    self.drink -= 1
                    print(f" eau = {self.drink}")
            elif pyxel.btnp(pyxel.KEY_W):
                "s'amuser"
                if self.drink > 0 < self.food:
                    if self.amusement < 5:
                        self.amusement += 1
                        self.drink -= 1
                        self.food -= 1
            elif pyxel.btnp(pyxel.KEY_S):
                "chercher alimentation"
                if self.food < 10:
                    self.food += 1
                if self.drink < 10:
                    self.drink += 1
                print(f"eau = {self.drink}, nourriture = {self.food}")
            elif pyxel.btnp(pyxel.KEY_E):
                "pillule bleu"
                if self.p_blue > 0:
                    self.p_blue -= 1
                    if self.amusement < 10:
                        self.amusement += 1
                    if self.food > 0:
                        self.food -= 1
                    if self.drink > 1:
                        self.drink -= 2
                if self.morale > 0:
                    self.morale -= 1
                print(f"pillule bleu = {self.p_blue}")
            elif pyxel.btnp(pyxel.KEY_R):
                "pillule rouge"
                if self.p_red > 0:
                    self.p_red -= 1
                    if self.amusement < 10:
                        self.amusement += 1
                    if self.food > 1:
                        self.food -= 2
                    if self.drink > 0:
                        self.drink -= 1
                    self.compteur_moral -= 300
                print(f"pillule rouge = {self.p_red}")

    def check_morale(self):
        if self.morale >= 1:
            pyxel.blt(56, 49, 0, 24, 64, 5, 5, 2)
        if self.morale >= 2:
            pyxel.blt(56, 54, 0, 24, 64, 5, 5, 2)
        if self.morale >= 3:
            pyxel.blt(56, 59, 0, 24, 64, 5, 5, 2)
        if self.morale >= 4:
            pyxel.blt(56, 49, 0, 16, 64, 5, 5, 2)
        if self.morale >= 5:
            pyxel.blt(56, 54, 0, 16, 64, 5, 5, 2)
        if self.morale >= 6:
            pyxel.blt(56, 59, 0, 16, 64, 5, 5, 2)

    """def check_amusement(self):
        if self.amusement >= 1:
            ..."""

    def check_death(self):
        if self.morale >= 7 or self.drink < 1 or self.food < 1:
            self.death = True
        else:
            self.death = False

    def death_event(self):
        pyxel.rect(0, 0, 64, 64, 0)
        pyxel.text(3, 32, "BOB EST MORT :( ",  pyxel.frame_count % 16)
        pyxel.stop()

    def draw(self):
        "dessine le jeu"
        y = 49
        if not self.death:
            pyxel.mouse(True)
            pyxel.cls(0)
            pyxel.rect(0, 0, 64, 47, 6)
            pyxel.blt(10, 48, 0, 0, 64, 8, 8, 2)  # water icon
            pyxel.text(2, 50, str(self.drink), 12)  # water value
            pyxel.blt(10, 56, 0, 8, 64, 8, 8, 2)  # food icon
            pyxel.text(2, 58, str(self.food), 9)  # food value
            pyxel.blt(36, 48, 0, 8, 80, 8, 8, 2)  # p_red icon
            pyxel.text(28, 50, str(self.p_red), 7)  # p_red value
            pyxel.blt(36, 56, 0, 0, 80, 8, 8, 2)  # p_blue icon
            pyxel.text(28, 58, str(self.p_blue), 7)  # p_blue value
            if self.morale >= 0:
                for _ in range(3):
                    pyxel.blt(56, y, 0, 24, 72, 5, 5, 2)  # moral_bubble
                    y += 5
            for x in range(0, 56, 24):  # environnement
                pyxel.blt(x, 39, 0, 0, 96, 8, 8)
                pyxel.blt(x+8, 39, 0, 16, 96, 8, 8)
                pyxel.blt(x+16, 39, 0, 32, 96, 8, 8)
                pyxel.blt(x+24, 39, 0, 32, 96, 8, 8)
            pyxel.blt(0, 31, 0, 0, 88, 8, 8, 2)
            pyxel.blt(8, 31, 0, 16, 88, 8, 8, 2)
            pyxel.blt(16, 31, 0, 0, 88, 8, 8, 2)
            pyxel.blt(24, 31, 0, 32, 88, 8, 8, 2)
            pyxel.blt(32, 31, 0, 16, 88, 8, 8, 2)
            pyxel.blt(40, 31, 0, 0, 88, 8, 8, 2)
            pyxel.blt(48, 31, 0, 32, 88, 8, 8, 2)
            pyxel.blt(56, 31, 0, 0, 88, 8, 8, 2)
            pyxel.blt(24, 24, 0, 0, 112, 8, 8, 2)
            pyxel.blt(32, 24, 0, 8, 112, 8, 8, 2)
            pyxel.blt(40, 24, 0, 16, 112, 8, 8, 2)
            pyxel.blt(24, 32, 0, 0, 120, 8, 8, 2)
            pyxel.blt(32, 32, 0, 8, 120, 8, 8, 2)
            pyxel.blt(40, 32, 0, 16, 120, 8, 8, 2)
            pyxel.blt(24, 16, 0, 0, 104, 8, 8, 2)
            pyxel.blt(32, 16, 0, 8, 104, 8, 8, 2)
            pyxel.blt(40, 16, 0, 16, 104, 8, 8, 2)
            pyxel.blt(0, 0, 0, 40, 104, 8, 8, 2)
            pyxel.blt(8, 0, 0, 48, 104, 8, 8, 2)
            pyxel.blt(0, 8, 0, 40, 112, 8, 8, 2)
            pyxel.blt(8, 8, 0, 48, 112, 8, 8, 2)
            pyxel.blt(24, 4, 0, 8, 128, 8, 8, 2)
            pyxel.blt(38, 8, 0, 16, 136, 8, 8, 2)
            pyxel.blt(46, 8, 0, 24, 136, 8, 8, 2)
            self.check_morale()
            pyxel.line(0, 47, 63, 47, 7)
        else:
            self.death_event()

        # pyxel.blt(10, 16, 0, 8, 72, 8, 8, 2)  # amusement icon
        # pyxel.text(2, 18, str(self.amusement), 11)  # amusement value


App()
