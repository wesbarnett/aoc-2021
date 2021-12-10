package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

type pos struct {
	x int
	y int
}

func isLower(data [][]int, x int, y int) bool {

	p := data[x][y]

	if x+1 < len(data) && p >= data[x+1][y] {
		return false
	}

	if y+1 < len(data[x]) && p >= data[x][y+1] {
		return false
	}

	if x > 0 && p >= data[x-1][y] {
		return false
	}

	if y > 0 && p >= data[x][y-1] {
		return false
	}

	return true
}

func walkBasin(p pos, data [][]int, ch chan int) {
	var visit func(p pos, ch chan int)
	var next pos
	visited := make(map[pos]struct{})

	visit = func(p pos, ch chan int) {

		visited[p] = struct{}{}

		if !(p.x < 0 || p.y < 0 || p.x >= len(data) || p.y >= len(data[p.x]) || data[p.x][p.y] == 9) {

			ch <- 1

			for _, next = range []pos{pos{p.x + 1, p.y}, pos{p.x - 1, p.y}, pos{p.x, p.y + 1}, pos{p.x, p.y - 1}} {
				if _, ok := visited[next]; !ok {
					visit(next, ch)
				}
			}

		}

	}
	visit(p, ch)
	close(ch)

}

func main() {
	var file string
	flag.StringVar(&file, "infile", "input", "Input file")
	flag.Parse()

	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(strings.Trim(string(content), "\n"), "\n")
	data := make([][]int, len(lines))

	for i, x := range lines {
		data[i] = make([]int, len(x))
		for j, y := range x {
			data[i][j] = int(y) - '0'
		}

	}

	// Part 1
	var lows []int
	var lows_loc []pos
	for i, row := range data {
		for j, x := range row {
			if isLower(data, i, j) {
				lows = append(lows, x)
				lows_loc = append(lows_loc, pos{i, j})
			}
		}
	}

	risk_score := 0
	for _, x := range lows {
		risk_score += x + 1
	}

	fmt.Println(risk_score)

	// Part 2
	var sizes []int
	for _, p := range lows_loc {
		ch := make(chan int)
		go walkBasin(p, data, ch)
		size := 0
		for v := range ch {
			size += v
		}
		sizes = append(sizes, size)
	}

	sort.Ints(sizes)
	result := 1
	for _, size := range sizes[len(sizes)-3 : len(sizes)] {
		result *= size
	}
	fmt.Println(result)
}
