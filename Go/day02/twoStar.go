package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func getLosingScore(choice string) int {
	losing := map[string]int{"A": 3, "B": 1, "C": 2}
	return losing[choice]
}

func getWinningScore(choice string) int {
	winning := map[string]int{"A": 2, "B": 3, "C": 1}
	return winning[choice] + 6
}

func getDrawScore(choice string) int {
	draw := map[string]int{"A": 1, "B": 2, "C": 3}
	return draw[choice] + 3
}

func main() {

	input := getInput()

	var sum int

	for i := 0; i < len(input); i++ {
		var splitString []string = strings.Split(input[i], " ")

		switch splitString[1] {
		case "X":
			sum += getLosingScore(splitString[0])
		case "Y":
			sum += getDrawScore(splitString[0])
		case "Z":
			sum += getWinningScore(splitString[0])
		}
	}
	fmt.Println(sum)
}

func getInput() []string {
	file, err := os.Open("Go/day02/input.txt")
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
