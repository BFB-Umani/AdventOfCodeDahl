package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	input := getInput()

	var sum int

	for i := 0; i < len(input); i++ {
		var halfInput = len(input[i]) / 2
		var firstCompartment string = input[i][0:halfInput]
		var secondCompartment string = input[i][halfInput:len(input[i])]
		var foundItems []byte

		for j := 0; j < len(firstCompartment); j++ {
			if strings.Contains(secondCompartment, string(firstCompartment[j])) && !strings.Contains(string(foundItems), string(firstCompartment[j])) {
				if firstCompartment[j] > 90 {
					foundItems = append(foundItems, firstCompartment[j])
					sum += int(firstCompartment[j]) - 96
				} else {
					foundItems = append(foundItems, firstCompartment[j])
					sum += int(firstCompartment[j]) - 38
				}
			}
		}
	}
	fmt.Println(sum)
}

func getInput() []string {
	file, err := os.Open("Go/day03/input.txt")
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
