import math


def get_fuel_consumption(pos, nums):
    total = 0
    for num in nums:
        total += abs(num - pos)
    return total


def main():
    with open("day7.txt") as file:
        file_content = file.readlines()
        file_content = [line.strip() for line in file_content]
        nums = file_content[0].split(",")
        nums = [int(num) for num in nums]
        min_val = nums[0]
        max_val = nums[0]
        min_fuel = math.inf
        for num in nums:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num
        for i in range(min_val, max_val + 1):
            fuel_cons = get_fuel_consumption(i, nums)
            if fuel_cons < min_fuel:
                min_fuel = fuel_cons
        print(f"Min fuel consumption: {min_fuel}")


if __name__ == "__main__":
    main()
