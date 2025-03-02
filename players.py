import pygame as pg

class Player1:
    def __init__(self):
        self.type = "planter"
        self.idle_img = pg.transform.scale(pg.image.load('assets/player_1/idle.png'), (96, 144))
        self.catch_img = pg.transform.scale(pg.image.load('assets/player_1/caught.png'), (96, 144))
        self.wrong_img = pg.transform.scale(pg.image.load('assets/player_1/wrong.png'), (96, 144))
        self.x = 160
        self.y = 240
        self.speed = 1.5

class Player2:
     def __init__(self):
        self.type = "cleaner"
        self.idle_img = pg.transform.scale(pg.image.load('assets/player_2/idle.png'), (96, 144))
        self.catch_img = pg.transform.scale(pg.image.load('assets/player_2/caught.png'), (96, 144))
        self.wrong_img = pg.transform.scale(pg.image.load('assets/player_2/wrong.png'), (96, 144))
        self.x = 256
        self.y = 240
        self.speed = 1.5
