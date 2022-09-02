from config import constants, resource_paths

file_path = resource_paths.TILEMAP_PATH + "blank.tm"

with open(file_path, "w") as f:
    tilemap_line = "".join(["." for _ in range(constants.NUM_TILES_WIDE)]) + "\n"

    for _ in range(constants.NUM_TILES_HIGH):
        f.write(tilemap_line)
