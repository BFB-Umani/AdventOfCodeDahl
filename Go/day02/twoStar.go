package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var losing = map[string]int{"A": 3, "B": 1, "C": 2}
var winning = map[string]int{"A": 2, "B": 3, "C": 1}
var draw = map[string]int{"A": 1, "B": 2, "C": 3}

func main() {

	input := getInput()
	var sum int

	for i := 0; i < len(input); i++ {
		var splitString []string = strings.Split(input[i], " ")
		switch splitString[1] {
		case "X":
			sum += losing[splitString[0]]
		case "Y":
			sum += draw[splitString[0]] + 3
		case "Z":
			sum += winning[splitString[0]] + 6
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
