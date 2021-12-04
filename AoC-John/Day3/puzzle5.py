import math

filename = "day3.txt"
with open(filename) as file:
    bit_strings = file.readlines()
    bit_strings = [bits.strip() for bits in bit_strings]
    total_bit_strings = len(bit_strings)
    bit_counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
    }
    for bits in bit_strings:
        for i in range(len(bits)):
            if bits[i] == "1":
                bit_counts[i] += 1
    gamma_string = ""
    epsilon_string = ""
    for key, value in bit_counts.items():
        if value > math.ceil(total_bit_strings / 2.0):
            gamma_string += "1"
            epsilon_string += "0"
        else:
            gamma_string += "0"
            epsilon_string += "1"
    print(f"Gamma: {gamma_string}, {int(gamma_string, 2)}")
    print(f"Epsilon: {epsilon_string}, {int(epsilon_string, 2)}")
    print(f"Power consumption: {int(gamma_string, 2) * int(epsilon_string, 2)}")
