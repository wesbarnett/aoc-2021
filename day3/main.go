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
	if (float64(sum) / float64(len(nums))) >= 0.5 {
		return 1
	} else {
		return 0
	}

}

func filterCO2Nums(nums []int, place int) []int {
	majorityBit := calcMajorityBit(nums, place)
	var result []int
	for _, x := range nums {
		if majorityBit != ((x >> place) & 1) {
			result = append(result, x)
		}
	}
	return result
}

func filterOxygenNums(nums []int, place int) []int {
	majorityBit := calcMajorityBit(nums, place)
	var result []int
	for _, x := range nums {
		if majorityBit == ((x >> place) & 1) {
			result = append(result, x)
		}
	}
	return result
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
	return gamma * epsilon
}

func part2(nums []int, num_bits int) int {

	oxygenNums := make([]int, len(nums))
	copy(oxygenNums, nums)
	for i := num_bits - 1; i >= 0; i-- {
		oxygenNums = filterOxygenNums(oxygenNums, i)
		if len(oxygenNums) == 1 {
			break
		}
	}

	CO2Nums := make([]int, len(nums))
	copy(CO2Nums, nums)
	for i := num_bits - 1; i >= 0; i-- {
		CO2Nums = filterCO2Nums(CO2Nums, i)
		if len(CO2Nums) == 1 {
			break
		}
	}

	return oxygenNums[0] * CO2Nums[0]
}

func main() {
	nums, num_bits := readFile("input")
	fmt.Println(part1(nums, num_bits))
	fmt.Println(part2(nums, num_bits))
}
