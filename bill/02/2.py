from dataclasses import dataclass
import re
from typing import List
from input import input





def input_adapter(input):
    game_input = []
    for i in input.split("\n"):
        id = re.search("Game (\\d+)", i) #|(\\d+ blue|\\d+ green|\\d+ red)", i)
        game = {"id": int(id[0].split("Game ")[-1]),
                "games": []
                }
        for j in i.split(";"):
            red = re.search("(\\d+) red", j)
            blue = re.search("(\\d+) blue", j)
            green = re.search("(\\d+) green", j)
            game["games"].append({ 
                "red": int(red.groups()[0]) if red else 0,
                "blue": int(blue.groups()[0]) if blue else 0,
                "green": int(green.groups()[0]) if green else 0,
            })
        game_input.append(game)
    return game_input

class GamePartOne:

    @dataclass(frozen=True)
    class Rules:
        red: int
        green: int
        blue: int

    def __init__(self):
        self._rules = GamePartOne.Rules(red=12, green=13, blue=14)

    def play(self, red: int = 0, green: int = 0, blue: int = 0) -> bool:
        return self._rules.red >= red \
                and self._rules.green >= green \
                and self._rules.blue >= blue

    def run_test(self):
        expected_result = 8
        game_input = input_adapter(GamePartOne.test_input)
        res = 0
        for i in game_input:
            win = True
            for g in i["games"]:
                if not self.play(**g):
                    win = False
            if win:
                res += int(i["id"])
        assert expected_result == res


class GamePartTwo:
    # Take some input
    # Every input "row" find the lowest amount of red, blue and green and multiply them
    # add the result from every row

    def play(self):
        pass

def get_lowest(input: List[int], current = None) -> int:
    for i in input:
        i = int(i)
        if current is None:
            current = i
        elif i > current:
            current = i
    return str(current)


def line_adapter(line_of_game_info: str) -> List[int]:
    red_findings = re.findall("(\\d+) red", line_of_game_info)
    blue_findings = re.findall("(\\d+) blue", line_of_game_info)
    green_findings = re.findall("(\\d+) green", line_of_game_info)
    return [get_lowest(red_findings), get_lowest(blue_findings), get_lowest(green_findings)]


def game(input: List[str], val=0):
    curr = input.pop() if len(input) else None
    if curr is None:
        return val
    res = line_adapter(curr)
    val += eval("*".join(res))
    return game(input, val) 


test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input = input.split("\n")

print(game(input))

