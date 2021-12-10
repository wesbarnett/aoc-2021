package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func unionDigits(d1 string, d2 string) int {

	d1_counts := make(map[rune]int)
	d2_counts := make(map[rune]int)

	for _, x := range "abcdefg" {
		d1_counts[x] = 0
		d2_counts[x] = 0
	}

	for _, x := range d1 {
		d1_counts[x] = 1
	}

	for _, x := range d2 {
		d2_counts[x] = 1
	}

	union := 0
	for _, x := range "abcdefg" {
		if d1_counts[x] == 1 && d2_counts[x] == 1 {
			union += 1
		}
	}

	return union
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

	easy_count := 0
	output_sum := 0

	for _, x := range lines {

		line := strings.Split(x, " | ")
		charmap := make(map[string]int)
		nummap := make(map[int]string)

		for _, w := range strings.Split(line[0], " ") {
			s := sortString(w)
			if len(s) == 2 {
				charmap[s] = 1
				nummap[1] = s
			} else if len(s) == 4 {
				charmap[s] = 4
				nummap[4] = s
			} else if len(s) == 3 {
				charmap[s] = 7
				nummap[7] = s
			} else if len(s) == 7 {
				charmap[s] = 8
				nummap[8] = s
			}
		}

		for _, w := range strings.Split(line[1], " ") {
			s := sortString(w)
			if _, ok := charmap[s]; ok {
				easy_count += 1
			}
		}

		for _, w := range strings.Split(line[0], " ") {
			s := sortString(w)
			if len(s) == 5 {
				if unionDigits(s, nummap[1]) == 2 {
					charmap[s] = 3
				} else if unionDigits(s, nummap[4]) == 3 {
					charmap[s] = 5
				} else {
					charmap[s] = 2
				}
			} else if len(s) == 6 {
				if unionDigits(s, nummap[4]) == 4 {
					charmap[s] = 9
				} else if unionDigits(s, nummap[1]) == 1 {
					charmap[s] = 6
				} else {
					charmap[s] = 0
				}
			}
		}

		factor := 1000
		decoded := 0
		for _, w := range strings.Split(line[1], " ") {
			s := sortString(w)
			decoded += charmap[s] * factor
			factor /= 10
		}
		output_sum += decoded

	}

	fmt.Println(easy_count)
	fmt.Println(output_sum)
}
