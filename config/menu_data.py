from config import game_constants, resource_paths
from utils import data_management

TITLE_SCREEN_RESOURCE_PATHS = {}
TITLE_SCREEN = {
    "background_path": resource_paths.BACKGROUNDS + "/title_screen.png",
    "sprites": {
        "text": [
            {
                "position": (0, 0),
                "dimensions": (50, 50),
                "font": (None, 75),
                "text": "Press 'Enter'",
                "color": (255, 255, 255),
            }
        ]
    },
}

MAIN_MENU_PATHS = {}
MAIN_MENU = {
    "background_path": resource_paths.BACKGROUNDS + "/title_screen.png",
    "sprites": {
        "text": [],
        "button": [
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 110),
                "dimensions": (700, 200),
                "type": "text",
                "name": "new_game_button",
                "font": (None, 75),
                "text": "New Game",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
                "hover_text_color": (0, 0, 55),
                "hover_color": (255, 255, 255),
                "border_radius": 12,
            },
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 320),
                "dimensions": (700, 200),
                "type": "text",
                "name": "load_game_button",
                "font": (None, 75),
                "text": "Load Game",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
                "hover_text_color": (0, 0, 55),
                "hover_color": (255, 255, 255),
                "border_radius": 12,
            },
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 530),
                "dimensions": (700, 200),
                "type": "text",
                "name": "options_button",
                "font": (None, 75),
                "text": "Options",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
                "hover_text_color": (0, 0, 55),
                "hover_color": (255, 255, 255),
                "border_radius": 12,
            },
        ],
    },
}

PAUSE_MENU_PATHS = {}
PAUSE_MENU = {
    "background_path": resource_paths.BACKGROUNDS + "/title_screen.png",
    "sprites": {
        "text": [],
        "button": [
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 60),
                "dimensions": (480, 100),
                "type": "text",
                "name": "new_game_button",
                "font": (None, 75),
                "text": "New Game",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
                "hover_text_color": (0, 0, 55),
                "hover_color": (255, 255, 255),
                "border_radius": 12,
            },
            {
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
            },
            {
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
            },
            {
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
            },
            {
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
            },
            {
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
            },
        ],
    },
}
