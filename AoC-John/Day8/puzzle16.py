# Get the digit that `letters` represents, return as a string
def get_digit(letters):
    # Unique digits
    if len(letters) == 2:
        return "1"
    elif len(letters) == 3:
        return "7"
    elif len(letters) == 4:
        return "4"
    elif len(letters) == 7:
        return "8"
    # Sort the letters so we can do string literal comparison
    sorted_letters = sorted(letters)
    # Length 5 digits: 2, 3, 5
    if len(letters) == 5:
        if sorted_letters == "bcdef":
            return "5"
        elif sorted_letters == "acdfg":
            return "2"
        else:
            return "3"
    # Length 6 digits: 0, 6, 9
    if len(letters) == 6:
        if sorted_letters == "abcdeg":
            return "0"
        elif sorted_letters == "bcdefg":
            return "6"
        else:
            return "9"


with open("day8example.txt") as file:
    file_content = file.readlines()
    total = 0
    for line in file_content:
        out_seq = line.split("|")[1].split()
        print(f"output sequence: {out_seq}")
        digs = (
            get_digit(out_seq[0])
            + get_digit(out_seq[1])
            + get_digit(out_seq[2])
            + get_digit(out_seq[3])
        )
        print(f"Digits: {digs}\n")
        total += int(digs)
    print(f"Final total: {total}")
