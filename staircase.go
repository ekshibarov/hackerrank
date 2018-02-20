package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	var counter int
	counter = n

	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if j < counter {
				fmt.Print(" ")
			}
			if j >= counter {
				fmt.Print("#")
			}
		}
		counter = counter - 1
		fmt.Println()
	}
}
