# Window settings.
WINDOW_TITLE = "Garbage"
WINDOW_DIMENSIONS = (1024, 768)

# Tile settings.
TILE_SIZE = 64
NUM_TILES_WIDE = WINDOW_DIMENSIONS[0] // TILE_SIZE  # 32
NUM_TILES_HIGH = WINDOW_DIMENSIONS[1] // TILE_SIZE  # 24

# Colors for safe mode.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREY = (40, 40, 40)
LIGHT_GREY = (150, 150, 150)

PLAYER_COLOR = GREEN
ENEMY_COLOR = RED
WALL_COLOR = YELLOW
BACKGROUND_COLOR = DARK_GREY
GRID_COLOR = LIGHT_GREY
PICKUP_COLOR = BLUE

PLAYER_START_X = 2 * TILE_SIZE
PLAYER_START_Y = 37 * TILE_SIZE

# Timing.
FPS = 60
ANIMATION_SPEED = 100
MENU_BUTTON_COOLDOWN = 200
