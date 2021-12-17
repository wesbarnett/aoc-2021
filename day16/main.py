from argparse import ArgumentParser
from pathlib import Path


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


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    x = Path(args.infile).read_text().rstrip("\n")
    x = "D2FE28"
    x = "38006F45291200"
    x = "EE00D40C823060"
    x = "8A004A801A8002F478"
    x = "620080001611562C8802118E34"
    x = "C0015000016115A2E0802F182340"
    x = "A0016C880162017C3686B18A3D4780"
    print(x)
    b = format(int(x, 16), f"0>{len(x)*4}b")
    print(b)

    total_vers = 0

    def run(b):

        global total_vers

        vers, b = int(b[:3], 2), b[3:]
        total_vers += vers
        print(f"version = {vers}")

        type_id, b = int(b[:3], 2), b[3:]
        print(f"type id = {type_id}")

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
            print(f"val = {val}")
            return length + 6

        else:

            length_type, b = b[0], b[1:]

            if length_type == "0":

                subpackets_length, b = int(b[:15], 2), b[15:]

                total_length = 0
                while total_length < subpackets_length:
                    length = run(b)
                    b = b[length:]
                    total_length += length
                return total_length + 22

            elif length_type == "1":

                subpackets_no, b = int(b[:11], 2), b[11:]
                total_length = 0
                length = 0
                for _ in range(subpackets_no):
                    length = run(b)
                    b = b[length:]
                    total_length += length
                return total_length + 18
    run(b)
    print(total_vers)
