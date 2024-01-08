import fileinput
from functools import reduce
import re

def part_numbers(numbers: dict, symbols: list):
    parts = []
    symbols_cache = set(symbols)
    for coordinates, number in numbers.items():
        for neighbor in neighbors(coordinates, len(str(number))):
            if neighbor in symbols_cache:
                parts.append(number)
    return parts

def gear_ratios(numbers: dict, symbols: dict):
    ratios = []
    numbers_cache = create_numbers_cache(numbers)
    gear_coordinates = [k for k, v in symbols.items() if v == "*"]
    for coordinates in gear_coordinates:
        parts = set()
        for neighbor in neighbors(coordinates):
            if neighbor in numbers_cache:
                parts.add(numbers_cache[neighbor])
        if len(parts) >= 2:
            ratios.append(reduce(lambda a, b: a*b, parts))
    return ratios

def create_numbers_cache(numbers: dict):
    cache = {}
    for coordinates, number in numbers.items():
        x, y = coordinates
        length = len(str(number))
        for i in range(x, x+length):
            cache[(i, y)] = number
    return cache

def neighbors(coordinates: tuple, length=1):
    x, y = coordinates
    for i in range(x-1, x+length+1):
        for j in range(y-1, y+2):
            if x <= i <= x+length-1 and j == y:
                continue
            yield (i, j)

def parse_engine_schematics(lines: list):
    numbers = {}
    symbols = {}
    for j, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            numbers[(m.start(), j)] = int(m.group(0))
        for m in re.finditer(r"[^.\d\s]", line):
            symbols[(m.start(), j)] = m.group(0)
    return numbers, symbols

if __name__ == "__main__":
    lines = fileinput.input()
    numbers, symbols = parse_engine_schematics(lines)
    ratios = gear_ratios(numbers, symbols)
    print(sum(ratios))
