from resources.input_1 import input

import sys
from typing import List


def str_rows_to_array(text: str) -> List[str]:
    # We will remove empty lines
    return list(filter(lambda x: x != "", text.split("\n")))

def first_and_last_int(text: str) -> int:
    integers = []
    for i in text:
        try:
            integers.append(int(i))
        except:
            pass
    if len(integers):
        return int("".join([str(integers[0]), str(integers[-1])]))
    return 0

def first(input: List[str]) -> int:
    def append(str_list: List[str], curr: int = 0):
        if len(str_list):
            curr += first_and_last_int(str_list.pop())
            return append(str_list, curr)
        else:
            return curr

    return append(input)

#inp = input
inp = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

res = inp.replace("two", "2")
res = res.replace("one", "1")
res = res.replace("nine", "9")
res = res.replace("eight", "8")
res = res.replace("three", "3")
res = res.replace("four", "4")
res = res.replace("five", "5")
res = res.replace("six", "6")
res = res.replace("seven", "7")
res = str_rows_to_array(res)

print(res)

list1 = res[:len(res)//2]
list2 = res[len(res)//2:]
print(first(list1)+first(list2))

