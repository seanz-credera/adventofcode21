filename = "puzzle_1.txt"
filename2 = "puzzle_1_example.txt"

with open(filename2) as f:
    nums = f.readlines()
    nums = [int(num.strip()) for num in nums]
    windows = []
    for i in range(len(nums) - 2):
        windows.append(nums[i] + nums[i + 1] + nums[i + 2])
    prev = None
    increase_count = 0
    for window in windows:
        if prev is None:
            prev = window
        if window > prev:
            increase_count += 1
        prev = window

    print(increase_count)
