import pygame as pg
from random import randint

pg.init()
# TODO: import the images
#bg_img = pg.image.load("assets/")

# TODO: import pixel font
pixelify = "assets/PixelifySans-VariableFont_wght.ttf"
font = pg.font.Font(pixelify, 32)

WIDTH=512
HEIGHT=384
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("LandSavers")
#pg.display.set_icon()

while True:
    screen.fill((100, 100, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
    pg.display.update()