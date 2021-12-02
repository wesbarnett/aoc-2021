package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
)

func main() {
    var nums []int

    f, err := os.Open("./input")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    scanner := bufio.NewScanner(f)
    scanner.Split(bufio.ScanWords)

    for scanner.Scan() {
        i, _ := strconv.Atoi(scanner.Text())
        nums = append(nums, i)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    sum := 0
    for i, _ := range nums[1:] {
        if nums[i+1] > nums[i] {
            sum += 1
        }
    }
    fmt.Println(sum)

    var nums3 []int
    for i, _ := range nums[2:] {
        nums3 = append(nums3, nums[i] + nums[i+1] + nums[i+2])
    }

    sum = 0
    for i, _ := range nums3[1:] {
        if nums3[i+1] > nums3[i] {
            sum += 1
        }
    }
    fmt.Println(sum)
}
