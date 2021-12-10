package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func findFirstIncorrect(line string) int {

	var stack []rune
	pairs := map[rune]rune{')': '(', ']': '[', '}': '{', '>': '<'}
	points := map[rune]int{')': 3, ']': 57, '}': 1197, '>': 25137}
	for _, x := range line {
		if _, ok := pairs[x]; ok {
			if stack[len(stack)-1] == pairs[x] {
				stack = stack[:len(stack)-1]
			} else {
				return points[x]
			}
		} else {
			stack = append(stack, x)
		}
	}

	return 0

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

	total_score := 0
	for _, line := range lines {
		total_score += findFirstIncorrect(line)
	}

	fmt.Println(total_score)
}
