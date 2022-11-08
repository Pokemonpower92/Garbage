import os

GRAPHICS_PATH = os.path.abspath("resources/graphics")

# Menu resources
BACKGROUNDS = os.path.abspath("resources/graphics/menus/backgrounds")

## Button Sprites.
TITLE_SCREEN_BUTTONS = None
MAIN_MENU_BUTTONS = None
PAUSE_MENU_BUTTONS = None

TITLE_SCREEN_BUTTON_LAYOUT = None
MAIN_MENU_BUTTON_LAYOUT = None
PAUSE_MENU_BUTTON_LAYOUT = None

## Text Sprites.
TITLE_SCREEN_TEXT = None
MAIN_MENU_TEXT = None
PAUSE_MENU_TEXT = None

TITLE_SCREEN_TEXT_LAYOUT = None
MAIN_MENU_TEXT_LAYOUT = None
PAUSE_MENU_TEXT_LAYOUT = None

# Tilesets
FLOOR_TILES = os.path.abspath("resources/graphics/floors")
WALL_TILES = os.path.abspath("resources/graphics/walls")
CAT_TILES = os.path.abspath("resources/graphics/enemies/cat")
CAT_START = CAT_TILES + "/down/down_0.png"

LEVEL_DATA_PATH = os.path.abspath("resources/levels")
LEVEL_0_DATA = os.path.abspath("resources/levels/0")

TEST_PLAYER = GRAPHICS_PATH + "/test/down_0.png"
TEST_ROCK = GRAPHICS_PATH + "/test/rock.png"


# Player animations
PLAYER_MAGE_ANIMATIONS = GRAPHICS_PATH + "/player/mage"
