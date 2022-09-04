from config import resource_paths
from utils import data_management

LEVEL_0 = {
    "floor_path": resource_paths.FLOOR_TILES + "/level_0.png",
    "wall_path": resource_paths.WALL_TILES + "/0/",
    "tiles": {
        "wall": data_management.import_layout_from_csv(
            resource_paths.LEVEL_0_DATA + "/level_0_walls.csv"
        )
    },
}
