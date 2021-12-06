import copy


def main():
    with open("day6.txt") as file:
        file_content = file.readlines()
        file_content = [line.strip() for line in file_content]
        file_string = file_content[0].split(",")
        nums = [int(num) for num in file_string]
        num_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for num in nums:
            num_fish[num] += 1
        print(num_fish)
        num_days = 256
        for i in range(num_days):
            old_num_fish = copy.deepcopy(num_fish)
            num_fish[0] = old_num_fish[1]
            num_fish[1] = old_num_fish[2]
            num_fish[2] = old_num_fish[3]
            num_fish[3] = old_num_fish[4]
            num_fish[4] = old_num_fish[5]
            num_fish[5] = old_num_fish[6]
            num_fish[6] = old_num_fish[0] + old_num_fish[7]
            num_fish[7] = old_num_fish[8]
            num_fish[8] = old_num_fish[0]
        print(num_fish)
        total = 0
        for value in num_fish.values():
            total += value
        print(total)


if __name__ == "__main__":
    main()
