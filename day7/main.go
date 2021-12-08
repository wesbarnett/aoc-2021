package main

import (
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func preprocess(line []string) (map[int]int, int, int) {
	positions := make(map[int]int)

	start := math.MaxInt
	end := math.MinInt
	for _, x := range line {
		i, _ := strconv.Atoi(x)
		if i < start {
			start = i
		}
		if i > end {
			end = i
		}
		positions[i] += 1
	}
	return positions, start, end
}

func calc_fuel1(positions map[int]int, new_position int) int {
	sum := 0
	for i, x := range positions {
		fuel := (i - new_position)
		if fuel < 0 {
			fuel *= -1
		}
		sum += fuel * x
	}
	return sum
}

func calc_fuel2(positions map[int]int, new_position int, fuel_map map[int]int) int {
	sum := 0
	for i, x := range positions {
		fuel := (i - new_position)
		if fuel < 0 {
			fuel *= -1
		}
		sum += fuel_map[fuel] * x
	}
	return sum
}

func main() {
	var file string
	flag.StringVar(&file, "infile", "input", "Input file")
	flag.Parse()

	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	line := strings.Split(strings.Trim(string(content), "\n"), ",")

	positions, start, end := preprocess(line)

	min_fuel := math.MaxInt
	for i := start; i < end; i++ {
		result := calc_fuel1(positions, i)
		if result < min_fuel {
			min_fuel = result
		}
	}
	fmt.Println(min_fuel)

	fuel_map := make(map[int]int)
	fuel_map[0] = 0
	for i := 1; i < end; i++ {
		fuel_map[i] = fuel_map[i-1] + i
	}

	min_fuel = math.MaxInt
	for i := start; i < end; i++ {
		result := calc_fuel2(positions, i, fuel_map)
		if result < min_fuel {
			min_fuel = result
		}
	}
	fmt.Println(min_fuel)
}
