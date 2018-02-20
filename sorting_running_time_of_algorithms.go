package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	arr := make([]int, n)

	for i := range arr {
		fmt.Scan(&arr[i])
	}

	sorted := insertionSort(arr)
	// printArray(sorted)
}

func insertionSort(arr []int) []int {
	var x, j int
	shiftsNumber := 0
	for i := 1; i < len(arr); i++ {
		x = arr[i]
		j = i
		for (j > 0) && (arr[j-1] > x) {
			shiftsNumber = shiftsNumber + 1
			arr[j] = arr[j-1]
			j = j - 1
		}
		arr[j] = x
	}
	fmt.Printf("%d", shiftsNumber)
	return arr
}

func printArray(arr []int) {
	for i := range arr {
		fmt.Printf("%d ", arr[i])
	}
	fmt.Println()
}
