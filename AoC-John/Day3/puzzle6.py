import math
import os

print(os.getcwd())
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
    # Count bits
    for bits in bit_strings:
        for i in range(len(bits)):
            if bits[i] == "1":
                bit_counts[i] += 1
    gamma_string = ""
    epsilon_string = ""
    # see which bits are most common in each position, add bits to gamma/epsilon accordingly
    for key, value in bit_counts.items():
        if value >= math.ceil(total_bit_strings / 2.0):
            gamma_string += "1"
            epsilon_string += "0"
        else:
            gamma_string += "0"
            epsilon_string += "1"
    done = False
    bit_strings_oxy = [bits for bits in bit_strings]
    bit_strings_co2 = [bits for bits in bit_strings]
    while True:
        # Most common
        for i in range(len(gamma_string)):
            for bits in bit_strings:
                if bits[i] != gamma_string[i] and not done:
                    while bits in bit_strings_oxy:
                        bit_strings_oxy.remove(bits)
                    if len(bit_strings_oxy) == 1:
                        done = True
        if done:
            break
    print(gamma_string)
    print(bit_strings_oxy)
    done = False
    while True:
        # Least common
        for i in range(len(epsilon_string)):
            for bits in bit_strings:
                if bits[i] != epsilon_string[i] and not done:
                    while bits in bit_strings_co2:
                        bit_strings_co2.remove(bits)
                    if len(bit_strings_co2) == 1:
                        done = True
        if done:
            break

    print(epsilon_string)
    print(bit_strings_co2)
    oxy = int(bit_strings_oxy[0], 2)
    co2 = int(bit_strings_co2[0], 2)
    print(f"oxy: {oxy}")
    print(f"co2: {co2}")
    print(f"Life support: {oxy * co2}")
