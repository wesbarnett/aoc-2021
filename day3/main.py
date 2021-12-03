from pathlib import Path

lines = Path("./input").read_text().rstrip("\n").split("\n")
lines = [list(x) for x in lines]
lines = [[int(y) for y in x] for x in lines]

n = len(lines)

gamma = [str(int(sum([x[i] for x in lines]) / n >= 0.5)) for i in range(len(lines[0]))]
epsilon = [str(int(sum([x[i] for x in lines]) / n < 0.5)) for i in range(len(lines[0]))]

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma*epsilon)
