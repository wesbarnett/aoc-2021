from pathlib import Path

lines = Path("./input").read_text().rstrip("\n").split("\n")
lines = [list(x) for x in lines]
lines = [[int(y) for y in x] for x in lines]

n = len(lines)

# Part 1
gamma = [str(int(sum([x[i] for x in lines]) / n >= 0.5)) for i in range(len(lines[0]))]
epsilon = [str(int(sum([x[i] for x in lines]) / n <= 0.5)) for i in range(len(lines[0]))]

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma*epsilon)

# Part 2
O_lines = list(lines)
CO2_lines = list(lines)

for i in range(len(lines[0])):
    if len(O_lines) > 1:
        most_common = int(sum([x[i] for x in O_lines]) / len(O_lines) >= 0.5)
        O_lines = list(filter(lambda x: most_common == x[i], O_lines))
    if len(CO2_lines) > 1:
        least_common = int(sum([x[i] for x in CO2_lines]) / len(CO2_lines) < 0.5)
        CO2_lines = list(filter(lambda x: least_common == x[i], CO2_lines))
    if len(O_lines) == 1:
        O_rating = int("".join([str(x) for x in O_lines[0]]), 2)
    if len(CO2_lines) == 1:
        CO2_rating = int("".join([str(x) for x in CO2_lines[0]]), 2)

print(O_rating*CO2_rating)
