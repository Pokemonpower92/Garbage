from csv import reader


def import_layout_from_csv(layout_path):
    """Import a layout object from a csv file."""
    layout_map = []

    with open(layout_path) as map:
        layout = reader(map, delimiter=",")
        for row in layout:
            layout_map.append(list(row))

    return layout_map
