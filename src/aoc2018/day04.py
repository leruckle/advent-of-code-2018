"""
AOC 2018, day 04
https://adventofcode.com/2018/day/4
"""

from dataclasses import dataclass
import re
import numpy as np
import numpy.typing as npt
from typing import Dict, List, Optional

from aoc2018.utilities import read_input_file


@dataclass
class SleepInterval:
    """Data class for capturing guard sleep intervals."""
    guard_id: int
    start: int
    end: int


class InputParser:
    """Utility class for formatting puzzle input."""
    def __init__(self, raw_input: List[str]) -> None:
        self._sorted_raw_input = sorted(raw_input)
        self._formatted_input: Optional[Dict[int, npt.NDArray]] = None
        self._index = 0
        self._guard_id = -1

    def get_parsed_input(self) -> Dict[int, npt.NDArray]:
        """Returns the parsed puzzle input as guard sleep intervals."""
        if self._formatted_input is None:
            sleep_intervals = self._parse_sleep_intervals()
            self._formatted_input = self._make_sleep_matrices_from_sleep_intervals(sleep_intervals)
        return self._formatted_input

    def _parse_sleep_intervals(self) -> Dict[int, List['SleepInterval']]:
        """Parses puzzle input into guard sleep intervals."""
        to_return: Dict[int, List[SleepInterval]] = {}
        guard_start_regex_pattern = r'^.*Guard #(?P<guard_id>\d+).*'
        while self._index < len(self._sorted_raw_input):
            line = self._sorted_raw_input[self._index]
            guard_shift_start_match = re.search(guard_start_regex_pattern, line)
            if guard_shift_start_match is not None:
                self._guard_id = self._parse_guard_id(guard_shift_start_match)
                self._index = self._index + 1
            else:
                sleep_interval = self._parse_sleep_event()
                self._index = self._index + 2
                if self._guard_id not in to_return:
                    to_return[self._guard_id] = []
                to_return[self._guard_id].append(sleep_interval)
        return to_return

    def _make_sleep_matrices_from_sleep_intervals(self,
        guard_sleep_intervals: Dict[int, List['SleepInterval']]
    ) -> Dict[int, npt.NDArray]:
        to_return = {}
        for guard, sleep_intervals in guard_sleep_intervals.items():
            sleep_array = np.zeros((len(sleep_intervals), 60))
            for i, interval in enumerate(sleep_intervals):
                sleep_array[i, interval.start:interval.end] = 1
            to_return[guard] = sleep_array
        return to_return

    def _parse_guard_id(self, guard_shift_start_match) -> int:
        to_return = int(guard_shift_start_match.group('guard_id'))
        return to_return

    def _parse_sleep_event(self) -> 'SleepInterval':
        start_line = self._sorted_raw_input[self._index]
        start_time = self._parse_sleep_event_time(start_line)
        end_line = self._sorted_raw_input[self._index + 1]
        end_time = self._parse_sleep_event_time(end_line)
        to_return = SleepInterval(self._guard_id, start_time, end_time)
        return to_return

    def _parse_sleep_event_time(self, line: str) -> int:
        sleep_event_regex_pattern = r'^\[\d{4}-\d{2}-\d{2} 00\:(?P<time>\d{2})\] (?P<action>[\w\s]*)$'
        sleep_event_match = re.search(sleep_event_regex_pattern, line)
        if not sleep_event_match:
            raise Exception(f"Line is not a sleep event: {line}")
        action = sleep_event_match.group('action').strip()
        if action not in ['falls asleep', 'wakes up']:
            raise Exception(f"Unrecognized sleep event: {action}")
        time_str = sleep_event_match.group('time')
        time = int(time_str)
        return time


class Day04PuzzleSolver:
    """Solver class for Day 04 Puzzle"""

    def __init__(self, raw_input: List[str]) -> None:
        self._raw_input = raw_input
        self._guard_sleep_data: Optional[Dict[int, npt.NDArray]] = None

    @property
    def guard_sleep_data(self) -> Dict[int, npt.NDArray]:
        """Parsed and formatted puzzle input data."""
        if self._guard_sleep_data is None:
            parser = InputParser(self._raw_input)
            self._guard_sleep_data = parser.get_parsed_input()
        return self._guard_sleep_data

    def part_1(self) -> int:
        """Solution for part 1 of the puzzle."""       
        sleepiest_guard = self._find_sleepiest_guard()
        sleepiest_minute = self._find_sleepiest_minute_of_guard(sleepiest_guard)
        to_return = sleepiest_guard * sleepiest_minute
        return int(to_return)

    def _find_sleepiest_guard(self):
        max_sleep_guard_id: int = -1
        max_sleep_sum: float = 0
        for guard_id in self.guard_sleep_data:
            sleep_sum = np.sum(self.guard_sleep_data[guard_id])
            if sleep_sum > max_sleep_sum:
                max_sleep_guard_id = guard_id
                max_sleep_sum = sleep_sum
        return max_sleep_guard_id

    def _find_sleepiest_minute_of_guard(self, guard_id: int) -> int:
        sleep_data = self.guard_sleep_data[guard_id]
        minute_sums = sleep_data.sum(axis=0)
        sleepiest_minute = np.argmax(minute_sums)
        return int(sleepiest_minute)



if __name__ == '__main__':
    raw_puzzle_input = read_input_file("day04.txt")
    solver = Day04PuzzleSolver(raw_puzzle_input)
    part_1_answer = solver.part_1()
    print(f"part 1 answer: {part_1_answer}")

    # part_2_answer: int = part_2(input)
    # print(f"part 2 answer: {part_2_answer}")