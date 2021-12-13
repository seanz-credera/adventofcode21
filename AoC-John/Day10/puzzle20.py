import math

CHAR_MAP = {"<": ">", "{": "}", "[": "]", "(": ")"}
VAL_MAP = {")": 1, "]": 2, "}": 3, ">": 4}


def is_open(char):
    return char == "[" or char == "{" or char == "<" or char == "("


def is_close(char):
    return char == "]" or char == "}" or char == ">" or char == ")"


def is_match(char1, char2):
    return (
        (char1 == "[" and char2 == "]")
        or (char1 == "{" and char2 == "}")
        or (char1 == "<" and char2 == ">")
        or (char1 == "(" and char2 == ")")
    )


with open("day10.txt") as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    incomplete = []
    for line in file_content:
        stack = []
        is_corrupt = False
        for char in line:
            if is_open(char):
                stack.append(char)
            if is_close(char):
                if len(stack) > 0:
                    last_char = stack.pop()
                    if not is_match(last_char, char):
                        is_corrupt = True
                        break
                else:
                    print("No characters to close.")
        if not is_corrupt:
            complete_str = ""
            while len(stack) > 0:
                bracket = stack.pop()
                complete_str += CHAR_MAP[bracket]
            incomplete.append(complete_str)

    total_scores = []
    for chars in incomplete:
        total = 0
        for char in chars:
            total = (total * 5) + VAL_MAP[char]
        total_scores.append(total)

    total_scores.sort()

    print(f"Middle score: {total_scores[math.floor(len(total_scores) / 2)]}")
