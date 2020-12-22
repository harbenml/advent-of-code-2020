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

    def __repr__(self):
        return f"tile ID: {self.id}"

    def rotate(self):
        """A method that rotates the pixels to the left."""
        self.pixels = np.rot90(self.pixels)
        a = self.matches
        self.matches = a[1:] + [a[0]]

    def flipud(self):
        """A method that flips the pixels up-down."""
        self.pixels = np.flipud(self.pixels)
        a = self.matches
        self.matches = [a[2], a[1], a[0], a[3]]

    def fliplr(self):
        """A method that flips the pixels left-right."""
        self.pixels = np.fliplr(self.pixels)
        a = self.matches
        self.matches = [a[0], a[3], a[2], a[1]]

    def check_right_edge(self, t):
        edge = self.pixels[:, -1]
        if np.all(edge == t.pixels[:, 0]):
            # print("YEAH!", t.id)
            self.matches[1] = t.id
            t.matches[3] = self.id
            return True
        return False

    def get_num_matches(self) -> int:
        return 4 - sum(np.isnan(self.matches))


def find_next_right_match(current_tile: Tile, tiles: Dict[int, Tile]):
    for t in tiles.values():
        if t.id == current_tile.id:
            continue
        t.flipud()
        for _ in range(4):  # rotation counter
            for flip in [False, True]:
                is_match = current_tile.check_right_edge(t)

                if is_match:
                    break

                if flip:
                    t.flipud()
                else:
                    t.flipud()
                    t.rotate()

    # print("no match found.")
    return current_tile, is_match


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
    data = [x.strip().split("\n") for x in raw]
    tiles = parse_data(data)
    return tiles


def check_for_corner(m: list):
    """Check: edges must be neighbors"""
    x = np.argwhere(np.isnan(m))
    if (len(x) == 2) and (x[1][0] - x[0][0] == 1):
        return True
    return False


def solve_part1(tiles: Dict[int, Tile]) -> int:
    result = 1
    for tile in tiles.values():
        for _ in range(4):
            tile, is_match = find_next_right_match(tile, tiles)
            num_matches = tile.get_num_matches()
            tile.rotate()
        num_matches = tile.get_num_matches()
        is_corner = check_for_corner(tile.matches)
        if num_matches == 2 and is_corner:
            print("corner found! id: ", tile.id)
            result *= tile.id
    return result


if __name__ == "__main__":

    fn = "./data/test_data20.txt"
    tiles = get_data(fn)

    result = solve_part1(tiles)
    print("solution of part 1:", result)
