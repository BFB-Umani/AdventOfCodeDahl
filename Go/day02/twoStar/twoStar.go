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
		var splitString []string = strings.Split(input[i], " ")
		var choiceScore int

		switch splitString[1] {
		case "X":
			switch splitString[0] {
			case "A":
				choiceScore = 3
			case "B":
				choiceScore = 1
			case "C":
				choiceScore = 2
			}
			sum += calcLose(choiceScore)
		case "Y":
			switch splitString[0] {
			case "A":
				choiceScore = 1
			case "B":
				choiceScore = 2
			case "C":
				choiceScore = 3
			}
			sum += calcDraw(choiceScore)
		case "Z":
			switch splitString[0] {
			case "A":
				choiceScore = 2
			case "B":
				choiceScore = 3
			case "C":
				choiceScore = 1
			}
			sum += calcWin(choiceScore)
		}
	}
	fmt.Println(sum)
}

func calcLose(score int) int {
	return score + 0
}

func calcDraw(score int) int {
	return score + 3
}

func calcWin(score int) int {
	return score + 6
}

func getInput() []string {
	file, err := os.Open("day02/input.txt")
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
