package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
    "strings"
)

func readFile() []string {
    var lines []string

    f, err := os.Open("./input")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)
    scanner.Split(bufio.ScanLines)

    for scanner.Scan() {
        lines = append(lines, string(scanner.Text()))
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    return lines
}

func part1() {
    position := 0
    depth := 0
    lines := readFile()

    for _, line := range lines {
        line_split := strings.Split(line, " ")
        cmd := line_split[0]
        amt, _ := strconv.Atoi(line_split[1])
        if cmd == "forward" {
            position += amt
        } else if cmd == "down" {
            depth += amt
        } else if cmd == "up" {
            depth -= amt
        }
    }
    fmt.Println(depth*position)
}

func part2() {

    position := 0
    depth := 0
    aim := 0
    lines := readFile()

    for _, line := range lines {
        line_split := strings.Split(line, " ")
        cmd := line_split[0]
        amt, _ := strconv.Atoi(line_split[1])
        if cmd == "forward" {
            position += amt
        depth += aim*amt
        } else if cmd == "down" {
            aim += amt
        } else if cmd == "up" {
            aim -= amt
        }
    }

    fmt.Println(depth*position)
}

func main() {
    part1()
    part2()
}
