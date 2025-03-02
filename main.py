import pygame as pg
from random import randint
from objects import Object
from players import Player1, Player2

pg.init()
# import images
bg_img = pg.image.load("assets/bg.png")
heart_img = pg.transform.scale(pg.image.load("assets/heart.png"), (32, 32))
icon_img = pg.image.load("assets/icon.png")

# import pixel font
pixelify = "assets/PixelifySans-VariableFont_wght.ttf"
title_font = pg.font.Font(pixelify, 48)
font = pg.font.Font(pixelify, 24)
fact_font = pg.font.Font(pixelify, 16)

# import and play main theme
pixel_song = pg.mixer.Sound("assets/pixel_song.mp3")
pg.mixer.Channel(0).play(pixel_song, -1)

# import sfx
basket_sfx = pg.mixer.Sound("assets/basket.mp3")
error_sfx = pg.mixer.Sound("assets/error.mp3")

# constants
WIDTH=512
HEIGHT=384
DARK_BLUE = (8, 33, 64) # RGB color

# storing facts + advice
facts = ["Consumption halved wildlife population in last fifty years.", "14 million tonnes of plastic enter oceans annually.", "300 football fields worth of trees are cut down hourly.", "Deforestry can directly increase infectious disease outbreaks."]
advice = ["Avoid single use plastics!", "Make sure to dispose of your trash properly; reuse and recycle!", "Opt for responsibly created wood products!", "Planting trees is nature's way of combating climate change. 🌳"]

# initialize screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("LandSavers")
pg.display.set_icon(icon_img)

# keep track of scores + lives
score = 0
lives = 3

# create title screen text
title_text = title_font.render("LandSavers", True, DARK_BLUE)
title_rect = title_text.get_rect()

p1_text = font.render("Player 1: Planter, use A/D to move", True, DARK_BLUE)
p1_rect = p1_text.get_rect()
p2_text = font.render("Player 2: Cleaner, use LEFT/RIGHT to move", True, DARK_BLUE)
p2_rect = p2_text.get_rect()

inst_text = font.render("Press SPACE to start", True, DARK_BLUE)
inst_rect = inst_text.get_rect()

# title screen loop
is_title_screen = True
is_story_line = False

while is_title_screen:
    # blit bg image and text
    screen.blit(bg_img, (0, 0))
    screen.blit(title_text, (WIDTH/2 - title_rect.width/2, HEIGHT/2 - title_rect.height/2 - 56))
    screen.blit(p1_text, (WIDTH/2 - p1_rect.width/2, HEIGHT/2 - p1_rect.height/2 - 20))
    screen.blit(p2_text, (WIDTH/2 - p2_rect.width/2, HEIGHT/2 - p2_rect.height/2+8))
    screen.blit(inst_text, (WIDTH/2 - inst_rect.width/2, HEIGHT/2 - inst_rect.height/2 + 65))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
    # move on to story line screen if space is pressed
    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        is_title_screen = False
        is_story_line = True
        break
    pg.display.update()

# story line text
is_game_instructions = False
story_text = ["The world is ending!", "You and your friend must help restore", "sustainability in the world!", "Collect seeds to be planted later", "and catch plastic to clean the land.", "Press Space to continue"]

# story line loop
while is_story_line:
    screen.blit(bg_img, (0, 0))

    # blit each line in story_text
    for line in range(len(story_text)):
        story_line = font.render(story_text[line], True, DARK_BLUE)
        story_rect = story_line.get_rect()
        # add extra space above last line
        if line == 5:
            line += 1
        screen.blit(story_line, (WIDTH/2 - story_rect.width/2, HEIGHT/2 - story_rect.height/2 - 84 + (line * 28)))

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        # move on to game instructions screen if space is pressed
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_story_line = False
                is_game_instructions = True
                break

# game instructions text
instruction_text = ["Catch seeds as the planter (player 1).", "Catch bottles as the cleaner (player 2).", "Lose a point for catching the wrong item.", "Lose a life for missing an item.", "Press Space to start"]

while is_game_instructions:
    screen.blit(bg_img, (0, 0))

    # blit each line in instruction_text
    for line in range(len(instruction_text)):
        instruction_line = font.render(instruction_text[line], True, DARK_BLUE)
        instruction_rect = instruction_line.get_rect()
        # add extra space above last line
        if line == 4:
            line += 1
        screen.blit(instruction_line, (WIDTH/2 - instruction_rect.width/2, HEIGHT/2 - instruction_rect.height/2 - 84 + (line * 28)))

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break
        # move on to game if space is pressed
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_game_instructions = False
                break
    
# create player objects
player_1 = Player1()
player_2 = Player2()

# keep track of objects + time
items = []
time = 0
frames = 150
obj_speed = 1
fact_int = 0

game_over = False
running = True

# main game loop
while running:
    screen.blit(bg_img, (0, 0))

    # game over screen
    if game_over:
        # display game over text
        game_over_text = title_font.render("Game Over!", True, DARK_BLUE)
        game_over_rect = game_over_text.get_rect()
        screen.blit(game_over_text, (WIDTH/2 - game_over_rect.width/2, HEIGHT/2 - game_over_rect.height/2 - 72))

        score_text = font.render("Final Score: " + str(score) + " / Rank: " + str(round((score/25)*100, 1)) + '%', True, DARK_BLUE)
        score_rect = score_text.get_rect()
        screen.blit(score_text, (WIDTH/2 - score_rect.width/2, HEIGHT/2 - score_rect.height/2 - 36))
        
        # display fact + advice
        fact_heading = font.render("Fact & Advice", True, DARK_BLUE) 
        fact_rect = fact_heading.get_rect()
        screen.blit(fact_heading, (WIDTH/2 - fact_rect.width/2, HEIGHT/2 - fact_rect.height/2))

        fact_text = fact_font.render(facts[fact_int], True, DARK_BLUE)
        fact_rect = fact_text.get_rect()
        screen.blit(fact_text, (WIDTH/2 - fact_rect.width/2, HEIGHT/2 - fact_rect.height/2 + 24))

        advice_text = fact_font.render(advice[fact_int], True, DARK_BLUE)
        advice_rect = advice_text.get_rect()
        screen.blit(advice_text, (WIDTH/2 - advice_rect.width/2, HEIGHT/2 - advice_rect.height/2 + 40))

        inst_text = font.render("Press SPACE to play again", True, DARK_BLUE)
        inst_rect = inst_text.get_rect()
        screen.blit(inst_text, (WIDTH/2 - inst_rect.width/2, HEIGHT/2 - inst_rect.height/2 + 72))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break
            # restart game + related variables if space is pressed
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
                    fact_int = 0
                    for player in [player_1, player_2]:
                        player.cur_img = player.idle_img
        pg.display.update()
        continue

    # game_over if lives = 0
    if lives == 0:
        game_over = True
        fact_int = randint(0, 3)
        continue

    for event in pg.event.get():
        if event.type == pg.QUIT: #checks if the user quits the game
            pg.quit() #quits the game
            break

    key = pg.key.get_pressed() #checks the key pressed

    if key[pg.K_LEFT]: 
        player_2.x -= player_2.speed #moves the player_2 to the left
        if player_2.x <= -12:
            player_2.x = -12
    if key[pg.K_RIGHT]: 
        player_2.x += player_2.speed #moves the player_2 to the right
        if player_2.x >= WIDTH - 112:
            player_2.x = WIDTH - 112
    if key[pg.K_a]:
        player_1.x -= player_1.speed #moves player_1 to the left
        if player_1.x <= -12:
            player_1.x = -12
    if key[pg.K_d]:
        player_1.x += player_1.speed #moves player_1 to the right
        if player_1.x >= WIDTH - 112: 
            player_1.x = WIDTH - 112
    
    # drop items from above
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
                    # if seed colldies with planter, add point to score
                    if player_type == "planter":
                        # change player_1 sprite to happy
                        player_1.cur_img = player_1.catch_img
                        player_1.sprite_time = 0
                        pg.mixer.Channel(1).play(basket_sfx)
                        score += 1
                    # otherwise seed collides with cleaner, lose a life
                    else:
                        # change player_2 sprite to sad
                        player_2.cur_img = player_2.wrong_img
                        player_2.sprite_time = 0
                        pg.mixer.Channel(1).play(error_sfx)
                        score -= 1
                elif obj_type == "trash":
                    # if trash collides with cleaner, add point to score
                    if player_type == "cleaner":
                        # change player_2 sprite to happy
                        player_2.cur_img = player_2.catch_img
                        player_2.sprite_time = 0
                        pg.mixer.Channel(1).play(basket_sfx)
                        score += 1
                    # otherwise trash collides with planter, lose a life
                    else:
                        # change player_1 sprite to sad
                        player_1.cur_img = player_1.wrong_img
                        player_1.sprite_time = 0
                        pg.mixer.Channel(1).play(error_sfx)
                        score -= 1
                # otherwise object collides with ground, lose a point from score
                elif obj_type == "ground":
                    pg.mixer.Channel(1).play(error_sfx)
                    lives -= 1
                to_remove.add(obj)
                break
    # remove all objects that have collided
    for obj in to_remove:
        items.remove(obj)

    # update player sprites
    for player in [player_1, player_2]:
        player.sprite_time += 1
        # change sprite back to idle after 75 frames
        if player.sprite_time == 75:
            player.sprite_time = 0
            player.cur_img = player.idle_img

    # blit players
    screen.blit(player_1.cur_img, (player_1.x, player_1.y))
    screen.blit(player_2.cur_img, (player_2.x, player_2.y))

    # spawn new object after 
    if time % frames == 0:
        items.append(Object(obj_speed))

    # speed up objects every 1500 frames if scoer is positive
    if time % 1500 == 0 and score > 0:
        obj_speed += 0.25
    time += 1

    # display score + lives text
    score_text = font.render("Score: " + str(score) + " / Rank " + str(round((score/25)*100, 1)) + '%', True, DARK_BLUE)
    score_rect = score_text.get_rect()

    lives_text = font.render("Lives", True, DARK_BLUE)
    lives_rect = lives_text.get_rect()

    screen.blit(score_text, (WIDTH/2 - score_rect.width/2, 0 + score_rect.height))
    screen.blit(lives_text, (8, HEIGHT - lives_rect.height - 8))
    for life in range(lives):
        screen.blit(heart_img, (16 + lives_rect.width + (40 * life), HEIGHT - 40))
    
    pg.display.update()