import re
from typing import List, LiteralString
from input import input

def line_adapter(game_info: str) -> List[str]:
    r = re.findall(r'(\d+) r', game_info)
    b = re.findall(r'(\d+) b', game_info)
    g = re.findall(r'(\d+) g', game_info)
    return [str(max([int(i) for i in r])), str(max([int(i) for i in b])), str(max([int(i) for i in g]))]

def game(input: List[LiteralString], val=0):
    curr = input.pop() if len(input) else None
    if curr is None:
        return val
    val += eval("*".join(line_adapter(curr)))
    return game(input, val) 

print(game(input.split("\n"), 0))

