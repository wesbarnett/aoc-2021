from pathlib import Path

lines = Path("./input").read_text().rstrip().split("\n")

# Part 1
position = 0
depth = 0

for x in lines:
    cmd, amt = x.split(" ")
    amt = int(amt)
    if cmd == "forward":
        position += amt
    elif cmd == "down":
        depth += amt
    elif cmd == "up":
        depth -= amt

print(depth*position)

# Part 2
position = 0
depth = 0
aim = 0

for x in lines:
    cmd, amt = x.split(" ")
    amt = int(amt)
    if cmd == "down":
        aim += amt
    elif cmd == "up":
        aim -= amt
    elif cmd == "forward":
        position += amt
        depth += aim*amt

print(depth*position)
