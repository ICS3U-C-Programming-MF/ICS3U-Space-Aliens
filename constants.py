#!/usr/bin/env python3
# created by maximiliano
# date jan 07 2026
# This program is the constants for "space aliens" code.py


# PyBadge screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
TOTAL_NUMBER_OF_ALIENS = 5
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "Just Pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
    "button_a": False,
    "button_b": False
}

# new pallet for red filled text
RED_PALETTE = (
    b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
)
