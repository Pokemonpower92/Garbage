import os

GRAPHICS_PATH = os.path.abspath("resources/graphics")

# Menu resources
BACKGROUNDS = os.path.abspath("resources/graphics/menus/backgrounds")

# Buttons.
TITLE_SCREEN_BUTTONS = None
MAIN_MENU_BUTTONS = None
PAUSE_MENU_BUTTONS = None

# Text Sprites.
TITLE_SCREEN_TEXT = None
MAIN_MENU_TEXT = None
PAUSE_MENU_TEXT = None

# Tilesets
FLOOR_TILES = os.path.abspath("resources/graphics/floors")
WALL_TILES = os.path.abspath("resources/graphics/walls")
CAT_TILES = os.path.abspath("resources/graphics/enemies/cat")
CAT_START = CAT_TILES + "/down/down_0.png"

LEVEL_DATA_PATH = os.path.abspath("resources/levels")
LEVEL_0_DATA = os.path.abspath("resources/levels/0")

TEST_PLAYER = GRAPHICS_PATH + "/test/down_0.png"
TEST_ROCK = GRAPHICS_PATH + "/test/rock.png"
