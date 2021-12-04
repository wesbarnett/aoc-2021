package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type pos struct {
    x int
    y int
}

type Card struct {
    data map[int]pos
    marked [][]bool
    won bool
    unmarked_nums Set
}

type Set map[int]struct{}

func (s Set) add(item int) {
    s[item] = struct{}{}
}

func (s Set) remove(item int) {
    delete(s, item)
}

func (s Set) has(item int) bool {
    _, ok := s[item]
    return ok
}

func All(items []bool) bool {
    for _, item := range items {
        if !item {
            return false
        }
    }
    return true
}

func FinalScore(card Card, play int) int {
    sum := 0
    for k, _ := range card.unmarked_nums {
        sum += k
    }
    return sum*play
}

func NewCard(inputs string) Card {
    data := make(map[int]pos)
    rows := strings.Split(inputs, "\n")
    marked := make([][]bool, len(rows))
    unmarked_nums := Set{}
    for i, x := range rows {
        items := strings.Fields(x)
        marked[i] = make([]bool, len(items))
        for j, y := range items {
            marked[i][j] = false
            val, _ := strconv.Atoi(y)
            data[val] = pos{i, j}
            unmarked_nums.add(val)
        }
    }
    return Card{data, marked, false, unmarked_nums}
}

func (card *Card) Play(num int) bool {
    if pos, ok := card.data[num]; ok {
        card.marked[pos.x][pos.y] = true
    }
    if card.unmarked_nums.has(num) {
        card.unmarked_nums.remove(num)
    }
    return card.Win()

}

func (card *Card) Win() bool {
    for _, row := range card.marked {
        if All(row) {
            card.won = true
            return true
        }
    }

    for c := range card.marked[0] {
        col := make([]bool, len(card.marked[0]))
        for r := range card.marked[0] {
            col[r] = card.marked[r][c]
        }
        if All(col) {
            card.won = true
            return true
        }
    }

    return false

}

func Part1(cards []Card, plays []int) int {
    for _, play := range plays {
        for _, card := range cards {
            if card.Play(play) {
                return FinalScore(card, play)
            }
        }
    }
    return 0
}

func Part2(cards []Card, plays []int) int {
    var winning_card Card
    var winning_play int
    for _, play := range plays {
        for i := range cards {
            if !cards[i].won && cards[i].Play(play) {
                winning_card = cards[i]
                winning_play = play
            }
        }
    }
    return FinalScore(winning_card, winning_play)
}


func main() {

    file := "input"

	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(strings.Trim(string(content), "\n"), "\n\n")

    var plays []int
    for _, x := range strings.Split(lines[0], ",") {
        num, _ := strconv.Atoi(x)
        plays = append(plays, num)
    }

    var cards []Card
    for _, x := range lines[1:] {
        cards = append(cards, NewCard(x))
    }

    fmt.Println(Part1(cards, plays))
    fmt.Println(Part2(cards, plays))
}
