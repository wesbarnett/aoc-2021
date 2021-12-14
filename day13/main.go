package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

type pos struct {
	x uint32
	y uint32
}

type ThermalImage struct {
	data map[pos]struct{}
	max  pos
}

func NewThermalImage(initPos []pos) ThermalImage {
	data := make(map[pos]struct{}, len(initPos))
	var max_x, max_y uint32
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

func (ti *ThermalImage) FoldHorizontal(fold uint32) {
	var x, y uint32
	for y = 1; y < fold+1; y++ {
		for x = 0; x < ti.max.x+1; x++ {
			if _, ok := ti.data[pos{x, fold + y}]; ok {
				ti.data[pos{x, fold - y}] = struct{}{}
				delete(ti.data, pos{x, fold + y})
			}
		}
	}
	ti.max.y = fold
}

func (ti *ThermalImage) FoldVertical(fold uint32) {
	var x, y uint32
	for x = 1; x < fold+1; x++ {
		for y = 0; y < ti.max.y+1; y++ {
			if _, ok := ti.data[pos{fold + x, y}]; ok {
				ti.data[pos{fold - x, y}] = struct{}{}
				delete(ti.data, pos{fold + x, y})
			}
		}
	}
	ti.max.x = fold
}

func (ti *ThermalImage) Display() {
	var x, y uint32
	display := make([][]string, ti.max.y)
	for y = 0; y < ti.max.y; y++ {
		display[y] = make([]string, ti.max.x)
		for x = 0; x < ti.max.x; x++ {
			display[y][x] = "."
		}
	}
	for k := range ti.data {
		display[k.y][k.x] = "#"
	}
	for y = 0; y < ti.max.y; y++ {
		fmt.Println(strings.Join(display[y], ""))
	}
}

func (ti *ThermalImage) ProcessInstruction(inst string) {
	val := strings.Split(inst, "=")
	fold, _ := strconv.ParseUint(val[1], 10, 32)
	if strings.Contains(val[0], "x") {
		ti.FoldVertical(uint32(fold))
	} else {
		ti.FoldHorizontal(uint32(fold))
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
			x, _ := strconv.ParseUint(vals[0], 10, 32)
			y, _ := strconv.ParseUint(vals[1], 10, 32)
			initPos = append(initPos, pos{uint32(x), uint32(y)})
		}
	}

	start := time.Now()
	ti := NewThermalImage(initPos)
	for i, inst := range instructions {
		ti.ProcessInstruction(inst)
		if i == 0 {
			var sum uint32
			for _ = range ti.data {
				sum += 1
			}
			fmt.Println(sum)
		}
	}
	ti.Display()
	elapsed := time.Since(start)
	log.Printf("Elapsed: %v", elapsed)
}
