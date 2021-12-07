import math
import numpy as np


def triangular(num):
    return num * (num + 1) / 2


def get_fuel_consumption(pos, nums):
    total = 0
    for num in nums:
        total += triangular(abs(num - pos))
    return total


def main():
    with open("day7.txt") as file:
        file_content = file.readlines()
        file_content = [line.strip() for line in file_content]
        nums = file_content[0].split(",")
        nums = [int(num) for num in nums]
        print(
            f"Min fuel consumption: {int(get_fuel_consumption(math.floor(np.mean(nums)), nums))}"
        )


if __name__ == "__main__":
    main()
