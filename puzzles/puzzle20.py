import re
import copy

from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Tuple
from typing import Union

import numpy as np  # type: ignore
from numpy import nan  # type: ignore

import plotly.express as px  # type: ignore


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

    def check_right_edge(self, t: Any):
        edge = self.pixels[:, -1]
        if np.all(edge == t.pixels[:, 0]):
            self.matches[1] = t.id
            t.matches[3] = self.id
            return True
        return False

    def check_down_edge(self, t: Any):
        edge = self.pixels[-1, :]
        if np.all(edge == t.pixels[0, :]):
            self.matches[2] = t.id
            t.matches[0] = self.id
            return True
        return False

    def get_num_matches(self) -> int:
        return 4 - sum(np.isnan(self.matches))


class ImageRow(object):
    def __init__(self, ngrid: int):
        self.pixels: np.array = np.array([], int)
        self.tiles: List[Tile] = []
        self.ngrid = ngrid


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
    return current_tile, is_match


def get_next_tile(
    current_tile: Tile, tiles: Dict[int, Tile], check_down_instead_of_right: int = False
) -> Union[Tile, None]:
    tiles_dict = copy.deepcopy(tiles)
    for t in tiles_dict.values():
        if t.id == current_tile.id:
            continue
        t.flipud()
        for _ in range(4):  # rotation counter
            for flip in [False, True]:
                if check_down_instead_of_right:
                    is_match = current_tile.check_down_edge(t)
                else:
                    is_match = current_tile.check_right_edge(t)
                if is_match:
                    return t
                if flip:
                    t.flipud()
                else:
                    t.flipud()
                    t.rotate()
    return None


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


def find_corner(tiles: Dict[int, Tile]) -> Generator[Tile, None, None]:
    for tile in tiles.values():
        for _ in range(4):
            tile, _ = find_next_right_match(tile, tiles)
            num_matches = tile.get_num_matches()
            tile.rotate()
        num_matches = tile.get_num_matches()
        is_corner = check_for_corner(tile.matches)
        if num_matches == 2 and is_corner:
            print("corner found! id: ", tile.id)
            yield tile


def is_corner_rotation_correct(m: List) -> bool:
    if np.isnan(m[0]) and np.isnan(m[-1]):
        return True
    return False


def rotate_initial_corner(t: Tile) -> Tile:
    """
    Rotate the corner tile such that it has no matches to the left
    and to the top. I.e. tile.matches should look like:

         [nan, neighbor_id, neighbor_id, nan]
    i.e. [top, right,       bottom,      left]        

    """
    while not is_corner_rotation_correct(t.matches):
        t.rotate()
    return t


def create_image(tiles: Dict[int, Tile]) -> np.array:

    corner_gen = find_corner(tiles)
    corner = next(corner_gen)
    corner = rotate_initial_corner(corner)

    ngrid = int(np.sqrt(len(tiles)))
    img = create_empty_img(tiles, corner, ngrid)

    curr_tile = corner
    img = put_tile_in_image(img, corner, 0, 0)
    tiles_grid = {(0, 0): curr_tile}

    for row in range(ngrid):
        for col in range(ngrid):

            if row == 0 and col == 0:
                continue
            if col == 0 and row > 0:
                go_down = True
                curr_tile = tiles_grid[(row - 1, col)]  # go down
            else:
                go_down = False
                curr_tile = tiles_grid[(row, col - 1)]  # go right

            # get next tile
            next_tile = get_next_tile(curr_tile, tiles, go_down)

            # put tile in image
            if next_tile is not None:
                img = put_tile_in_image(img, next_tile, row, col)
            else:
                print("No next tile found!")
                break

            # store tile in grid
            tiles_grid[(row, col)] = next_tile

    return img


def create_empty_img(tiles: Dict[int, Tile], corner: Tile, ngrid: int) -> np.array:
    num_pixels = (len(corner.pixels) - 2) * ngrid
    img = np.empty(shape=(num_pixels, num_pixels))
    img[:] = np.nan
    return img


def put_tile_in_image(img: np.array, tile: Tile, row: int, col: int) -> np.array:
    pixels_to_install = tile.pixels[1:-1, 1:-1]
    npix = len(pixels_to_install)
    img[
        row * npix : (row + 1) * npix, col * npix : (col + 1) * npix
    ] = pixels_to_install
    return img


def get_monster_mask() -> np.array:
    with open("./data/data20_monster.txt") as f:
        monster = f.read().split("\n")
    mask = [[True if el == "#" else False for el in m] for m in monster]
    mask = np.array(mask, dtype=bool)
    return mask


def solve_part1(tiles: Dict[int, Tile]) -> int:
    result = 1
    corner = find_corner(tiles)
    for _ in range(4):
        tile = next(corner)
        result *= tile.id
    return result


if __name__ == "__main__":

    fn = "./data/test_data20.txt"
    tiles = get_data(fn)

    # result = solve_part1(tiles)
    # print("solution of part 1:", result)

    img = create_image(tiles)

    mask = get_monster_mask()

    # manipulate test image such that the monster is "visible"
    img = np.rot90(img)
    img = np.flipud(img)
    x = img[2:5, 2:22]
    xm = np.ma.masked_array(x, mask)
    print("is monster?:", sum(xm[xm.mask].data) == sum(mask[mask]))

    fig = px.imshow(img)
    fig.show()
