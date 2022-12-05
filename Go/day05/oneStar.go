package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

func getCratesAndMoves(input []string) (map[string][]string, []string) {
	cratesMap := make(map[string][]string)
	var crates []string
	var columns string
	var inputStart int
	for i := 0; i < len(input); i++ {
		if regexp.MustCompile(`\d`).MatchString(input[i]) {
			columns = input[i]
			inputStart = i + 2
			break
		}
		crates = append(crates, input[i])
	}

	for i := len(crates) - 1; i >= 0; i-- {
		for j := len(crates[i]) - 1; j >= 0; j-- {
			var crateString = crates[i]
			if crateString[j] == ']' {
				var crate string = string(crateString[j-1])
				cratesMap[string(columns[j-1])] = append(cratesMap[string(columns[j-1])], crate)
			}
		}
	}
	return cratesMap, input[inputStart:]
}

func main() {
	input := getInput()

	cratesMap, moves := getCratesAndMoves(input)
	var finalString string

	for i := 0; i < len(moves); i++ {
		instructions := strings.Split(moves[i], " ")
		loopAmount, _ := strconv.Atoi(instructions[1])
		for j := 0; j < loopAmount; j++ {
			cratesMap[instructions[5]] = append(cratesMap[instructions[5]], cratesMap[instructions[3]][len(cratesMap[instructions[3]])-1])
			cratesMap[instructions[3]] = cratesMap[instructions[3]][:len(cratesMap[instructions[3]])-1]
		}
	}

	keys := make([]string, 0, len(cratesMap))
	for k := range cratesMap {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		finalString += cratesMap[k][len(cratesMap[k])-1]
	}

	fmt.Println(finalString)
}

func getInput() []string {
	file, err := os.Open("Go/day05/input.txt")
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
