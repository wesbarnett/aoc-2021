package main

import (
	"flag"
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

func vertical_line(x1 int, y1 int, x2 int, y2 int, counter map[pos]int) map[pos]int {
	if y2 < y1 {
		tmp := y1
		y1 = y2
		y2 = tmp
	}
	for y := y1; y < y2+1; y++ {
		if _, ok := counter[pos{x1, y}]; ok {
			counter[pos{x1, y}] += 1
		} else {
			counter[pos{x1, y}] = 1
		}
	}
	return counter
}

func horizontal_line(x1 int, y1 int, x2 int, y2 int, counter map[pos]int) map[pos]int {
	if x2 < x1 {
		tmp := x1
		x1 = x2
		x2 = tmp
	}
	for x := x1; x < x2+1; x++ {
		if _, ok := counter[pos{x, y1}]; ok {
			counter[pos{x, y1}] += 1
		} else {
			counter[pos{x, y1}] = 1
		}
	}
	return counter
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

	counter := make(map[pos]int)
	for _, line := range lines {
		item := strings.Split(line, " -> ")
		coord1 := strings.Split(item[0], ",")
		coord2 := strings.Split(item[1], ",")
		x1, _ := strconv.Atoi(coord1[0])
		y1, _ := strconv.Atoi(coord1[1])
		x2, _ := strconv.Atoi(coord2[0])
		y2, _ := strconv.Atoi(coord2[1])

		if x1 == x2 {
			counter = vertical_line(x1, y1, x2, y2, counter)
		} else if y1 == y2 {
			counter = horizontal_line(x1, y1, x2, y2, counter)
		}
	}

	result := 0
	for _, v := range counter {
		if v >= 2 {
			result += 1
		}
	}
	fmt.Println(result)
}
