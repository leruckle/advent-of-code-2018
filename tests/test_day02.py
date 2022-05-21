import pytest

from aoc2018.day02 import part_1, part_2, BoxId

@pytest.mark.parametrize('input, truth',
    [
        ([BoxId("abcdef"), BoxId("bababc"), BoxId("abbcde"), BoxId("abcccd"), BoxId("aabcdd"), BoxId("abcdee"), BoxId("ababab")], 12),
    ]
)
def test_part_1(input, truth):
    value = part_1(input)
    assert value == truth 

@pytest.mark.parametrize('input, truth',
    [
        ([BoxId("abcde"), BoxId("fghij"), BoxId("klmno"), BoxId("pqrst"), BoxId("fguij"), BoxId("axcye"), BoxId("wvxyz")], "fgij"),
    ]
)
def test_part_2(input, truth):
    value = part_2(input)
    assert value == truth 