import string

INPUT = "inp"
MULTIPLY = "mul"
ADD = "add"
DIVIDE = "div"
EQUALS = "eql"
MOD = "mod"

global w
global x
global y
global z


def perform_action(instruction, vals, inp_count, monad):
    global w, x, y, z
    if instruction == INPUT:
        op = f"{vals[0]} = {int(str(monad)[inp_count])}"
        inp_count += 1
    else:
        var1 = vals[0]
        var2 = vals[1]
        if instruction == ADD:
            op = f"{var1} = {var1} + {var2}"
        elif instruction == DIVIDE:
            op = f"{var1} = int({var1} / {var2})"
        elif instruction == MULTIPLY:
            op = f"{var1} = {var1} * {var2}"
        elif instruction == MOD:
            op = f"{var1} = {var1} % {var2}"
        elif instruction == EQUALS:
            op = f"{var1} = int({var1} == {var2})"

    exec(op, globals())
    return inp_count


filename = "day24.txt"
debug = "AoC-John/Day24/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]

    max_valid = 0
    for num in range(99999999999999, 10000000000000, -1):
        if "0" not in str(num):
            inp_count = 0
            w, x, y, z = 0, 0, 0, 0
            for line in file_content:
                line = line.split()
                instruction = line[0]
                inp_count = perform_action(instruction, line[1:], inp_count, num)
        if z == 0 and "0" not in str(num):
            max_valid = num
            break

print(f"Max valid num for MONAD is {max_valid}")
