package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func findFirstIncorrect(line string) (int, []rune) {

	var stack []rune
	pairs := map[rune]rune{')': '(', ']': '[', '}': '{', '>': '<'}
	points := map[rune]int{')': 3, ']': 57, '}': 1197, '>': 25137}
	for _, x := range line {
		if _, ok := pairs[x]; ok {
			if stack[len(stack)-1] == pairs[x] {
				stack = stack[:len(stack)-1]
			} else {
				return points[x], nil
			}
		} else {
			stack = append(stack, x)
		}
	}

	return 0, stack

}

func autocomplete(stack []rune) int {

	pairs := map[rune]rune{'(': ')', '[': ']', '{': '}', '<': '>'}
	points := map[rune]int{')': 1, ']': 2, '}': 3, '>': 4}

	score := 0
	for i := len(stack) - 1; i > -1; i-- {
		score *= 5
		score += points[pairs[stack[i]]]
	}

	return score
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
	var incomplete [][]rune
	for _, line := range lines {
		score, stack := findFirstIncorrect(line)
		total_score += score
		if stack != nil {
			incomplete = append(incomplete, stack)
		}
	}

	fmt.Println(total_score)

	var compl_scores []int
	for _, stack := range incomplete {
		compl_scores = append(compl_scores, autocomplete(stack))
	}

	sort.Ints(compl_scores)

	fmt.Println(compl_scores[(len(compl_scores)+1)/2-1])
}
