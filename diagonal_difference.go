package main

import "fmt"
import "math"

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([][]int, n)

	for i := range arr {
		arr[i] = make([]int, n)
	}

	for i := range arr {
		for j := range arr[i] {
			fmt.Scan(&arr[i][j])
		}
	}

	var sumPrimary, sumSecondary int
	sumPrimary, sumSecondary = 0, 0
	for i := range arr {
		sumPrimary = sumPrimary + arr[i][i]
		sumSecondary = sumSecondary + arr[i][n-i-1]
	}

	difference := sumPrimary - sumSecondary
	fmt.Printf("%d", int(math.Abs(float64(difference))))
}
