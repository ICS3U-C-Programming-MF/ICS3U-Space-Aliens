#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the "space aliens program on the pybadge

# Import libraries needed for graphics, input, and sound
import ugame          # Handles buttons, sound, and display
import stage          # Handles sprites, backgrounds, and text
import time           # (Not currently used, but often helpful)
import constants      # Stores screen size, FPS, palettes, etc.


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------
def main():
    """
    Main program controller.
    Uses a state machine (scene variable) to switch
    between different parts of the game.
    """
    scene = "menu"  # Start the game on the menu screen

    # Infinite loop so the game never exits
    while True:
        if scene == "menu":
            scene = menu_scene()              # Go to menu
        elif scene == "difficulty":
            scene = difficulty_selection()    # Go to difficulty select
        elif scene == "game":
            scene = game_scene()              # Go to main game


# --------------------------------------------------
# MENU SCENE
# --------------------------------------------------
def menu_scene():
    """
    Displays the title screen and waits for the START button.
    """

    # ---------- TITLE TEXT ----------
    title_text = stage.Text(
        width=29,                     # Number of characters wide
        height=12,                    # Number of characters tall
        font=None,                    # Default font
        palette=constants.RED_PALETTE,# Red text palette
        buffer=None
    )
    title_text.move(20, 10)            # Position text on screen
    title_text.text("SPACE ALIENS")    # Set text content

    # ---------- START PROMPT ----------
    start_text = stage.Text(
        width=27,
        height=10,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    start_text.move(0, 85)             # Bottom of screen
    start_text.text("PRESS START TO BEGIN")

    # ---------- BACKGROUND ----------
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp"  # Background image file
    )
    background = stage.Grid(
        image_bank_background,
        constants.SCREEN_GRID_X,       # Grid width
        constants.SCREEN_GRID_Y        # Grid height
    )

    # ---------- CREATE STAGE ----------
    game = stage.Stage(ugame.display, constants.FPS)

    # Layers are drawn from LEFT (top) to RIGHT (bottom)
    game.layers = [
        title_text,
        start_text,
        background
    ]

    # Draw everything once
    game.render_block()

    # ---------- INPUT LOOP ----------
    while True:
        keys = ugame.buttons.get_pressed()

        # If START is pressed, move to difficulty screen
        if keys & ugame.K_START:
            return "difficulty"

        # Keep game running at constant FPS
        game.tick()


# --------------------------------------------------
# DIFFICULTY SELECTION SCENE
# --------------------------------------------------
def difficulty_selection():
    """
    Lets the player choose EASY (B) or HARD (A).
    """

    # Track button states (for edge detection)
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]

    #---------SOUND----------
    coin_sound = open("coin.wav", "rb")  # Sound played on selection
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # ---------- TEXT ----------
    title_text = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    title_text.move(20, 10)  # the first number is x axis, second is y axis
    title_text.text("Press A for HARD")

    start_text = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    start_text.move(20, 5)  # the first number is x axis, second is y axis
    start_text.text("PRESS B FOR EASY")

    # ---------- BACKGROUND ----------
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp"
    )
    background = stage.Grid(
        image_bank_background,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y
    )

    # ---------- STAGE ----------
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [title_text, start_text, background]

    # ---------- INPUT LOOP ----------
    while True:
        keys = ugame.buttons.get_pressed()

        # ---------- B BUTTON STATE MACHINE ----------
        if keys & ugame.K_X:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        # ---------- A BUTTON STATE MACHINE ----------
        if keys & ugame.K_O:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # ---------- CHECK SELECTION ----------
        if a_button == constants.button_state["button_just_pressed"]:
            # HARD MODE VARIABLES WOULD GO HERE

            # PROCEED TO GAME
            sound.play(coin_sound)
            time.sleep(0.8)
            return "game"

        if b_button == constants.button_state["button_just_pressed"]:
            # EASY MODE VARIABLES WOULD GO HERE

            # PROCEED TO GAME
            sound.play(coin_sound)
            time.sleep(0.8)
            return "game"

        game.render_block()
        game.tick()


# --------------------------------------------------
# GAME SCENE
# --------------------------------------------------
def game_scene():
    """
    Main gameplay loop.
    Handles movement, sound, and sprite updates.
    """

    # ---------- IMAGE BANKS ----------
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # ---------- BUTTON STATES ----------
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # ---------- SOUND ----------
    pew_sound = open("pew.wav", "rb")     # Laser sound
    boom_sound = open("boom.wav", "rb")    # Explosion sound
    pew2_sound = open("pew2.wav", "rb")   # Alternate laser sound
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # ---------- BACKGROUND ----------
    background = stage.Grid(
        image_bank_background,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y
    )

    # ---------- SPRITES ----------
    ship = stage.Sprite(
        image_bank_sprites,
        5,                                # Sprite index
        75,
        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16
    )

    # ---------- STAGE ----------
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    # ---------- GAME LOOP ----------
    while True:
        keys = ugame.buttons.get_pressed()

        # ---------- BUTTON STATE UPDATES ----------
        if keys & ugame.K_X:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_O:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # ---------- SHIP MOVEMENT ----------
        if keys & ugame.K_RIGHT:
            ship.move(min(ship.x + 1, constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_LEFT:
            ship.move(max(ship.x - 1, 0), ship.y)

        if keys & ugame.K_UP:
            ship.move(ship.x, max(ship.y - 1, 0))

        if keys & ugame.K_DOWN:
            ship.move(ship.x, min(ship.y + 1, constants.SCREEN_Y - constants.SPRITE_SIZE))

        # ---------- SOUND TRIGGERS ----------
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
            a_button = constants.button_state["button_still_pressed"]

        if b_button == constants.button_state["button_just_pressed"]:
            sound.play(boom_sound)
            b_button = constants.button_state["button_still_pressed"]


        #-----------GANE RESTART / DEBUG HACKS----------
        # If START is pressed, move to menu screen
        if keys & ugame.K_START:
            return "menu"
        # ---------- RENDER ----------
        game.render_sprites([ship] + [alien])
        game.tick()



if __name__ == "__main__":
    main()