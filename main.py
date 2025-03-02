import pygame as pg
from random import randint, choice
from objects import Object
from players import Player1, Player2

pg.init()
# TODO: import the images
bg_img = pg.image.load("assets/bg.png")
heart_img = pg.transform.scale(pg.image.load("assets/heart.png"), (32, 32))

# TODO: import pixel font
pixelify = "assets/PixelifySans-VariableFont_wght.ttf"
title_font = pg.font.Font(pixelify, 48)
font = pg.font.Font(pixelify, 24)

# constants
WIDTH=512
HEIGHT=384
DARK_BLUE = (31, 71, 120)

# initialize screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("LandSavers")
#pg.display.set_icon()

# keep track of scores
score = 0
lives = 3

# create title text
title_text = title_font.render("LandSavers", True, DARK_BLUE)
title_rect = title_text.get_rect()

p1_text = font.render("Player 1: Planter, use A/D to move", True, DARK_BLUE)
p1_rect = p1_text.get_rect()
p2_text = font.render("Player 2: Cleaner, use LEFT/RIGHTto move", True, DARK_BLUE)
p2_rect = p2_text.get_rect()

inst_text = font.render("Press SPACE to start", True, DARK_BLUE)
inst_rect = inst_text.get_rect()

is_title_screen = True
is_story_line = False

while is_title_screen:
    screen.blit(bg_img, (0, 0))
    screen.blit(title_text, (WIDTH/2 - title_rect.width/2, HEIGHT/2 - title_rect.height/2 - 56))
    screen.blit(p1_text, (WIDTH/2 - p1_rect.width/2, HEIGHT/2 - p1_rect.height/2 - 20))
    screen.blit(p2_text, (WIDTH/2 - p2_rect.width/2, HEIGHT/2 - p2_rect.height/2+8))
    screen.blit(inst_text, (WIDTH/2 - inst_rect.width/2, HEIGHT/2 - inst_rect.height/2 + 65))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        is_title_screen = False
        is_story_line = True
        break
    pg.display.update()

is_game_instructions = False
story_text = ["The world is ending!", "You and your friend must restore the", "ecological balance to save the world!","The planter must catch seeds,","and the cleaner must catch trash.","Press Space to continue"]

while is_story_line:
    screen.blit(bg_img, (0, 0))

    for line in range(len(story_text)):
        story_line = font.render(story_text[line], True, DARK_BLUE)
        story_rect = story_line.get_rect()
        if line == 5:
            line += 1
        screen.blit(story_line, (WIDTH/2 - story_rect.width/2, HEIGHT/2 - story_rect.height/2 - 84 + (line * 28)))

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_story_line = False
                is_game_instructions = True
                break

instruction_text = ["Catch seeds as the planter (player 1).", "Catch trash as the cleaner (player 2).", "Lose a heart for catching the wrong item.", "Lose a point for missing an item.", "Press Space to start"]

while is_game_instructions:
    screen.blit(bg_img, (0, 0))

    for line in range(len(instruction_text)):
        instruction_line = font.render(instruction_text[line], True, DARK_BLUE)
        instruction_rect = instruction_line.get_rect()
        if line == 4:
            line += 1
        screen.blit(instruction_line, (WIDTH/2 - instruction_rect.width/2, HEIGHT/2 - instruction_rect.height/2 - 84 + (line * 28)))

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_game_instructions = False
                break
    
# create player objects
player_1 = Player1()
player_2 = Player2()

items = []
time = 0
frames = 150
obj_speed = 1

game_over = False
running = True

while running:
    screen.blit(bg_img, (0, 0))

    if game_over:
        game_over_text = title_font.render("Game Over!", True, DARK_BLUE)
        game_over_rect = game_over_text.get_rect()
        screen.blit(game_over_text, (WIDTH/2 - game_over_rect.width/2, HEIGHT/2 - game_over_rect.height/2 - 48))

        score_text = font.render("Final Score: " + str(score), True, DARK_BLUE)
        score_rect = score_text.get_rect()
        screen.blit(score_text, (WIDTH/2 - score_rect.width/2, HEIGHT/2 - score_rect.height/2))

        inst_text = font.render("Press SPACE to play again", True, DARK_BLUE)
        inst_rect = inst_text.get_rect()
        screen.blit(inst_text, (WIDTH/2 - inst_rect.width/2, HEIGHT/2 - inst_rect.height/2 + 24))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_over = False
                    running = True
                    score = 0
                    lives = 3
                    player_1.x = 160
                    player_2.x = 256
                    items = []
                    time = 0
                    obj_speed = 1
        pg.display.update()
        continue

    if lives == 0:
        game_over = True
        continue

    for event in pg.event.get():
        if event.type == pg.QUIT: #checks if the user quits the game
            pg.quit() #quits the game
            break

    key = pg.key.get_pressed() #checks the key pressed

    if key[pg.K_LEFT]: 
        player_2.x -= player_2.speed #moves the player 1 to the left
        if player_2.x <= -12:
            player_2.x = -12
    if key[pg.K_RIGHT]: 
        player_2.x += player_2.speed #moves the player 1 to the right
        if player_2.x >= WIDTH - 112:
            player_2.x = WIDTH - 112
    if key[pg.K_a]:
        player_1.x -= player_1.speed
        if player_1.x <= -12:
            player_1.x = -12
    if key[pg.K_d]:
        player_1.x += player_1.speed 
        if player_1.x >= WIDTH - 112: 
            player_1.x = WIDTH - 112
    
    # drop items
    to_remove = set()
    for obj in items:
        obj.drop_object(screen)
        # check collisions for each player with each object
        for player in [player_1, player_2]:
            collision, obj_type = obj.check_collision(player)
            player_type = player.type
            # check type of collision
            if collision:
                if obj_type == "seed":
                    # if seed colldies with planter, add point
                    if player_type == "planter":
                        score += 1
                    # otherwise seed collides with cleaner, lose a life
                    else:
                        lives -= 1
                elif obj_type == "trash":
                    # if trash collides with cleaner, add point
                    if player_type == "cleaner":
                        score += 1
                    # otherwise trash collides with planter, lose a life
                    else:
                        lives -= 1
                # otherwise object collides with ground, lose a life
                elif obj_type == "ground":
                    score -= 1
                # todo: fix remove
                to_remove.add(obj)
                break
    for obj in to_remove:
        items.remove(obj)

    # blit players
    screen.blit(player_1.idle_img, (player_1.x, player_1.y))
    screen.blit(player_2.idle_img, (player_2.x, player_2.y))

    # spawn new object after 
    if time % frames == 0:
        items.append(Object(obj_speed))

    # speed up objects after score reaches multiple of 5
    if score % 5 == 0:
        obj_speed += 1
    time += 1
    
    # display score + lives text
    score_text = font.render("Score: " + str(score), True, DARK_BLUE)
    score_rect = score_text.get_rect()

    lives_text = font.render("Lives", True, DARK_BLUE)
    lives_rect = lives_text.get_rect()

    screen.blit(score_text, (WIDTH/2 - score_rect.width/2, 0 + score_rect.height))
    screen.blit(lives_text, (8, HEIGHT - lives_rect.height - 8))
    for life in range(lives):
        screen.blit(heart_img, (8 + lives_rect.width + (40 * life), HEIGHT - 32))
    
    pg.display.update()

# TODO: update aseprite files

# TODO: ranks, instructions, game over screen, music, README.md, switching between player sprites