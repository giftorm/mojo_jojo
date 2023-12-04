import time
start_time = time.time()
from resources.input_1 import input

numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def try_find_number(combination_of_letters_and_numbers: str, first=0, last=0):
    def iterate(findings, first, last):
        if first == last:
            if first > len(combination_of_letters_and_numbers):
                return findings
            try:
                number = int(combination_of_letters_and_numbers[first])
                findings.append(number)
                # move cursor to the right 
                first+=1
                return iterate(findings, first, first)
            except:
                pass

        finding = numbers_dict.get(f"{combination_of_letters_and_numbers[first:last]}",None)
        if finding is None:
            if last >= first+5:
                first = first + 1
                last = first
            elif last >= len(combination_of_letters_and_numbers):
                first = first + 1
                last = first
            else:
                last+=1
            return iterate(findings, first=first, last=last)
        else:
            findings.append(finding)
            first = last-1
            return iterate(findings, first=first, last=first)

    return iterate([], first, last)

def main():
    res = 0
    for i in input.split("\n"):
        if i == "":
            continue
        x = try_find_number(i)
        first_and_last_number=f"{x[0]}{x[-1]}"
        if x and len(x):
            res += int(first_and_last_number)
    print(res)

main()
print("--- %s seconds ---" % (time.time() - start_time))
