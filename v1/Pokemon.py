import pygame
import random
from setup import *
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

# Images
# character_sprite = pygame.image.load('sprite.png')
charizard_sprite = pygame.image.load("Charizard_Sprite.png")
pikachu_sprite = pygame.image.load("Pikachu_Sprite.png")
gold_sprite = pygame.image.load("gold_intro.png")
gold_sprite = pygame.transform.scale(gold_sprite, (250, 425))
red_spirte = pygame.image.load("red_intro.png")


background = pygame.image.load("Ice_background.png")

empty_health_bar = pygame.image.load("empty_health_bar.png")
empty_health_bar = pygame.transform.scale(empty_health_bar, (238, 28))

battle_platform = pygame.image.load("battle_platform.png")
battle_platform = pygame.transform.scale(battle_platform, (290, 60))

textBox = pygame.image.load("textbox.png")
textBox = pygame.transform.scale(textBox, (470, 135))

pokemon_logo = pygame.image.load("pokemon_logo.png")
pokemon_logo = pygame.transform.scale(pokemon_logo, (450, 200))
#
# intro_background = pygame.image.load("introscreen_background.jpg")
# intro_background = pygame.transform.scale(intro_background, (1000, 600))

intro_charizard = pygame.image.load("intro_charizard.png")

intro_pikachu = pygame.image.load("intro_pikachu.png")
intro_pikachu = pygame.transform.scale(intro_pikachu, (220, 300))

pokeball_img = pygame.image.load("pokeball.png")
pokeball_img = pygame.transform.scale(pokeball_img, (380, 380))

crying_pikachu_img = pygame.image.load("crying_pikachu.jpg")
crying_pikachu_img = pygame.transform.scale(crying_pikachu_img, (1000, 600))
happy_pikachu_img = pygame.image.load("happy_pikachu.jpg")
happy_pikachu_img = pygame.transform.scale(happy_pikachu_img, (1000, 600))

# Audio
battle_theme = 'Pokemon_Red_Theme.mp3'
intro_theme = "intro_song.mp3"


thunderbolt_sound = pygame.mixer.Sound("thunderbolt.wav")
thunderbolt_sound.set_volume(0.7)

voltTackle_sound = pygame.mixer.Sound("volt_tackle.wav")
voltTackle_sound.set_volume(0.7)

doubleTeam_sound = pygame.mixer.Sound("double_team.wav")
doubleTeam_sound.set_volume(0.7)

recover_sound = pygame.mixer.Sound("recover.wav")
recover_sound.set_volume(0.7)

flamethrower_sound = pygame.mixer.Sound("flamethrower.wav")
flamethrower_sound.set_volume(0.7)

fireblast_sound = pygame.mixer.Sound("fireblast.wav")
fireblast_sound.set_volume(0.7)

clock = pygame.time.Clock()
fps = clock.tick(fps)

pygame.display.set_caption(title)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_width, display_height))

screen.fill(WHITE)
pygame.display.set_caption(title)


thunderbolt_colour = WHITE
recover_colour = WHITE
doubleTeam_colour = WHITE
voltTackle_colour = WHITE

# Pokemon Health
health_charizard = 400
health_pikachu = 350
pikachu_health_length = 208
charizard_health_length = 208

pygame.mixer.music.load(intro_theme)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)


def draw():
    screen.fill(WHITE)

    screen.blit(background, (0, 0))

    screen.blit(battle_platform, (630, 310))
    screen.blit(battle_platform, (95, 430))

    screen.blit(charizard_sprite, (655, 120))
    screen.blit(pikachu_sprite, (150, 300))

    # Move box outline
    pygame.draw.line(screen, BLACK, (500, 470), (930, 470), 4)
    pygame.draw.line(screen, BLACK, (500, 580), (930, 580), 4)
    pygame.draw.line(screen, BLACK, (500, 470), (500, 580), 4)
    pygame.draw.line(screen, BLACK, (930, 470), (930, 580), 4)

    # Pokemon textbox dialogue
    pygame.draw.rect(screen, BEIGE, (23, 468.5, 440, 120))
    screen.blit(textBox, (10, 455))

    pygame.display.flip()


# Pokemon Health
health_charizard = 400
health_pikachu = 350
pikachu_health_length = 208
charizard_health_length = 208


# Thunderbolt messages
thunderbolt_msg = font_moves.render('Pikachu used Thunderbolt!', True, (BLACK))
thunderbolt_crit_msg = font_moves.render("Thunderbolt's a critical hit!", True, (BLACK))
thunderbolt_miss_msg = font_moves.render("Thunderbolt Missed!", True, (BLACK))

# Double Team messages
doubleTeam_msg = font_moves.render("Pikachu used doubleteam!", True, (BLACK))
doubleTeam_miss_msg = font_moves.render("Doubleteam missed!", True, (BLACK))

# Recover messages
pikachu_recover_msg = font_moves.render("Pikachu used recover!", True, (BLACK))
pikachu_recover_fail_msg = font_moves.render("Pikachus recover failed!", True, (BLACK))
charizard_recover_msg = font_moves.render("Charizard used recover!", True, (BLACK))
charizard_recover_fail_msg = font_moves.render("Charizards recover failed!", True, (BLACK))

# Volt tackle messages
voltTackle_msg = font_moves.render("Pikachu used volt tackle!", True, (BLACK))
voltTackle_miss_msg = font_moves.render("Volt tackle missed!", True, (BLACK))
voltTackle_crit_msg = font_moves.render("Volt tackle's a critical hit", True, (BLACK))

# Flamethrower messages
flamethrower_msg = font_moves.render("Charizard used flamethrower", True, (BLACK))
flamethrower_miss_msg = font_moves.render("Flamethrower missed!", True, (BLACK))
flamethrower_crit_msg = font_moves.render("Flamethrower's a critical hit", True, (BLACK))

# Fire Blast messages
fireBlast_msg = font_moves.render("Charizard used fireblast", True, (BLACK))
fireBlast_miss_msg = font_moves.render("Fire blast missed!", True, (BLACK))
fireBlast_crit_msg = font_moves.render("Fire Blast's a critical hit!", True, (BLACK))


def charizard_draw():
    global health_charizard, charizard_health_length
    charizard_health_text = font.render("{} / 400".format(health_charizard), False, (BLACK))
    screen.blit(charizard_health_text, (510, 160))

    charizard_text = font.render("Charizard", False, (BLACK))
    screen.blit(charizard_text, (510, 100))

    # Charizard health bar
    screen.blit(empty_health_bar, (90, 270))
    screen.blit(empty_health_bar, (415, 120))
    pygame.draw.rect(screen, RED, (425, 128, 208, 13))
    pygame.draw.rect(screen, FOREST_GREEN, (425, 128, charizard_health_length, 13))


def pikachu_draw():
    global pikachu_health_length, health_pikachu
    pikachu_health_text = font.render("{} / 350".format(health_pikachu), False, (BLACK))
    screen.blit(pikachu_health_text, (210, 250))

    pikachu_text = font.render("Pikachu", False, (BLACK))
    screen.blit(pikachu_text, (108, 250))

    # Pikachu health bar
    pygame.draw.rect(screen, RED, (100, 278, 208, 13))
    pygame.draw.rect(screen, FOREST_GREEN, (100, 278, pikachu_health_length, 13))


def main_draw():
    global thunderbolt_colour, doubleTeam_colour, recover_colour, voltTackle_colour
    # Moves Box
    # Top left box
    pygame.draw.rect(screen, thunderbolt_colour, (502, 472.5, 213, 53))
    # Bottom left box
    pygame.draw.rect(screen, doubleTeam_colour, (502, 526, 213, 54))
    # Top right box
    pygame.draw.rect(screen, recover_colour, (716.9, 472.5, 214, 53))
    # Bottom right box
    pygame.draw.rect(screen, voltTackle_colour, (716.9, 526.5, 214, 54))

    # Moves Cross Section
    pygame.draw.line(screen, BLACK, (500, 525), (930, 525), 3)
    pygame.draw.line(screen, BLACK, (715, 470), (715, 580), 3)


def instructions():

    screen.fill(WHITE)
    intro_heading = large_text.render("Welcome to the World of Pokemon!", False, (BLACK))
    intro_text = small_font.render(
        "This is the epic battle between Red and Gold. Red, who is the protagonist of first generation Pokemon games. His opponent,", False, (BLACK))
    intro_text1 = small_font.render(
        "Gold is the protagonist of the second generation games. Both individuals have defeated team Rocket all by themselves and", False, (BLACK))
    intro_text2 = small_font.render(
        "are considered Pokemon masters. Who's better, Red... or Gold???", False, (BLACK))
    intro_text3 = small_font.render(
        "You will be playing as Gold and against youu opponent, Red. Your one and only Pokemon is iconic Pikachu, while your", False, (BLACK))
    intro_text4 = small_font.render(
        "opponent has a powerful Charizard. As a young Pokemon master you must defeat Red and secure the position of best trainer", False, (BLACK))
    intro_text5 = font.render("Pikachu", False, (BLACK))
    intro_text6 = small_font1.render(
        "Thunderbolt: Most consistent attack move, which deals adequate damage.", False, (BLACK))
    intro_text7 = small_font1.render(
        "Volt Tackle: Least consistent attack move but can deal a significant amount of damage.", False, (BLACK))
    intro_text8 = small_font1.render(
        "Double team: Increases Pikachu’s evasiveness.", False, (BLACK))
    intro_text9 = small_font1.render(
        "Recover: Has a chance of restoring a portion of Pikachu’s lost health.", False, (BLACK))
    intro_text10 = font.render("Charizard", False, (BLACK))
    intro_text11 = small_font1.render(
        "Flamethrower: Most consistent attack ove, which deals adequate damage.", False, (BLACK))
    intro_text12 = small_font1.render(
        "Fire blast: Least consistent attack move but deals a significant amount of damage.", False, (BLACK))
    intro_text13 = small_font1.render(
        "Recover: Has a chance of restoring a portion of Charizard’s lost health.", False, (BLACK))

    back_text = font.render("B A C K", False, (BLACK))

    screen.blit(intro_heading, (20, 20))
    screen.blit(intro_text, (20, 75))
    screen.blit(intro_text1, (20, 95))
    screen.blit(intro_text2, (20, 115))
    screen.blit(intro_text3, (20, 155))
    screen.blit(intro_text4, (20, 175))
    screen.blit(intro_text5, (20, 215))
    screen.blit(intro_text6, (20, 250))
    screen.blit(intro_text7, (20, 280))
    screen.blit(intro_text8, (20, 310))
    screen.blit(intro_text9, (20, 340))
    screen.blit(intro_text10, (20, 400))
    screen.blit(intro_text11, (20, 435))
    screen.blit(intro_text12, (20, 465))
    screen.blit(intro_text13, (20, 495))

    screen.blit(back_text, (20, 575))

    pygame.display.flip()


def game_intro():
    screen.fill(RED)

    screen.blit(pokeball_img, (330, 200))
    screen.blit(red_spirte, (850, 150))
    screen.blit(gold_sprite, (0, 150))

    # pygame.draw.rect(screen, colour_play, (460, 260, 120, 40))
    # pygame.draw.rect(screen, colour_instructions, (420, 450, 200, 40))

    play_text = large_text.render("Play", True, (BLACK))
    screen.blit(play_text, (480, 268))

    instructions_text = large_text.render("Instructions", True, (BLACK))
    screen.blit(instructions_text, (410, 460))

    screen.blit(intro_charizard, (600, 260))
    screen.blit(intro_pikachu, (130, 220))

    # screen.blit(intro_background, (0, 0))
    screen.blit(pokemon_logo, (280, 0))

    pygame.display.flip()


def game():
    global health_pikachu, health_charizard, charizard_health_length, pikachu_health_length
    global thunderbolt_y, flamethrower_y, flamethrower_x, thunderbolt_colour, doubleTeam_colour, voltTackle_colour, recover_colour
    global doubleTeam_msg, pikachu_recover_msg, pikachu_recover_fail_msg, charizard_recover_msg, charizard_recover_fail_msg
    global thunderbolt_msg, thunderbolt_miss_msg, thunderbolt_crit_msg, voltTackle_msg, voltTackle_crit_msg, voltTackle_miss_msg

    # Computer Random Choice - 1 = flamethrower / 2 = fireBlast / 3 = recover1 / 4 = fireBlast / 5 = flamethrower
    charizard_choice = random.randint(1, 5)

    for event in pygame.event.get():
        mousex, mousey = pygame.mouse.get_pos()

        # Thunderbolt Hover
        if 500 <= mousex <= 715 and 470 <= mousey <= 525:
            thunderbolt_colour = DARK_YELLOW
        else:
            thunderbolt_colour = YELLOW

        # Recover hover
        if 715 <= mousex <= 930 and 470 <= mousey <= 525:
            recover_colour = DARK_YELLOW
        else:
            recover_colour = YELLOW

        # Volt tackle hover
        if 715 <= mousex <= 930 and 525 <= mousey <= 580:
            voltTackle_colour = DARK_YELLOW
        else:
            voltTackle_colour = YELLOW

        # Doubleteam hover
        if 500 <= mousex <= 715 and 525 <= mousey <= 580:
            doubleTeam_colour = DARK_YELLOW
        else:
            doubleTeam_colour = YELLOW

        if event.type == pygame.MOUSEBUTTONUP:
            # Pikachu Thunderbolt
            if 500 <= mousex <= 715 and 470 <= mousey <= 525:
                health_charizard -= thunderbolt

                if thunderbolt == 0:
                    screen.blit(thunderbolt_miss_msg, (120, 490))

                if thunderbolt == 45:
                    pygame.mixer.Sound.play(thunderbolt_sound)
                    charizard_health_length -= 26
                    screen.blit(thunderbolt_msg, (100, 490))

                if thunderbolt == 25:
                    pygame.mixer.Sound.play(thunderbolt_sound)
                    # while charizard_health_length !=
                    charizard_health_length -= 13
                    screen.blit(thunderbolt_msg, (100, 490))

                pygame.display.flip()
                time.sleep(2)
                draw()
                main_draw()
                charizard_draw()
                pikachu_draw()
                pygame.display.flip()
                time.sleep(1.5)

                # Charizard Flamethrower
                if charizard_choice == 1 or 5:
                    health_pikachu -= flamethrower

                    if flamethrower == 0:
                        screen.blit(flamethrower_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif flamethrower == 35:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 20.8
                        screen.blit(flamethrower_msg, (100, 490))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif flamethrower == 48:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 29.174
                        screen.blit(flamethrower_crit_msg, (100, 490))
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Fire Blast
                if charizard_choice == 2 or 4:
                    health_pikachu -= fireBlast

                    if fireBlast == 0:
                        screen.blit(fireBlast_miss_msg, (95, 522))
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif fireBlast == 45:
                        pikachu_health_length -= 26.7429
                        screen.blit(fireBlast_msg, (95, 522))
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif fireBlast == 60:
                        pikachu_health_length -= 35.658
                        screen.blit(fireBlast_crit_msg, (95, 522))
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Recover
                if charizard_choice == 3:

                    if recover1 == 0:
                        screen.blit(charizard_recover_fail_msg)
                        pygame.display.flip()
                        continue

                    elif recover1 == 28 and recover1 < 373:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 14.56
                        screen.blit(charizard_recover_msg, (95, 522))
                        charizard_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif recover1 == 42 and recover1 < 359:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 21.84
                        screen.blit(charizard_recover_msg, (95, 522))
                        charizard_draw()
                        draw()
                        continue

            # Pikachu Volt Tackle
            if 715 <= mousex <= 930 and 525 <= mousey <= 580:
                health_charizard -= volt_tackle
                if volt_tackle == 0:
                    screen.blit(voltTackle_miss_msg, (100, 490))

                if volt_tackle == 38:
                    pygame.mixer.Sound.play(voltTackle_sound)
                    charizard_health_length -= 19.24
                    screen.blit(voltTackle_msg, (100, 490))

                if volt_tackle == 56:
                    pygame.mixer.Sound.play(voltTackle_sound)
                    charizard_health_length -= 28
                    screen.blit(voltTackle_crit_msg, (100, 490))

                pygame.display.flip()
                time.sleep(2)
                draw()
                main_draw()
                charizard_draw()
                pikachu_draw()
                pygame.display.flip()
                time.sleep(1.5)

                # Charizard Flamethrower
                if charizard_choice == 1 or 5:
                    health_pikachu -= flamethrower

                    if flamethrower == 0:
                        screen.blit(flamethrower_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif flamethrower == 35:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 20.8
                        screen.blit(flamethrower_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif flamethrower == 48:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 29.174
                        screen.blit(flamethrower_crit_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Fire Blast
                if charizard_choice == 2 or 4:
                    health_pikachu -= fireBlast

                    if fireBlast == 0:
                        screen.blit(fireBlast_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif fireBlast == 45:
                        pygame.mixer.Sound.play(fireblast_sound)
                        pikachu_health_length -= 26.7429
                        screen.blit(fireBlast_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif fireBlast == 60:
                        pygame.mixer.Sound.play(fireblast_sound)
                        pikachu_health_length -= 35.658
                        screen.blit(fireBlast_crit_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Recover
                if charizard_choice == 3:

                    if recover1 == 0:
                        screen.blit(charizard_recover_fail_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif recover1 == 28 and recover1 < 373:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 14.56
                        screen.blit(charizard_recover_msg, (95, 522))
                        pygame.display.flip()
                        charizard_draw()
                        draw()
                        continue

                    elif recover1 == 42 and recover1 < 359:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 21.84
                        screen.blit(charizard_recover_msg, (95, 522))
                        pygame.display.flip()
                        charizard_draw()
                        draw()
                        continue

            # Pikachu Double Team
            if 500 <= mousex <= 715 and 525 <= mousey <= 580:
                pygame.mixer.Sound.play(doubleTeam_sound)
                flamethrower_damage.append(0)
                fireBlast_damage.append(0)
                screen.blit(doubleTeam_msg, (100, 490))

                pygame.display.flip()
                time.sleep(3)
                draw()

                # Charizard Flamethrower
                if charizard_choice == 1 or 5:
                    health_pikachu -= flamethrower

                    if flamethrower == 0:
                        screen.blit(flamethrower_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif flamethrower == 35:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 20.8
                        screen.blit(flamethrower_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif flamethrower == 48:
                        pikachu_health_length -= 29.174
                        screen.blit(flamethrower_crit_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Fire Blast
                if charizard_choice == 2 or 4:
                    health_pikachu -= fireBlast

                    if fireBlast == 0:
                        screen.blit(fireBlast_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif fireBlast == 45:
                        pikachu_health_length -= 26.7429
                        screen.blit(fireBlast_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif fireBlast == 60:
                        pikachu_health_length -= 35.658
                        screen.blit(fireBlast_crit_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                # Charizard Recover
                if charizard_choice == 3:

                    if recover1 == 0:
                        screen.blit(charizard_recover_fail_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif recover1 == 28 and recover1 < 373:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 14.56
                        screen.blit(charizard_recover_msg, (95, 522))
                        pygame.display.flip()
                        charizard_draw()
                        draw()
                        continue

                    elif recover1 == 42 and recover1 < 359:
                        health_charizard += recover1
                        pygame.mixer.Sound.play(recover_sound)
                        charizard_health_length += 21.84
                        screen.blit(charizard_recover_msg, (95, 522))
                        pygame.display.flip()
                        charizard_draw()
                        draw()
                        continue

            # Pikachu Recover
            if 715 <= mousex <= 930 and 470 <= mousey <= 525:
                if health_pikachu >= 350 or recover == 0 or (recover == 42 and recover > 308) or (recover == 28 and health_pikachu > 322):
                    screen.blit(pikachu_recover_fail_msg, (100, 490))

                elif recover == 42 and health_pikachu <= 308:
                    pikachu_health_length += 24.96
                    pygame.mixer.Sound.play(recover_sound)
                    health_pikachu += recover
                    screen.blit(pikachu_recover_msg, (100, 490))

                elif recover == 28 and health_pikachu <= 322:
                    pikachu_health_length += 16.64
                    pygame.mixer.Sound.play(recover_sound)
                    health_pikachu += recover
                    screen.blit(pikachu_recover_msg, (100, 490))

                pygame.display.flip()
                time.sleep(3)
                pikachu_draw()
                draw()
                pikachu_draw()
                main_draw()
                charizard_draw()
                pygame.display.flip()

                # Charizard Flamethrower
                if charizard_choice == 1 or 5:
                    health_pikachu -= flamethrower

                    if flamethrower == 0:
                        screen.blit(flamethrower_miss_msg, (95, 522))
                        pygame.display.flip()
                        continue

                    elif flamethrower == 35:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 20.8
                        screen.blit(flamethrower_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    elif flamethrower == 48:
                        pygame.mixer.Sound.play(flamethrower_sound)
                        pikachu_health_length -= 29.174
                        screen.blit(flamethrower_crit_msg, (95, 522))
                        pygame.display.flip()
                        time.sleep(2)
                        pikachu_draw()
                        draw()
                        pygame.display.flip()
                        continue

                    # Charizard Fire Blast
                    if charizard_choice == 2 or 4:
                        health_pikachu -= fireBlast

                        if fireBlast == 0:
                            screen.blit(fireBlast_miss_msg, (95, 522))
                            pygame.display.flip()
                            continue

                        elif fireBlast == 45:
                            pygame.mixer.Sound.play(fireblast_sound)
                            pikachu_health_length -= 26.7429
                            screen.blit(fireBlast_msg, (95, 522))
                            pygame.display.flip()
                            time.sleep(2)
                            pikachu_draw()
                            draw()
                            pygame.display.flip()
                            continue

                        elif fireBlast == 60:
                            pygame.mixer.Sound.play(fireblast_sound)
                            pikachu_health_length -= 35.658
                            screen.blit(fireBlast_crit_msg, (95, 522))
                            pygame.display.flip()
                            time.sleep(2)
                            pikachu_draw()
                            draw()
                            pygame.display.flip()
                            continue

                    # Charizard Recover
                    if charizard_choice == 3:

                        if recover1 == 0:
                            screen.blit(charizard_recover_fail_msg, (95, 522))
                            pygame.display.flip()
                            continue

                        elif recover1 == 28 and recover1 < 373:
                            health_charizard += recover1
                            pygame.mixer.Sound.play(recover_sound)
                            charizard_health_length += 14.56
                            screen.blit(charizard_recover_msg, (95, 522))
                            pygame.display.flip()
                            charizard_draw()
                            draw()
                            continue

                        elif recover1 == 42 and recover1 < 359:
                            health_charizard += recover1
                            pygame.mixer.Sound.play(recover_sound)
                            charizard_health_length += 21.84
                            screen.blit(charizard_recover_msg, (95, 522))
                            pygame.display.flip()
                            charizard_draw()
                            draw()
                            continue

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def game_won():

    screen.blit(happy_pikachu_img, (0, 0))
    game_wontext = large_text.render("C O N G R A T U L A T I O N S", False, (BLACK))
    game_wontext1 = large_text.render("YOU HAVE WON!!!", False, (BLACK))
    back_text1 = font.render("B A C K", False, (BLACK))
    exit_text = font.render("E X I T", False, (BLACK))

    screen.blit(back_text1, (20, 575))
    screen.blit(exit_text, (920, 575))
    screen.blit(game_wontext, (250, 70))
    screen.blit(game_wontext1, (340, 130))

    pygame.display.flip()


def game_lost():

    screen.blit(crying_pikachu_img, (0, 0))
    game_losttext = large_text.render("PIKACHU IS DEAD!", False, (BLACK))
    game_losttext1 = large_text.render("YOU HAVE LOST!", False, (BLACK))
    back_text2 = font.render("B A C K", False, (BLACK))
    exit_text1 = font.render("E X I T", False, (BLACK))

    screen.blit(back_text2, (20, 575))
    screen.blit(exit_text1, (920, 575))
    screen.blit(game_losttext, (275, 70))
    screen.blit(game_losttext1, (345, 130))

    pygame.display.flip()


page = 0

while True:
    if page == 0:

        game_intro()
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                # Play button interaction
                if 475 <= mouse_x <= 550 and 260 <= mouse_y <= 300:
                    page = 2
                    print(page)

                # Introduction button click interaction
                elif 395 <= mouse_x <= 620 and 450 <= mouse_y <= 490:
                    page = 1
                    print(page)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    elif page == 1:
        instructions()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()

                if 20 <= mouseX <= 100 and 575 <= mouseY <= 590:
                    page = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    elif page == 2:

        pygame.mixer.music.load(battle_theme)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        draw()

        while health_charizard >= 0 and health_pikachu >= 0:

            charizard_draw()
            pikachu_draw()
            main_draw()

            # Animation variables
            thunderbolt_y = 40
            thunderbolt_y_velocity = 5

            flamethrower_y = 190
            flamethrower_x = 600
            flamethrower_y_velocity = 1
            flamethrower_x_velocity = 2.5

            # Thunderbolt Damage
            thunderbolt_dmg = [0, 25, 25, 25, 25, 25, 25, 25, 45]
            thunderbolt = random.choice(thunderbolt_dmg)

            # Volt Tackle Damage
            volt_tackle_dmg = [0, 0, 0, 38, 38, 38, 38, 38, 38, 56]
            volt_tackle = random.choice(volt_tackle_dmg)

            # Recover Effects
            recover_health = [0, 28, 28, 28, 28, 42, 42]
            recover = random.choice(recover_health)

            # Charizard Moves
            flamethrower_damage = [0, 35, 35, 35, 35, 35, 48]
            flamethrower = random.choice(flamethrower_damage)

            fireBlast_damage = [0, 0, 0, 0, 0, 45, 45, 60]
            fireBlast = random.choice(fireBlast_damage)

            recover_health1 = [0, 28, 28, 28, 28, 42, 42]
            recover1 = random.choice(recover_health1)

            thunderbolt_text = font.render("Thunderbolt", True, (BLACK))
            screen.blit(thunderbolt_text, (545, 490))

            doubleTeam_text = font.render("Double Team", True, (BLACK))
            screen.blit(doubleTeam_text, (545, 542))

            recover_text = font.render("Recover", True, (BLACK))
            screen.blit(recover_text, (773, 490))

            voltTackle_text = font.render("Volt Tackle", True, (BLACK))
            screen.blit(voltTackle_text, (763, 542))

            pygame.display.flip()

            game()
        if health_pikachu <= 0:
            time.sleep(0.5)
            page = 4
        elif charizard_health_length <= 0:
            time.sleep(0.5)
            page = 3

    elif page == 3:
        pygame.mixer.music.stop()
        game_won()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()

                if 20 <= mouseX <= 100 and 575 <= mouseY <= 590:
                    page = 2
                elif 900 <= mouseX <= 1000 and 575 <= mouseY <= 590:
                    pygame.quit()
                    quit()

    elif page == 4:
        pygame.mixer.music.stop()
        game_lost()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()

                if 20 <= mouseX <= 100 and 575 <= mouseY <= 590:
                    health_pikachu = 350
                    health_charizard = 400
                    charizard_health_length = 208
                    pikachu_health_length = 208
                    page = 2

                if 900 <= mouseX <= 1000 and 575 <= mouseY <= 590:
                    pygame.quit()
                    quit()
