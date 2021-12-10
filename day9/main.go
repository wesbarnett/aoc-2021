package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

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

	var lows []int
	for i, row := range data {
		for j, x := range row {
			if isLower(data, i, j) {
				lows = append(lows, x)
			}
		}
	}

	risk_score := 0
	for _, x := range lows {
		risk_score += x + 1
	}

	fmt.Println(risk_score)
}
