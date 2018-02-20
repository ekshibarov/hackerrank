package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	arr := make([]int, n)

	for i := range arr {
		fmt.Scan(&arr[i])
	}

	var x, j int
	for i := range arr {
		x = arr[i]
		j = i
		for (j > 0) && (arr[j-1] > x) {
			arr[j] = arr[j-1]
			printArray(arr)
			j = j - 1
		}
		arr[j] = x
	}
	printArray(arr)
}

func printArray(arr []int) {
	for i := range arr {
		fmt.Printf("%d ", arr[i])
	}
	fmt.Println()
}
