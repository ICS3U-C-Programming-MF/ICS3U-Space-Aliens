#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the constants for "space aliens" code.py

import random

# PyBadge screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
TOTAL_NUMBER_OF_ROCKETS = 5
ROCKET_AMMO = 5
RELOAD_TIME = 5  # seconds
SHIP_SPEED = 1
EASY_MODE = -2
HARD_MODE = +2
SMALL_ALIEN_SPEED = 2
BIG_ALIEN_SPEED = 0.5
NORMAL_ALIEN_SPEED = 1
LASER_SPEED = 3
ROCKET_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
OFF_LEFT_SCREEN = -1 * SPRITE_SIZE
OFF_RIGHT_SCREEN = SCREEN_X + SPRITE_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "Just Pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
    "button_a": False,
    "button_b": False,
}

# new pallet for red filled text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
