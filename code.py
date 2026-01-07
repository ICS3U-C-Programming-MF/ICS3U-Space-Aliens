#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the "space aliens program on the pybadge

import ugame
import stage


def game_scene():
    # This function is the main scene of the game

    # image banks for circuit python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to the image 0 in the image bank
    # and the size to 10x8 tiles of 16x16 pixels each
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite for that will be updated every frame
    cowboy = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the game background
    game = stage.Stage(ugame.display, 60)

    # set the background layer
    game.layers = [cowboy] + [background]

    # render all sprites
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("START")
        if keys & ugame.K_SELECT:
            print("SELECT")
        if keys & ugame.K_RIGHT:
            cowboy.move(cowboy.x + 1, cowboy.y)
        if keys & ugame.K_LEFT:
            cowboy.move(cowboy.x - 1, cowboy.y)
        if keys & ugame.K_UP:
            cowboy.move(cowboy.x, cowboy.y - 1)
        if keys & ugame.K_DOWN:
            cowboy.move(cowboy.x, cowboy.y + 1)

        # update game logic

        # redraw Sprites
        game.render_sprites([cowboy])
        game.tick()


if __name__ == "__main__":
    game_scene()