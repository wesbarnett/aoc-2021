package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func traverse(graph map[string][]string, visitCond func(map[string]int, string) bool) int {

	visited := make(map[string]int)

	var visit func(node string) int
	visit = func(node string) int {

		if node == "end" {
			return 1
		}

		if strings.ToLower(node) == node {
			visited[node] += 1
		}

		sum := 0
		for _, dst := range graph[node] {
			if visitCond(visited, dst) {
				sum += visit(dst)
			}
		}

		if visited[node] > 0 {
			visited[node] -= 1
		}

		return sum

	}

	return visit("start")

}

func part1VisitCond(visited map[string]int, dst string) bool {
	return dst != "start" && visited[dst] == 0
}

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

	fmt.Println(traverse(graph, part1VisitCond))
	fmt.Println(traverse(graph, part2VisitCond))
}
