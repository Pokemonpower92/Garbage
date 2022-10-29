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
                "font": (None, 75),
                "text": "New Game",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
            },
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 320),
                "dimensions": (700, 200),
                "type": "text",
                "font": (None, 75),
                "text": "Load Game",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
            },
            {
                "position": (game_constants.WINDOW_DIMENSIONS[0] // 2, 530),
                "dimensions": (700, 200),
                "type": "text",
                "font": (None, 75),
                "text": "Options",
                "text_color": (255, 255, 255),
                "color": (0, 0, 55),
            },
        ],
    },
}
