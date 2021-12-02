from pathlib import Path

nums = [int(x) for x in Path("./input").read_text().rstrip().split("\n")]
count = sum(x2 > x1 for x1, x2 in zip(nums, nums[1:]))

print(count)

nums3 = [sum([x1, x2, x3]) for x1, x2, x3 in zip(nums, nums[1:], nums[2:])]
count = sum(x2 > x1 for x1, x2 in zip(nums3, nums3[1:]))

print(count)
