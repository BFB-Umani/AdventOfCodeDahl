package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	input := getInput()

	teams := getTeams(input)

	var sum int

	for i := 0; i < len(teams); i++ {
		var elves []string = strings.Split(teams[i], " ")
		var firstElf string = elves[0]
		var foundItems []byte

		for j := 0; j < len(firstElf); j++ {
			if strings.Contains(elves[1], string(firstElf[j])) && strings.Contains(elves[2], string(firstElf[j])) && !strings.Contains(string(foundItems), string(firstElf[j])) {
				if firstElf[j] > 90 {
					foundItems = append(foundItems, firstElf[j])
					sum += int(firstElf[j]) - 96
				} else {
					foundItems = append(foundItems, firstElf[j])
					sum += int(firstElf[j]) - 38
				}
			}
		}
	}
	fmt.Println(sum)
}

func getTeams(input []string) []string {
	var returnArray []string
	for i := 0; i < len(input); i += 3 {
		var team string = input[i] + " " + input[i+1] + " " + input[i+2]
		returnArray = append(returnArray, team)
	}
	return returnArray
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
