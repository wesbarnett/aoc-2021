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

    def play(self, num):
        if num in self.data:
            x, y = self.data[num]
            self.marked[x][y] = True
            self.unmarked_nums.remove(num)
        return self.win()

    def win(self):
        for row in self.marked:
            if all(row):
                return True
        for c in range(len(self.marked[0])):
            if all([self.marked[r][c] for r in range(len(self.marked[0]))]):
                return True
        return False


def play_bingo(cards, plays):
    for play in plays:
        for card in cards:
            result = card.play(play)
            if result:
                return card, play

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n\n")

    plays = [int(x) for x in lines[0].split(",")]
    cards = [Card(x) for x in lines[1:]]

    winner, play = play_bingo(cards, plays)
    print(sum(list(winner.unmarked_nums))*play)

