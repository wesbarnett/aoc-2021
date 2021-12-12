package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func traverse(graph map[string][]string) int {

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
			if dst != "start" && visited[dst] == 0 {
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

func main() {
	var file string
	flag.StringVar(&file, "infile", "input", "Input file")
	flag.Parse()

	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(strings.Trim(string(content), "\n"), "\n")
	fmt.Println(lines)
	graph := make(map[string][]string)
	for _, line := range lines {
		x := strings.Split(line, "-")
		graph[x[0]] = append(graph[x[0]], x[1])
		graph[x[1]] = append(graph[x[1]], x[0])
	}

	fmt.Println(traverse(graph))
}
