package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	plusCount, minCount, zeroCount := 0, 0, 0
	for i := range arr {
		if arr[i] > 0 {
			plusCount = plusCount + 1
		}
		if arr[i] < 0 {
			minCount = minCount + 1
		}
		if arr[i] == 0 {
			zeroCount = zeroCount + 1
		}
	}

	fmt.Println(float32(plusCount) / float32(n))
	fmt.Println(float32(minCount) / float32(n))
	fmt.Println(float32(zeroCount) / float32(n))
}
