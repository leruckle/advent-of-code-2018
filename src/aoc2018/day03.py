"""
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
"""

from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
import re

from aoc2018 import read_input_file

@dataclass
class Claim:
    id_number: int 
    horizontal_coordinate: int
    vertical_coordinate: int 
    width: int
    height: int

    def get_horz_start_index(self) -> int:
        return self.horizontal_coordinate
    
    def get_horz_end_index(self) -> int:
        return self.horizontal_coordinate + self.width 
    
    def get_vert_start_index(self) -> int:
        return self.vertical_coordinate
    
    def get_vert_end_index(self) -> int:
        return self.vertical_coordinate + self.height

    def __eq__(self, __o: object) -> bool:
        if type(self) != type(__o):
            return False
        if self.__dict__ != __o.__dict__:
            return False 
        return True

class Grid:
    def __init__(self, 
        width: int,
        height: int
    ) -> 'Grid':
        self.grid: np.array = np.zeros((width, height), dtype=int)
    
    def get_grid_matrix(self) -> np.array:
        return self.grid
    
    def mark_out_claim(self, claim: Claim) -> None:
        self.grid[
            claim.get_horz_start_index():claim.get_horz_end_index(),
            claim.get_vert_start_index():claim.get_vert_end_index()
        ]+=1    # increment by one here
    
    def get_area_of_overlapped_claims(self) -> int:
        overlaps: np.array = self.grid > 1
        total: int = np.sum(overlaps)
        return total
    
    def is_overlaps_existing_claim(self, claim: Claim) -> bool:
        claim_selection: np.array = self.grid[
            claim.get_horz_start_index():claim.get_horz_end_index(),
            claim.get_vert_start_index():claim.get_vert_end_index()
        ]
        has_overlap: bool = np.any(claim_selection > 1)
        return has_overlap

    def __eq__(self, __o: object) -> bool:
        if type(self) != type(__o):
            return False
        if not np.all(np.equal(self.grid, __o.grid)):
            return False
        return True


def format_input(input: List[str]) -> List['Claim']: 
    to_return: List[Claim] = []
    regex_pattern: str = r'#(?P<id>\d+) @ (?P<horz_coord>\d+),(?P<vert_coord>\d+): (?P<width>\d+)x(?P<height>\d+)'
    for to_parse in input:
        match = re.search(regex_pattern, to_parse)
        if not match:
            raise Exception(f"Could not parse line: {to_parse}")
        claim = Claim(
            int(match.group('id')),
            int(match.group('horz_coord')),
            int(match.group('vert_coord')),
            int(match.group('width')),
            int(match.group('height'))
        )
        to_return.append(claim)
    return to_return

def calculate_necessary_grid_dimensions(claims: List['Claim']) -> Tuple[int]:
    max_width: int = 0
    max_height:int = 0
    for claim in claims:
        if claim.get_horz_end_index() > max_width:
            max_width = claim.get_horz_end_index()
        if claim.get_vert_end_index() > max_height:
            max_height = claim.get_vert_end_index()
    return (max_width, max_height)

def part_1(input: List['Claim']) -> int:
    """How many square inches of fabric are within two or more claims?"""
    grid_dimensions: Tuple[float] = calculate_necessary_grid_dimensions(input)
    grid: 'Grid' = Grid(*grid_dimensions)
    for claim in input:
        grid.mark_out_claim(claim)
    total_overlap: int = grid.get_area_of_overlapped_claims()
    return total_overlap

"""
--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""
def part_2(input: List['Claim']) -> int:
    grid_dimensions: Tuple[float] = calculate_necessary_grid_dimensions(input)
    grid: 'Grid' = Grid(*grid_dimensions)
    for claim in input:
        grid.mark_out_claim(claim)
    for claim in input:
        if not grid.is_overlaps_existing_claim(claim): 
            return claim.id_number
    raise Exception("Could not find non-overlapping claim")


if __name__ == '__main__':
    input = read_input_file('day03.txt')
    input = format_input(input)
    part_1_answer: int = part_1(input)
    print(f"part 1 answer: {part_1_answer}")

    part_2_answer: int = part_2(input)
    print(f"part 2 answer: {part_2_answer}")