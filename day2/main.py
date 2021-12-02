from pathlib import Path

position = 0
depth = 0

lines = Path("./input").read_text().rstrip().split("\n")

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
