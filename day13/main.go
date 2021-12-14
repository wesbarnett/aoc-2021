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

type ThermalImage struct {
	data map[pos]struct{}
	max  pos
}

func NewThermalImage(initPos []pos) ThermalImage {
	data := make(map[pos]struct{})
	max_x := 0
	max_y := 0
	for _, p := range initPos {
		data[p] = struct{}{}
		if p.x > max_x {
			max_x = p.x
		}
		if p.y > max_y {
			max_y = p.y
		}
	}
	return ThermalImage{data, pos{max_x + 1, max_y + 1}}
}

func (ti *ThermalImage) FoldHorizontal(fold int) {
	for y := 1; y < fold+1; y++ {
		for x := 0; x < ti.max.x+1; x++ {
			if _, ok := ti.data[pos{x, fold + y}]; ok {
				ti.data[pos{x, fold - y}] = struct{}{}
				delete(ti.data, pos{x, fold + y})
			}
		}
	}
	ti.max.y = fold
}

func (ti *ThermalImage) FoldVertical(fold int) {
	for x := 1; x < fold+1; x++ {
		for y := 0; y < ti.max.y+1; y++ {
			if _, ok := ti.data[pos{fold + x, y}]; ok {
				ti.data[pos{fold - x, y}] = struct{}{}
				delete(ti.data, pos{fold + x, y})
			}
		}
	}
	ti.max.x = fold
}

func (ti *ThermalImage) Display() {
	display := make([][]string, ti.max.y)
	for y := 0; y < ti.max.y; y++ {
		display[y] = make([]string, ti.max.x)
		for x := 0; x < ti.max.x; x++ {
			display[y][x] = "."
		}
	}
	for k := range ti.data {
		display[k.y][k.x] = "#"
	}
	for row := 0; row < ti.max.y; row++ {
		s := ""
		for col := 0; col < ti.max.x; col++ {
			s += display[row][col]
		}
		fmt.Println(s)
	}
}

func (ti *ThermalImage) ProcessInstruction(inst string) {
	val := strings.Split(inst, "=")
	fold, _ := strconv.Atoi(val[1])
	if strings.Contains(val[0], "x") {
		ti.FoldVertical(fold)
	} else {
		ti.FoldHorizontal(fold)
	}
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

	var instructions []string
	var initPos []pos
	for _, line := range lines {
		if strings.HasPrefix(line, "fold along") {
			instructions = append(instructions, line)
		} else if len(line) > 0 {
			vals := strings.Split(line, ",")
			x, _ := strconv.Atoi(vals[0])
			y, _ := strconv.Atoi(vals[1])
			initPos = append(initPos, pos{x, y})
		}
	}

	ti := NewThermalImage(initPos)
	for _, inst := range instructions {
		ti.ProcessInstruction(inst)
	}
	ti.Display()
}
