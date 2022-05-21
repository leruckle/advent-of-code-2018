import pytest

from aoc2018.day01 import part_1, part_2

@pytest.mark.parametrize('input, truth',
    [
        ([1, -2, 3, 1], 3),
        ([1, 1, 1],     3),
        ([1, 1, -2],    0),
        ([-1, -2, -3], -6)
    ]
)
def test_part_1(input, truth):
    value = part_1(input)
    assert value == truth 

@pytest.mark.parametrize('input, truth',
    [
        ([1, -2, 3, 1], 2),
        ([1, -1], 0),
        ([-6, 3, 8, 5, -6], 5),
        ([7, 7, -2, -7, -4], 14)
    ]
)
def test_part_2(input, truth):
    value = part_2(input)
    assert value == truth 
