"""This file contains the json data associated with pause menu buttons"""
from commands.run_loop_command import RunLoopCommand
from commands.temp_command import TempCommand
from config import game_constants


LOAD_GAME_BUTTON = {
    "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 170),
    "dimensions": (480, 100),
    "type": "text",
    "name": "load_game_button",
    "font": (None, 75),
    "text": "Load Game",
    "text_color": (255, 255, 255),
    "color": (0, 0, 55),
    "hover_text_color": (0, 0, 55),
    "hover_color": (255, 255, 255),
    "border_radius": 12,
    "command": TempCommand
}

OPTIONS_BUTTON = {
    "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 280),
    "dimensions": (480, 100),
    "type": "text",
    "name": "options_button",
    "font": (None, 75),
    "text": "Options",
    "text_color": (255, 255, 255),
    "color": (0, 0, 55),
    "hover_text_color": (0, 0, 55),
    "hover_color": (255, 255, 255),
    "border_radius": 12,
    "command": TempCommand
}

CHARACTER_SCREEN_BUTTON = {
    "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 390),
    "dimensions": (480, 100),
    "type": "text",
    "name": "character_screen_button",
    "font": (None, 75),
    "text": "Character Screen",
    "text_color": (255, 255, 255),
    "color": (0, 0, 55),
    "hover_text_color": (0, 0, 55),
    "hover_color": (255, 255, 255),
    "border_radius": 12,
    "command": TempCommand
}

SAVE_GAME_BUTTON = {
    "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 500),
    "dimensions": (480, 100),
    "type": "text",
    "name": "save_game_button",
    "font": (None, 75),
    "text": "Save Game",
    "text_color": (255, 255, 255),
    "color": (0, 0, 55),
    "hover_text_color": (0, 0, 55),
    "hover_color": (255, 255, 255),
    "border_radius": 12,
    "command": TempCommand
}

EXIT_GAME_BUTTON = {
    "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 610),
    "dimensions": (480, 100),
    "type": "text",
    "name": "exit_game_button",
    "font": (None, 75),
    "text": "Exit Game",
    "text_color": (255, 255, 255),
    "color": (0, 0, 55),
    "hover_text_color": (0, 0, 55),
    "hover_color": (255, 255, 255),
    "border_radius": 12,
    "command": TempCommand
}
