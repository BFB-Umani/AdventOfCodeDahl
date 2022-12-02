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
		switch splitString[0] {
		case "A":
			switch splitString[1] {
			case "X":
				sum += calcDraw(1)
			case "Y":
				sum += calcWin(2)
			case "Z":
				sum += calcLose(3)
			}
		case "B":
			switch splitString[1] {
			case "X":
				sum += calcLose(1)
			case "Y":
				sum += calcDraw(2)
			case "Z":
				sum += calcWin(3)
			}
		case "C":
			switch splitString[1] {
			case "X":
				sum += calcWin(1)
			case "Y":
				sum += calcLose(2)
			case "Z":
				sum += calcDraw(3)
			}
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
