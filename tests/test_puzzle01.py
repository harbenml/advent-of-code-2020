from puzzles.puzzle01 import solve_part_1
from puzzles.puzzle01 import solve_part_2

import numpy as np
import pandas as pd

data = pd.read_csv("./data/data01.txt").values


def test_solve_part_1():
    assert solve_part_1(data) == 970816


def test_solve_part_2():
    assert solve_part_2(data) == 96047280
