package main

import (
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strings"
)

func initPairCounts(template string) map[string]int {

	pairCounts := make(map[string]int)
	for i := 0; i < len(template)-1; i++ {
		pairCounts[template[i:i+2]] += 1
	}

	return pairCounts
}

func updatePairCounts(pairCounts map[string]int, rules map[string]string) map[string]int {

	newPairCounts := make(map[string]int)
	for k, v := range pairCounts {
		newPairCounts[k] = v
	}
	for pair, ins := range rules {
		newPairCounts[string(pair[0])+ins] += pairCounts[pair]
		newPairCounts[ins+string(pair[1])] += pairCounts[pair]
		newPairCounts[pair] -= pairCounts[pair]
	}
	return newPairCounts
}

// getElementCounts counts all elements in the polymer using pair counts
// It does this by counting the second item in each pair. Since the first element
// in the polymer is not the second item of a pair, it needs to be added once
func getElementCounts(polymerTemplate string, pairCounts map[string]int) map[string]int {

	counts := make(map[string]int)
	for k, v := range pairCounts {
		counts[string(k[1])] += v
	}

	counts[string(polymerTemplate[0])] += 1

	return counts
}

func getMinAndMaxDiff(counts map[string]int) int {

	max_v := 0
	min_v := math.MaxInt64
	for _, v := range counts {
		if v > max_v {
			max_v = v
		}
		if v < min_v {
			min_v = v
		}
	}
	return max_v - min_v
}

func run(steps int, polymerTemplate string, rules map[string]string) int {
	pairCounts := initPairCounts(polymerTemplate)

	for i := 0; i < steps; i++ {
		pairCounts = updatePairCounts(pairCounts, rules)
	}

	counts := getElementCounts(polymerTemplate, pairCounts)
	return getMinAndMaxDiff(counts)
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

	polymerTemplate := lines[0]
	rules := make(map[string]string)
	for _, line := range lines[2:] {
		val := strings.Split(line, " -> ")
		rules[val[0]] = val[1]
	}
	fmt.Println(run(10, polymerTemplate, rules))
	fmt.Println(run(40, polymerTemplate, rules))
}
