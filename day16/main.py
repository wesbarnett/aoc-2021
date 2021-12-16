from argparse import ArgumentParser
from pathlib import Path


def calc_literal(b, i):
    groups = []
    while b[i] == "1":
        i, g = i+5, b[i+1:i+5]
        groups.append(g)
    i, g = i+5, b[i+1:i+5]
    groups.append(g)
    while b[i] == 0:
        i += 1
    return i, int("".join(groups), 2)


def next_val(b, i, amt=1):
    return i+amt, int(b[i:i+amt], 2)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    data = Path(args.infile).read_text().rstrip("\n")
    x = "D2FE28"
    # x = "38006F45291200"
    # x = "EE00D40C823060"
    b = format(int(x, 16), f"0>{len(x)*4}b")

    i, vers = next_val(b, 0, 3)
    print(vers)
    i, type_id = next_val(b, i, 3)
    print(type_id)

    if type_id == 4:
        print(calc_literal(b, i))
    else:
        i, length_type_id = i+1, b[i]
        if length_type_id == "0":
            i, packet_length = next_val(b, i, 15)
            print(packet_length)
            length = 0
            i, literal = calc_literal(b, i)
            i, literal = calc_literal(b, i)
        else:
            num_packets = int(b[i:i+11], 2)
            print(num_packets)
