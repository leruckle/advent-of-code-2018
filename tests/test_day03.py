from typing import Tuple
import pytest
import numpy as np

from aoc2018.day03 import calculate_necessary_grid_dimensions, format_input, part_1, part_2, Claim, Grid


@pytest.fixture
def example_input():
    input = [
        Claim(1, 1, 3, 4, 4),
        Claim(2, 3, 1, 4, 4),
        Claim(3, 5, 5, 2, 2)
    ]
    return input


def test_format_input():
    input = ['#123 @ 3,2: 5x4']
    value = format_input(input)
    truth = [Claim(123, 3, 2, 5, 4)]
    assert value == truth

def test_calculate_necessary_grid_dimensions(example_input):
    value: Tuple[int]= calculate_necessary_grid_dimensions(example_input)
    truth: Tuple[int] = (7, 7)
    assert value == truth

def test_Grid_mark_out_claim():
    grid: 'Grid' = Grid(5, 5)
    claim: 'Claim' = Claim(0, 1, 1, 2, 2)
    grid.mark_out_claim(claim)
    value: np.array = grid.get_grid_matrix()
    truth: np.array = np.zeros((5, 5), dtype=int)
    truth[1:3,1:3] = 1
    assert np.all(np.equal(value, truth))

def test_part_1(example_input):
    value: int = part_1(example_input)
    truth: int = 4
    assert value == truth

def test_part_2(example_input):
    value: int = part_2(example_input)
    truth: int = 3
    assert value == truth