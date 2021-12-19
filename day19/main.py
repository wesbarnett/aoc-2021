from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    scanners = defaultdict(list)
    i = -1
    for line in lines:
        if line.startswith("---"):
            i += 1
        elif line:
            scanners[i].append(tuple(map(int, line.split(","))))

    all_beacons = set()
    offset = {}

    for j in range(5):
        x0, y0, z0 = scanners[j][0]
        for i in range(5):
            if i != j:
                for s in [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1), (-1, -1, -1)]:
                    for d in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
                        for p in scanners[i]:
                            x1, y1, z1 = s[0]*p[d[0]], s[1]*p[d[1]], s[2]*p[d[2]]
                            dx, dy, dz = x0 - x1, y0 - y1, z0 - z1
                            beacons = []
                            for p in scanners[i]:
                                beacon = s[0]*p[d[0]] + dx, s[1]*p[d[1]] + dy, s[2]*p[d[2]] + dz
                                if beacon in scanners[j]:
                                    beacons.append(beacon)
                            if len(beacons) >= 12:
#                               for beacon in beacons:
#                                   all_beacons.add(beacon)
                                print(s, d)
                                offset[(j, i)] = tuple((dx, dy, dz))

    print(offset)
#   print(all_beacons)
