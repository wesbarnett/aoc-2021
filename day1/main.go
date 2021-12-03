package main

import (
    "fmt"
    "log"
    "os"
    "strconv"
    "strings"
)

func calcSum(X []int) int {
    sum := 0
    for i, _ := range X[1:] {
        if X[i+1] > X[i] {
            sum += 1
        }
    }
    return sum
}

func main() {

    content, err := os.ReadFile("./input")
    if err != nil {
        log.Fatal(err)
    }
    lines := strings.Split(strings.Trim(string(content), "\n"), "\n")

    nums := make([]int, len(lines))
    for i, n := range lines {
        nums[i], _ = strconv.Atoi(n)
    }

    sum := calcSum(nums)
    fmt.Println(sum)

    nums3 := make([]int, len(nums))
    for i, _ := range nums[2:] {
        nums3[i] = nums[i] + nums[i+1] + nums[i+2]
    }

    sum3 := calcSum(nums3)
    fmt.Println(sum3)
}
