package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Pos struct {
	x int
	y int
}

type Counter struct {
	pos map[Pos]int
}

func NewCounter() Counter {
	pos := make(map[Pos]int)
	return Counter{pos}
}

func (c *Counter) Add(x int, y int) {
	if _, ok := c.pos[Pos{x, y}]; ok {
		c.pos[Pos{x, y}] += 1
	} else {
		c.pos[Pos{x, y}] = 1
	}
}

func (c *Counter) AddVerticalLine(x1 int, y1 int, x2 int, y2 int) {
	if y2 < y1 {
		y1, y2 = y2, y1
	}
	for y := y1; y < y2+1; y++ {
		c.Add(x1, y)
	}
}

func (c *Counter) AddHorizontalLine(x1 int, y1 int, x2 int, y2 int) {
	if x2 < x1 {
		x1, x2 = x2, x1
	}
	for x := x1; x < x2+1; x++ {
		c.Add(x, y1)
	}
}

func (c *Counter) AddDiagonalLine(x1 int, y1 int, x2 int, y2 int) {

	var y_dir int

	if y1 > y2 {
		y_dir = -1
	} else {
		y_dir = 1
	}

	y := y1

	if x1 > x2 {
		for x := x1; x > x2-1; x-- {
			c.Add(x, y)
			y += y_dir
		}
	} else {
		for x := x1; x < x2+1; x++ {
			c.Add(x, y)
			y += y_dir
		}
	}
}

func (c *Counter) CalcResult() int {
	result := 0
	for _, v := range c.pos {
		if v >= 2 {
			result += 1
		}
	}
	return result
}

func (c *Counter) AddLine(x1 int, y1 int, x2 int, y2 int, addDiagonal bool) {
	if x1 == x2 {
		c.AddVerticalLine(x1, y1, x2, y2)
	} else if y1 == y2 {
		c.AddHorizontalLine(x1, y1, x2, y2)
	} else if addDiagonal {
		c.AddDiagonalLine(x1, y1, x2, y2)
	}
}

func ProcessLine(line string) (int, int, int, int) {
	item := strings.Split(line, " -> ")
	coord1 := strings.Split(item[0], ",")
	coord2 := strings.Split(item[1], ",")
	x1, _ := strconv.Atoi(coord1[0])
	y1, _ := strconv.Atoi(coord1[1])
	x2, _ := strconv.Atoi(coord2[0])
	y2, _ := strconv.Atoi(coord2[1])

	return x1, y1, x2, y2
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

	counter := NewCounter()
	for _, line := range lines {
		x1, y1, x2, y2 := ProcessLine(line)
		counter.AddLine(x1, y1, x2, y2, false)
	}
	fmt.Println(counter.CalcResult())

	counter2 := NewCounter()
	for _, line := range lines {
		x1, y1, x2, y2 := ProcessLine(line)
		counter2.AddLine(x1, y1, x2, y2, true)
	}
	fmt.Println(counter2.CalcResult())
}
