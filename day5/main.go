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

func VerticalLine(x1 int, y1 int, x2 int, y2 int, counter map[pos]int) map[pos]int {
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

func HorizontalLine(x1 int, y1 int, x2 int, y2 int, counter map[pos]int) map[pos]int {
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

func DiagonalLine(x1 int, y1 int, x2 int, y2 int, counter map[pos]int) map[pos]int {


    var y_dir int

    if y1 > y2 {
        y_dir = -1
    } else {
        y_dir = 1
    }

    y := y1

    if x1 > x2 {
        for x := x1; x > x2-1; x-- {
            if _, ok := counter[pos{x, y}]; ok {
                counter[pos{x, y}] += 1
            } else {
                counter[pos{x, y}] = 1
            }
            y += y_dir
        }
    } else {
        for x := x1; x < x2+1; x++ {
            if _, ok := counter[pos{x, y}]; ok {
                counter[pos{x, y}] += 1
            } else {
                counter[pos{x, y}] = 1
            }
            y += y_dir
        }
    }

    return counter
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

func CalcResult(counter map[pos]int) int {
	result := 0
	for _, v := range counter {
		if v >= 2 {
			result += 1
		}
	}
    return result
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
        x1, y1, x2, y2 := ProcessLine(line)
		if x1 == x2 {
			counter = VerticalLine(x1, y1, x2, y2, counter)
		} else if y1 == y2 {
			counter = HorizontalLine(x1, y1, x2, y2, counter)
		}
	}
	fmt.Println(CalcResult(counter))

	counter2 := make(map[pos]int)
	for _, line := range lines {
        x1, y1, x2, y2 := ProcessLine(line)
		if x1 == x2 {
			counter2 = VerticalLine(x1, y1, x2, y2, counter2)
		} else if y1 == y2 {
			counter2 = HorizontalLine(x1, y1, x2, y2, counter2)
		} else {
			counter2 = DiagonalLine(x1, y1, x2, y2, counter2)
        }
    }
	fmt.Println(CalcResult(counter2))
}
