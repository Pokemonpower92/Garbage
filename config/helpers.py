"""Helpers to load data into config files."""
import os
from typing import Dict


def build_animation_set(path: str) -> Dict:

    new_set = {}

    for action in os.listdir(path):
        for direction in os.listdir(os.path.join(path, action)):
            absolute_path = os.path.join(path, action, direction)
            files = [os.path.join(absolute_path, x) for x in os.listdir(absolute_path)]

            if action not in new_set:
                new_set[action] = {}

            new_set[action][direction] = files

    return new_set
