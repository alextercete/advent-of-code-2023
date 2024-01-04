from cube_conundrum import minimum_set, possible_game, parse_line, power

def test_possible_game():
    available = {
        "red": 3,
        "green": 4,
        "blue": 5
    }
    revealed = {
        "red": 2,
        "green": 3,
        "blue": 4
    }
    assert possible_game(available, revealed) == True

def test_possible_game_revealed_subset():
    available = {
        "red": 3,
        "green": 4,
        "blue": 5
    }
    revealed = {
        "red": 2,
    }
    assert possible_game(available, revealed) == True

def test_not_enough_red():
    available = {
        "red": 3,
        "green": 4,
        "blue": 5
    }
    revealed = {
        "red": 4,
        "green": 3,
        "blue": 4
    }
    assert possible_game(available, revealed) == False

def test_minimum_set():
    revealed_sets = [
        {
            "red": 3,
            "green": 2,
            "blue": 1
        },
        {
            "green": 4
        },
        {
            "blue": 5
        }
    ]
    minimum = minimum_set(revealed_sets)
    assert minimum == {
        "red": 3,
        "green": 4,
        "blue": 5
    }

def test_power():
    set = {
        "red": 3,
        "green": 4,
        "blue": 5
    }
    assert power(set) == 60

def test_parse_line():
    line = "Game 39: 7 green, 7 blue, 2 red; 11 blue, 4 green, 8 red"
    id, revealed_sets = parse_line(line)
    assert id == 39
    assert revealed_sets == [
        {
            "green": 7,
            "blue": 7,
            "red": 2
        },
        {
            "blue": 11,
            "green": 4,
            "red": 8
        }
    ]
