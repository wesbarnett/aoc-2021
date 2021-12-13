package main

import (
	"flag"
	"log"
	"os"
	"strings"
	"time"
)

func traverse(graph map[string][]string, visitCond func(map[string]int, string) bool) int {

	visited := make(map[string]int)

	var visit func(node string) int
	visit = func(node string) int {

		if node == "end" {
			return 1
		}

		// Only keep track if this was a small cave
		if strings.ToLower(node) == node {
			visited[node] += 1
		}

		sum := 0
		for _, dst := range graph[node] {
			if visitCond(visited, dst) {
				sum += visit(dst)
			}
		}

		// If this was a small cave, indicate it can be used in the next path
		if visited[node] > 0 {
			visited[node] -= 1
		}

		return sum

	}

	return visit("start")

}

// Can only visit small caves once
func part1VisitCond(visited map[string]int, dst string) bool {
	return dst != "start" && visited[dst] == 0
}

// Can only visit small caves once, except for a single small cave we can visit twice
func part2VisitCond(visited map[string]int, dst string) bool {
	return dst != "start" && ((!visitedCaveTwice(visited) && visited[dst] < 2) || (visitedCaveTwice(visited) && visited[dst] < 1))
}

func visitedCaveTwice(visited map[string]int) bool {

	for _, v := range visited {
		if v == 2 {
			return true
		}
	}
	return false
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
	graph := make(map[string][]string)
	for _, line := range lines {
		x := strings.Split(line, "-")
		graph[x[0]] = append(graph[x[0]], x[1])
		graph[x[1]] = append(graph[x[1]], x[0])
	}

	part1Start := time.Now()
	log.Printf("Result: %v", traverse(graph, part1VisitCond))
	part1Elapsed := time.Since(part1Start)
	log.Printf("Elapsed: %v", part1Elapsed)

	part2Start := time.Now()
	log.Printf("Result: %v", traverse(graph, part2VisitCond))
	part2Elapsed := time.Since(part2Start)
	log.Printf("Elapsed: %v", part2Elapsed)
}
