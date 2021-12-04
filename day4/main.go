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
}

func All(items []bool) bool {
    for _, items := range items {
        if !item {
            return false
        }
    }
    return true
}

func NewCard(inputs string) Card {
    data := make(map[int]pos)
    rows := strings.Split(inputs, "\n")
    marked := make([][]bool, len(rows))
    for i, x :=  range rows {
        items := strings.Split(x, " ")
        marked[i] = make([]bool, len(items))
        for j, y := range items {
            marked[i][j] = false
            val, _ := strconv.Atoi(y)
            data[val] = pos{i, j}
        }
    }
    return Card{data, marked, false}
}

func (card Card) Play(num int) bool {
    if pos, ok := card.data[num]; ok {
        card.marked[pos.x][pos.y] = true
    }
    return card.Win()

}

func (card Card) Win() bool {
    for _, row := range card.marked {
        if All(row) {
            card.won = true
            return true
        }
    }

    for c := range card.marked[0] {
        col := make(int[], len(card.marked[0]))
        for r, x := range card.marked[0] {
            col[r] = card.marked[c][r]
        }
        if All(col) {
            card.won = true
            return true
        }
    }

    return false

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

    fmt.Println(cards[0].data)
    fmt.Println(cards[0].marked)

}
