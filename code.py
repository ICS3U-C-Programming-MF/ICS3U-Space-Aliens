#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the "space aliens program on the pybadge
# black ./*.py

# Import libraries needed for graphics, input, and sound
import ugame  # Handles buttons, sound, and display
import stage  # Handles sprites, backgrounds, and text
import time  # handles events to make for pauses in the game
import constants  # Stores screen size, FPS, palettes, etc.
import random  # Used to generate random things (like alien positions)


class SpaceAliens:
    def __init__(self):
        self.scene = "splash"

    def run(self):
        while True:
            if self.scene == "splash":
                self.scene = self.back_splash()
            elif self.scene == "menu":
                self.scene = self.menu_scene()
            elif self.scene == "difficulty":
                self.scene = self.difficulty_selection()
            elif self.scene == "game":
                self.scene = self.game_scene()

    # --------------------------------------------------
    # BACK SPLASH SCENE
    # --------------------------------------------------
    def back_splash(self):
        """
        Displays the back splash screen.
        """
        # ---------SOUND----------
        coin_sound = open("coin.wav", "rb")  # Sound played on selection
        sound = ugame.audio
        sound.stop()
        sound.mute(False)
        sound.play(coin_sound)

        # ---------- BACKGROUND ----------
        image_bank_background = stage.Bank.from_bmp16(
            "space_aliens_background.bmp"  # Background image file
        )
        background = stage.Grid(
            image_bank_background,
            constants.SCREEN_X,  # Grid width
            constants.SCREEN_Y,  # Grid height
        )
        for _ in range(3):
            for x_location in range(constants.SCREEN_GRID_X):
                for y_location in range(constants.SCREEN_GRID_Y):
                    tile_picked = random.randint(0, 3)
                    if tile_picked == 1:
                        tile_picked = 0
                    background.tile(x_location, y_location, tile_picked)

        # ---------- CREATE STAGE ----------
        game = stage.Stage(ugame.display, constants.FPS)

        # Layers are drawn from LEFT (top) to RIGHT (bottom)
        game.layers = [background]

        # Draw everything once
        game.render_block()

        # Pause for 2 seconds
        while True:
            time.sleep(2.0)
            return "menu"

    # --------------------------------------------------
    # MENU SCENE
    # --------------------------------------------------
    def menu_scene(self):
        """
        Displays the title screen and waits for the START button.
        """

        # ---------- TITLE TEXT ----------
        title_text = stage.Text(
            width=29,  # Number of characters wide
            height=12,  # Number of characters tall
            font=None,  # Default font
            palette=constants.RED_PALETTE,  # Red text palette
            buffer=None,
        )
        title_text.move(20, 10)  # Position text on screen
        title_text.text("SPACE ALIENS")  # Set text content

        # ---------- START PROMPT ----------
        start_text = stage.Text(
            width=27, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        start_text.move(0, 85)  # Bottom of screen
        start_text.text("PRESS START TO BEGIN")

        # ---------- BACKGROUND ----------
        image_bank_background = stage.Bank.from_bmp16(
            "space_aliens_background.bmp"  # Background image file
        )
        background = stage.Grid(
            image_bank_background,
            constants.SCREEN_GRID_X,  # Grid width
            constants.SCREEN_GRID_Y,  # Grid height
        )

        for _ in range(3):
            for x_location in range(constants.SCREEN_GRID_X):
                for y_location in range(constants.SCREEN_GRID_Y):
                    tile_picked = random.randint(0, 3)
                    if tile_picked == 1:
                        tile_picked = 0
                    background.tile(x_location, y_location, tile_picked)

        # ---------- CREATE STAGE ----------
        game = stage.Stage(ugame.display, constants.FPS)

        # Layers are drawn from LEFT (top) to RIGHT (bottom)
        game.layers = [title_text, start_text, background]

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
    def difficulty_selection(self):
        """
        Lets the player choose EASY (B) or HARD (A).
        """

        # Track button states (for edge detection)
        a_button = constants.button_state["button_up"]
        b_button = constants.button_state["button_up"]

        # ---------SOUND----------
        coin_sound = open("coin.wav", "rb")  # Sound played on selection
        sound = ugame.audio
        sound.stop()
        sound.mute(False)
        # ---------- TEXT ----------
        title_text = stage.Text(
            width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        title_text.move(20, 50)  # the first number is x axis, second is y axis
        title_text.text("Press A for HARD")

        start_text = stage.Text(
            width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        start_text.move(20, 5)  # the first number is x axis, second is y axis
        start_text.text("PRESS B FOR EASY")

        # ---------- BACKGROUND ----------
        image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
        background = stage.Grid(
            image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
        )

        for _ in range(3):
            for x_location in range(constants.SCREEN_GRID_X):
                for y_location in range(constants.SCREEN_GRID_Y):
                    tile_picked = random.randint(0, 3)
                    if tile_picked == 1:
                        tile_picked = 0
                    background.tile(x_location, y_location, tile_picked)

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
                aliens = constants.TOTAL_NUMBER_OF_ALIENS + 3  # Example variable change
                # PROCEED TO GAME
                sound.play(coin_sound)
                time.sleep(0.8)
                return "game"

            if b_button == constants.button_state["button_just_pressed"]:
                # EASY MODE VARIABLES WOULD GO HERE
                aliens = constants.TOTAL_NUMBER_OF_ALIENS - 3  # Example variable change
                # PROCEED TO GAME
                sound.play(coin_sound)
                time.sleep(0.8)
                return "game"

            game.render_block()
            game.tick()

    # --------------------------------------------------
    # GAME SCENE
    # --------------------------------------------------
    def game_scene(self):
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
        pew_sound = open("pew.wav", "rb")  # Laser sound
        boom_sound = open("boom.wav", "rb")  # Explosion sound
        pew2_sound = open("pew2.wav", "rb")  # Alternate laser sound
        sound = ugame.audio
        sound.stop()
        sound.mute(False)

        # ---------- BACKGROUND ----------
        background = stage.Grid(
            image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
        )
        # ---------- GAME VARIABLES ----------
        rocket_ammo = constants.TOTAL_NUMBER_OF_ROCKETS
        reloading = False
        reload_start_time = 0
        reload_R = constants.RELOAD_TIME

        # ---------- TEXT ----------
        ammo_text = stage.Text(
            width=26, height=9, font=None, palette=constants.RED_PALETTE, buffer=None
        )
        ammo_text.move(20, 5)
        ammo_text.text("Rocket Ammo: 3")

        for _ in range(3):
            for x_location in range(constants.SCREEN_GRID_X):
                for y_location in range(constants.SCREEN_GRID_Y):
                    tile_picked = random.randint(2, 3)
                    background.tile(x_location, y_location, tile_picked)

        # ---------- SPRITES ----------
        ship = stage.Sprite(
            image_bank_sprites,
            5,  # Sprite index
            75,
            constants.SCREEN_Y - (2 * constants.SPRITE_SIZE),
        )

        self.aliens = []
        self.aliens_directions = []
        for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
            a_single_alien = stage.Sprite(
                image_bank_sprites,
                9,
                random.randint(0, constants.SCREEN_X - constants.SPRITE_SIZE),
                random.randint(0, 40),
            )
            self.aliens.append(a_single_alien)
            self.aliens_directions.append(random.choice([-1, 1]))

        lasers = []
        for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
            a_single_laser = stage.Sprite(
                image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
            )
            lasers.append(a_single_laser)

        rockets = []
        for rocket_number in range(constants.TOTAL_NUMBER_OF_ROCKETS):
            a_single_rocket = stage.Sprite(
                image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
            )
            rockets.append(a_single_rocket)
        # ---------- STAGE ----------
        game = stage.Stage(ugame.display, constants.FPS)
        game.layers = self.aliens + lasers + rockets + [ship] + [background]
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
                ship.move(
                    min(ship.x + 1, constants.SCREEN_X - constants.SPRITE_SIZE), ship.y
                )

            if keys & ugame.K_LEFT:
                ship.move(max(ship.x - 1, 0), ship.y)

            if keys & ugame.K_UP:
                ship.move(ship.x, max(ship.y - 1, 0))

            if keys & ugame.K_DOWN:
                ship.move(
                    ship.x, min(ship.y + 1, constants.SCREEN_Y - constants.SPRITE_SIZE)
                )

            # ---------- TRIGGERS ----------
            if a_button == constants.button_state["button_just_pressed"]:
                # Fire laser from ship
                for laser_numbers in range(len(lasers)):
                    if lasers[laser_numbers].x < 0:  # If laser is off screen
                        lasers[laser_numbers].move(ship.x, ship.y)
                        sound.play(pew_sound)
                        break
                a_button = constants.button_state["button_still_pressed"]

            if b_button == constants.button_state["button_just_pressed"]:
                if rocket_ammo > 0 and not reloading:
                    for rocket in rockets:
                        if rocket.x < 0:
                            rocket.move(ship.x, ship.y)
                            rocket_ammo -= 1
                            sound.play(boom_sound)

                            if rocket_ammo == 0:
                                reloading = True
                                reload_start_time = time.monotonic()

                            ammo_text.text("Rocket Ammo: {}".format(rocket_ammo))
                            break  # break ONLY exits the rocket loop
                b_button = constants.button_state["button_still_pressed"]

                # ---------- RELOADING MECHANISM ----------
                if reloading:
                    if time.monotonic() - reload_start_time >= constants.RELOAD_TIME:
                        rocket_ammo = constants.TOTAL_NUMBER_OF_ROCKETS
                        reloading = False
                        ammo_text.text("Rocket Ammo: {}".format(rocket_ammo))
            # ---------- ALIEN BOSS AND DIFFRENT TYPES ----------
            # ---------- LASER MOVEMENT ----------
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x > 0:  # If laser is on screen
                    lasers[laser_number].move(
                        lasers[laser_number].x,
                        lasers[laser_number].y - constants.LASER_SPEED,
                    )
                    # If laser is off the top of the screen, move off screen
                    if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                        lasers[laser_number].move(
                            constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                        )

            # ---------- ROCKET MOVEMENT ----------
            for rocket_number in range(len(rockets)):
                if rockets[rocket_number].x > 0:  # If rocket is on screen
                    rockets[rocket_number].move(
                        rockets[rocket_number].x,
                        rockets[rocket_number].y - constants.ROCKET_SPEED,
                    )
                    # If rocket is off the top of the screen, move off screen
                    if rockets[rocket_number].y < constants.OFF_TOP_SCREEN:
                        rockets[rocket_number].move(
                            constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                        )
            # -----------GAME RESTART / DEBUG HACKS----------

            # If START is pressed, move to menu screen
            if keys & ugame.K_START:
                return "menu"

            # ----------- ALIEN MOVEMENT ----------
            for i in range(len(self.aliens)):
                alien = self.aliens[i]

                random_move = random.randint(1, 4)
                if random_move == 1 or random_move == 2:
                    # Move alien down
                    alien.move(alien.x, alien.y + constants.NORMAL_ALIEN_SPEED)
                elif random_move == 3 or random_move == 4:
                    # Horizontal movement
                    alien.move(
                        alien.x + self.aliens_directions[i],
                        alien.y + constants.NORMAL_ALIEN_SPEED,
                    )

                # Bounce off walls
                if (
                    alien.x <= 0
                    or alien.x >= constants.SCREEN_X - constants.SPRITE_SIZE
                ):
                    self.aliens_directions[i] *= -1

                # Respawn if off screen
                if alien.y > constants.SCREEN_Y:
                    alien.move(
                        random.randint(0, constants.SCREEN_X - constants.SPRITE_SIZE),
                        constants.OFF_TOP_SCREEN,
                    )

            # ---------- RENDER ----------
            game.render_sprites(self.aliens + lasers + rockets + [ship])
            game.tick()


if __name__ == "__main__":
    game = SpaceAliens()
    game.run()
