from typing import Dict
from typing import List
from typing import Tuple

import numpy as np
from numpy import nan

import re


class Tile(object):
    def __init__(self, id_: int, pixels: np.array):
        self.id = id_
        self.pixels = pixels
        self.matches = [nan] * 4  # [up right down left]
        self.is_locked = False

    def __repr__(self):
        return f"tile ID: {self.id}"

    def rotate(self):
        """A method that rotates the pixels to the left."""
        self.pixels = np.rot90(self.pixels)

    def flipud(self):
        """A method that flips the pixels up-down."""
        self.pixels = np.flipud(self.pixels)

    def fliplr(self):
        """A method that flips the pixels left-right."""
        self.pixels = np.fliplr(self.pixels)


def parse_data(data: list) -> Dict[int, Tile]:
    tiles: Dict[int, Tile] = {}
    for d in data:
        header = d[0]
        tile_id = int(re.findall("[0-9]+", header)[0])
        pic = d[1:]
        pic = np.array([[0 if el == "." else 1 for el in p] for p in pic], int)
        tiles[tile_id] = Tile(tile_id, pic)
    return tiles


def get_data(fn: str) -> Dict[int, Tile]:
    raw = open(fn).read().split("\n\n")
    data = [x.split("\n") for x in raw]
    tiles = parse_data(data)
    return tiles


fn = "./data/test_data20.txt"
tiles = get_data(fn)
print(tiles)
