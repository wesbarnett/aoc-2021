from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def fold_horizontal(thermal_image, max_x, fold):
    for y in range(1, fold+1):
        for x in range(max_x+1):
            thermal_image[(x, fold-y)] += thermal_image[(x, fold+y)]
            if thermal_image[(x, fold-y)] > 0:
                thermal_image[(x, fold-y)] = 1
            del thermal_image[(x, fold+y)]


def fold_vertical(thermal_image, max_y, fold):
    for x in range(1, fold+1):
        for y in range(max_y+1):
            thermal_image[(fold-x, y)] += thermal_image[(fold+x, y)]
            if thermal_image[(fold-x, y)] > 0:
                thermal_image[(fold-x, y)] = 1
            del thermal_image[(fold+x, y)]


def print_image(thermal_image, max_x, max_y):
    image = [["." for x in range(max_x+1)] for y in range(max_y+1)]
    for (x, y), v in thermal_image.items():
        if v == 1:
            image[y][x] = "#"

    for row in image:
        print("".join(row))


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    instructions = []
    thermal_image = Counter()
    max_x = 0
    max_y = 0
    for line in lines:
        if line.startswith("fold along"):
            instructions.append(line)
        elif line:
            x, y = line.split(",")
            x, y = int(x), int(y)
            thermal_image[(x, y)] = 1
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    print_image(thermal_image, max_x, max_y)

    for inst in instructions:
        _, val = inst.split("=")
        val = int(val)
        if "x" in inst:
            fold_vertical(thermal_image, max_y, val)
        elif "y" in inst:
            fold_horizontal(thermal_image, max_x, val)
        else:
            raise ValueError("Unknown fold instruction.")
    print(sum(thermal_image.values()))
    print_image(thermal_image, max_x, max_y)
