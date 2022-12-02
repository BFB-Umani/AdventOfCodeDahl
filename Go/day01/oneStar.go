package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := getInput()

	var sum int
	var highestSum int

	for i := 0; i < len(input); i++ {
		if input[i] == "" {
			if sum > highestSum {
				highestSum = sum
			}
			sum = 0
		} else {
			var parsedInput, _ = strconv.Atoi(input[i])

			sum += parsedInput
		}
	}
	if sum > highestSum {
		highestSum = sum
	}

	fmt.Println(highestSum)
}

func getInput() []string {
	file, err := os.Open("Go/day01/input.txt")
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
