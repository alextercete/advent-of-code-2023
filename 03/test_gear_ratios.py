from gear_ratios import parse_engine_schematics, part_numbers, gear_ratios

def test_single_digit_part_numbers():
    numbers = {
        (0, 0): 2,
        (3, 0): 5,
        (6, 0): 8
    }
    symbols = [
        (1, 0),
        (5, 0)
    ]
    assert part_numbers(numbers, symbols) == [2, 8]

def test_multiple_digit_part_numbers():
    numbers = {
        (0, 0): 12,
        (4, 0): 345,
        (9, 0): 6
    }
    symbols = [
        (2, 0),
        (7, 1)
    ]
    assert part_numbers(numbers, symbols) == [12, 345]

def test_gear_ratios_horizontal():
    numbers = {
        (0, 0): 12,
        (3, 0): 345,
        (9, 0): 6
    }
    symbols = {
        (2, 0): "*",
        (7, 1): "*"
    }
    assert gear_ratios(numbers, symbols) == [
        12*345
    ]

def test_gear_ratios_vertical():
    numbers = {
        (0, 0): 12,
        (0, 2): 345,
        (0, 5): 6
    }
    symbols = {
        (0, 1): "*",
        (0, 6): "*"
    }
    assert gear_ratios(numbers, symbols) == [
        12*345
    ]

def test_parse_engine_schematics():
    lines = [
        "123..*45\n",
        ".$.67..8\n"
    ]
    numbers, symbols = parse_engine_schematics(lines)
    assert numbers == {
        (0, 0): 123,
        (6, 0): 45,
        (3, 1): 67,
        (7, 1): 8
    }
    assert symbols == {
        (5, 0): "*",
        (1, 1): "$"
    }
