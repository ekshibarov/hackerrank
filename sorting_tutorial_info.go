package main

import "fmt"

func main() {
	var v, n int
	fmt.Scan(&v)
	fmt.Scan(&n)

	arr := make([]int, n)

	for i := range arr {
		fmt.Scan(&arr[i])
	}

	for i := range arr {
		if arr[i] == v {
			fmt.Printf("%d", i)
			break
		}
	}
}
