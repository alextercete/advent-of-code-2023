import fileinput
from functools import reduce
import re

AVAILABLE = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def possible_game(available: dict, revealed: dict):
    for color, amount in available.items():
        if color in revealed and revealed[color] > amount:
            return False
    return True

def minimum_set(revealed_sets: list):
    minimum = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for set in revealed_sets:
        for color in minimum:
            existing = minimum[color]
            new = set[color] if color in set else 0
            minimum[color] = max(existing, new)
    return minimum

def power(set: dict):
    return reduce(lambda x, y: x*y, set.values())

def parse_line(line: str):
    line_match = re.match(r"^Game (\d+):(.*?)$", line)
    id = int(line_match.group(1))
    revealed_sets = []
    for set in line_match.group(2).split(";"):
        parsed_set = {}
        for item_match in re.finditer(r"(\d+)\s(red|green|blue)", set):
            parsed_set[item_match.group(2)] = int(item_match.group(1))
        revealed_sets.append(parsed_set)
    return id, revealed_sets

if __name__ == "__main__":
    total = 0
    for line in fileinput.input():
        _, revealed_sets = parse_line(line)
        minimum = minimum_set(revealed_sets)
        total += power(minimum)
    print(total)
