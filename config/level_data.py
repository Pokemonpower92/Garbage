from config import resource_paths
from utils import data_management

LEVEL_0_IMAGE_PATHS = {
    "walls": resource_paths.WALL_TILES + "/0/",
    "enemies": {"0": resource_paths.CAT_START},
}
LEVEL_0 = {
    "floor_path": resource_paths.FLOOR_TILES + "/level_0.png",
    "graphics_paths": LEVEL_0_IMAGE_PATHS,
    "tiles": {
        "wall": data_management.import_layout_from_csv(
            resource_paths.LEVEL_0_DATA + "/0_walls.csv"
        ),
        "enemy": data_management.import_layout_from_csv(
            resource_paths.LEVEL_0_DATA + "/0_enemies.csv"
        ),
    },
}
