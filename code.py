#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the "space aliens program on the pybadge

import ugame
import stage


def game_scene():
    # main scene

    # image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets background to the image 0
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite will updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # sets stage for the background
    game = stage.Stage(ugame.display, 60)

    # background layer
    game.layers = [ship] + [background]

    # all sprites
    game.render_block()

    # Loop forever
    while True:
        # get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()