package main

import (
	"fmt"
	"log"
	"os"
    "strconv"
	"strings"
)

func readFile(file string) ([]int, int) {
	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(strings.Trim(string(content), "\n"), "\n")

    num_bits := len(lines[0])
    num_items := len(lines)
    nums := make([]int, num_items)

    for i, x := range lines {
        num, err := strconv.ParseInt(x, 2, 32)
        if err != nil {
            log.Fatal(err)
        }
        nums[i] = int(num)
    }
    return nums, num_bits
}

func calcMajorityBit(nums []int, place int) int {
    sum := 0
    for _, x := range nums {
        sum += x >> place & 1
    }
    if (float64(sum) / float64(len(nums))) > 0.5 {
        return 1
    } else {
        return 0
    }

}

func part1(nums []int, num_bits int) int {
    gamma := 0
    epsilon := 0
    for i := 0; i < num_bits; i++ {
        place := num_bits - i - 1
        majorityBit := calcMajorityBit(nums, place)

        gamma |= majorityBit << place
        epsilon |= (majorityBit ^ 1) << place
    }
    return gamma*epsilon
}

func main() {
    nums, num_bits := readFile("input")
    fmt.Println(part1(nums, num_bits))
}
