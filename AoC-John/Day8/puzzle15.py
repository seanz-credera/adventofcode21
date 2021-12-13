with open("day8.txt") as file:
    file_content = file.readlines()
    count = 0
    for line in file_content:
        nums = line.split("|")[1].split()
        for num in nums:
            if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
                count += 1

    print(f"Total number of 1,4,7,8: {count}")
