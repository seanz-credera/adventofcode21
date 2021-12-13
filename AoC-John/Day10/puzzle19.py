CHAR_MAP = {"<": ">", "{": "}", "[": "]", "(": ")"}


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


def get_value(char):
    if char == ")":
        return 3
    if char == "]":
        return 57
    if char == "}":
        return 1197
    else:
        return 25137


with open("day10.txt") as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    total = 0
    for line in file_content:
        stack = []
        for char in line:
            if is_open(char):
                stack.append(char)
            if is_close(char):
                if len(stack) > 0:
                    last_char = stack.pop()
                    if not is_match(last_char, char):
                        print(
                            f"Expected {CHAR_MAP[last_char]}, but found {char} instead."
                        )
                        total += get_value(char)
                        break

    print(f"Total: {total}")
