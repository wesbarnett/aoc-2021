from argparse import ArgumentParser
from pathlib import Path
from math import prod


def calc_literal(b, i):
    groups = []
    while b[i] == "1":
        i, g = i+5, b[i+1:i+5]
        groups.append(g)
    i, g = i+5, b[i+1:i+5]
    groups.append(g)
    return i, int("".join(groups), 2)


def next_val(b, i, amt=1):
    return i+amt, int(b[i:i+amt], 2)


def calc_subpack(vals, type_id):
    if type_id == 0:
        return sum(vals)
    elif type_id == 1:
        return prod(vals)
    elif type_id == 2:
        return min(vals)
    elif type_id == 3:
        return max(vals)
    elif type_id == 5:
        return vals[0] > vals[1]
    elif type_id == 6:
        return vals[0] < vals[1]
    elif type_id == 7:
        return vals[0] == vals[1]


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    x = Path(args.infile).read_text().rstrip("\n")
    b = format(int(x, 16), f"0>{len(x)*4}b")

    total_vers = 0

    def run(b):

        global total_vers

        vers, b = int(b[:3], 2), b[3:]
        total_vers += vers

        type_id, b = int(b[:3], 2), b[3:]

        if type_id == 4:

            length = 0
            groups = []
            while b[0] != "0":

                b = b[1:]
                g, b = b[:4], b[4:]
                length += 5

                groups.append(g)

            b = b[1:]
            g, b = b[:4], b[4:]
            length += 5

            groups.append(g)

            val = int("".join(groups), 2)
            return length + 6, val

        else:

            length_type, b = b[0], b[1:]

            if length_type == "0":

                subpackets_length, b = int(b[:15], 2), b[15:]

                total_length = 0
                subpack_vals = []
                while total_length < subpackets_length:
                    length, val = run(b)
                    b = b[length:]
                    total_length += length
                    subpack_vals.append(val)

                val = calc_subpack(subpack_vals, type_id)
                return total_length + 22, val

            elif length_type == "1":

                subpackets_no, b = int(b[:11], 2), b[11:]
                total_length = 0
                length = 0
                subpack_vals = []
                for _ in range(subpackets_no):
                    length, val = run(b)
                    b = b[length:]
                    total_length += length
                    subpack_vals.append(val)
                val = calc_subpack(subpack_vals, type_id)
                return total_length + 18, val

    part2 = run(b)[0]
    print(total_vers)
    print(part2)
