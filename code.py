#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the "space aliens program on the pybadge

import ugame
import stage

import constants


def game_scene():
    # This function is the main scene of the game

    # image banks for circuit python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Button state variables
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]


    # get sound ready
    pew_sound = open("pew.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sets the background to the image 0 
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite thats updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9,
                        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                        16)

    # create a stage for the game background
    game = stage.Stage(ugame.display, constants.FPS)

    # set the background layer
    game.layers = [ship] + [alien] + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_START != 0:
            print("start")
        if keys & ugame.K_SELECT != 0:
            print("select")
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else: 
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            if ship.y <= constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, ship.y + 1)

        # update game logic
        # play sound if a button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            a_button = constants.button_state["button_still_pressed"]
        if b_button == constants.button_state["button_just_pressed"]:
            sound.play(boom_sound)
            b_button = constants.button_state["button_still_pressed"]
        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    game_scene()
