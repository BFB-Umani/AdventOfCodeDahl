package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := getInput()

	var threeHighest []int
	var sum int

	for i := 0; i < len(input); i++ {
		if input[i] == "" {
			if sum > threeHighest[2] {
				threeHighest[1] = threeHighest[2]
				threeHighest[0] = threeHighest[1]
				threeHighest[2] = sum
			} else if sum > threeHighest[1] {
				threeHighest[0] = threeHighest[1]
				threeHighest[1] = sum
			} else if sum > threeHighest[0] {
				threeHighest[0] = sum
			}
			sum = 0
		} else {
			var parsedInput, _ = strconv.Atoi(input[i])

			sum += parsedInput
		}
	}

	fmt.Println()
}

func getInput() []string {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lineArr []string

	for scanner.Scan() {
		// do something with a line
		lineArr = append(lineArr, scanner.Text())
	}
	return lineArr
}
