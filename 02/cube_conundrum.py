import fileinput
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
        id, revealed_sets = parse_line(line)
        if all([possible_game(AVAILABLE, s) for s in revealed_sets]):
            total += id
    print(total)
