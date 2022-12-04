package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	input := getInput()

	var sum int

	for i := 0; i < len(input); i++ {
		workload := strings.Split(input[i], ",")
		firstIntRange := getIntRange(strings.Split(workload[0], "-"))
		secondIntRange := getIntRange(strings.Split(workload[1], "-"))

		if firstIntRange[0] < secondIntRange[0] {
			if firstIntRange[1] >= secondIntRange[1] {
				sum++
			}
		} else if firstIntRange[0] == secondIntRange[0] {
			sum++
		} else {
			if firstIntRange[1] <= secondIntRange[1] {
				sum++
			}
		}
	}
	fmt.Println(sum)
}

func getIntRange(input []string) []int {
	var returnArray []int
	for i := 0; i < len(input); i++ {
		var result, _ = strconv.Atoi(input[i])
		returnArray = append(returnArray, result)
	}
	return returnArray
}

func getInput() []string {
	file, err := os.Open("Go/day04/input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lineArr []string

	for scanner.Scan() {
		lineArr = append(lineArr, scanner.Text())
	}
	return lineArr
}
