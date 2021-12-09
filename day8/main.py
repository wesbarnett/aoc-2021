from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path


def process_word(x):
    return "".join(sorted(list(x)))


def decode_line(line):

    signal, output = line.split(" | ")
    digits = {}

    for k, length in zip([1, 4, 7, 8], [2, 4, 3, 7]):
        digits[k] = set(list(filter(lambda x: len(x) == length, signal.split()))[0])

    for x in filter(lambda x: len(x) == 5, signal.split()):
        chars = set(x)
        if len(digits[1] & chars) == 2:
            digits[3] = chars
        elif len(digits[4] & chars) == 3:
            digits[5] = chars
        else:
            digits[2] = chars

    for x in filter(lambda x: len(x) == 6, signal.split()):
        chars = set(x)
        if len(digits[4] & chars) == 4:
            digits[9] = chars
        elif len(digits[1] & chars) == 1:
            digits[6] = chars
        else:
            digits[0] = chars

    charmap = {process_word(v): str(k) for k, v in digits.items()}
    return int("".join([charmap[process_word(x)] for x in output.split()]))


if __name__ == "__main__":

    digits = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    lengths = defaultdict(list)
    for k, v in digits.items():
        lengths[len(v)].append(k)

    unique_length = []
    for k, v in lengths.items():
        if len(v) == 1:
            unique_length.append(k)

    count = 0
    for line in lines:
        signal, output = line.split(" | ")
        for x in output.split():
            if len(x) in unique_length:
                count += 1

    print(count)

    print(sum([decode_line(line) for line in lines]))
