import pygame as pg
from random import randint, choice

class Object:
    def __init__(self, speed):
        self.x = randint(0, 384)
        self.y = -128
        self.img = choice(("assets/seed.png", "assets/trash.png"))
        self.type = "seed" if "assets/seed.png" == self.img else "trash"
        self.img = pg.transform.scale(pg.image.load(self.img), (64, 64))
        self.speed = 1

    def drop_object(self, screen):
        self.y += self.speed
        screen.blit(self.img, (self.x, self.y))

    def check_collision(self, player):
        # check collison w/ player
        if self.y + 32 >= player.y and self.y <= player.y + 16:
            if self.x >= player.x + 16 and self.x <= player.x + 80:
                # check in main.py if type matches with player
                return True, self.type
        # check collision with ground
        elif self.y >= 320:
            return True, "ground"
        # otherwise, no collision
        return False, None