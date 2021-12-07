package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func countFish(line []string, days int) int {

	fish := make([]int, 9)

	for _, x := range line {
		i, _ := strconv.ParseUint(x, 10, 32)
		fish[i] += 1
	}

	for i := 0; i < days; i++ {
		fish = append(fish[1:6], fish[6]+fish[8], fish[7], fish[8], fish[0])
	}

	sum := 0
	for _, x := range fish {
		sum += x
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
	fmt.Println(countFish(line, 80))
	fmt.Println(countFish(line, 256))

}
