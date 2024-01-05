import fileinput
import re

def part_numbers(numbers: dict, symbols: list):
    parts = []
    symbols_cache = set(symbols)
    for coordinates, number in numbers.items():
        for neighbor in neighbors(coordinates, number):
            if neighbor in symbols_cache:
                parts.append(number)
    return parts

def neighbors(coordinates: tuple, number: int):
    x, y = coordinates
    length = len(str(number))
    for i in range(x-1, x+length+1):
        for j in range(y-1, y+2):
            if x <= i <= x+length-1 and j == y:
                continue
            yield (i, j)

def parse_engine_schematics(lines: list):
    numbers = {}
    symbols = []
    for j, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            numbers[(m.start(), j)] = int(m.group(0))
        for m in re.finditer(r"[^.\d\s]", line):
            symbols.append((m.start(), j))
    return numbers, symbols

if __name__ == "__main__":
    lines = fileinput.input()
    numbers, symbols = parse_engine_schematics(lines)
    parts = part_numbers(numbers, symbols)
    print(sum(parts))
