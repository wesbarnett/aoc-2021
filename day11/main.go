package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

type pos struct {
	x int
	y int
}

func FlashSequence(i int, j int, data [][]int, flashed map[pos]struct{}) {

	var flash func(i int, j int)
	flash = func(i int, j int) {
		if data[i][j] > 9 {
			if _, ok := flashed[pos{i, j}]; !ok {
				flashed[pos{i, j}] = struct{}{}
				for x := i - 1; x < i+2; x++ {
					for y := j - 1; y < j+2; y++ {
						if (pos{x, y} != pos{i, j}) && x >= 0 && x < len(data) && y >= 0 && y < len(data[x]) {
							data[x][y] += 1
							flash(x, y)
						}
					}
				}
			}
		}
	}

	flash(i, j)
}

func ReadMatrixInts(file string) [][]int {

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

	return data
}

func IncrementAll(data [][]int) [][]int {

	for i, row := range data {
		for j := range row {
			data[i][j] += 1
		}
	}

	return data
}

func main() {
	var file string
	flag.StringVar(&file, "infile", "input", "Input file")
	flag.Parse()

	data := ReadMatrixInts(file)

	flashes := 0
	for step := 0; step < 100; step++ {

		flashed := make(map[pos]struct{})
		data = IncrementAll(data)

		for i, row := range data {
			for j := range row {
				FlashSequence(i, j, data, flashed)
			}
		}

		for p := range flashed {
			data[p.x][p.y] = 0
			flashes += 1
		}
	}

	fmt.Println(flashes)
}
