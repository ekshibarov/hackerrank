package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	var sum int64
	sum = 0
	for i := 0; i < n; i++ {
		sum = sum + int64(arr[i])
	}
	fmt.Printf("%d", sum)
}
