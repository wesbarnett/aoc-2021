from argparse import ArgumentParser
from pathlib import Path


class Card:

    def __init__(self, inputs):
        self.data = {}
        rows = inputs.split("\n")
        self.unmarked_nums = set()
        for i, x in enumerate(rows):
            for j, y in enumerate(x.split()):
                self.data[int(y)] = (i, j)
                self.unmarked_nums.add(int(y))

        self.marked = [[False for _ in x.split()] for x in rows]
        self.won = False

    def play(self, num):
        if num in self.data:
            x, y = self.data[num]
            self.marked[x][y] = True
        if num in self.unmarked_nums:
            self.unmarked_nums.remove(num)
        return self.win()

    def win(self):
        for row in self.marked:
            if all(row):
                self.won = True
                return True
        for c in range(len(self.marked[0])):
            if all([self.marked[r][c] for r in range(len(self.marked[0]))]):
                self.won = True
                return True
        return False


def part1(cards, plays):
    for play in plays:
        for card in cards:
            result = card.play(play)
            if result:
                return card, play


def part2(cards, plays):
    for play in plays:
        for card in cards:
            if not card.won:
                result = card.play(play)
                if result:
                    winner = card, play
    return winner


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n\n")

    plays = [int(x) for x in lines[0].split(",")]
    cards = [Card(x) for x in lines[1:]]

    winner, play = part1(cards, plays)
    print(sum(list(winner.unmarked_nums))*play)

    winner, play = part2(cards, plays)
    print(sum(list(winner.unmarked_nums))*play)
