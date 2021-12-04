filename = "puzzle_1.txt"
filename2 = "puzzle_1_example.txt"

with open(filename) as f:
    nums = f.readlines()
    nums = [int(num.strip()) for num in nums]
    prev = None
    increase_count = 0
    for num in nums:
        if prev is None:
            prev = num
        if num > prev:
            increase_count += 1
        prev = num

print(increase_count)
