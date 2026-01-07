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

    # sets the background to the image 0 
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite thats updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the game background
    game = stage.Stage(ugame.display, constants.FPS)

    # set the background layer
    game.layers = [ship] + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else: 
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
