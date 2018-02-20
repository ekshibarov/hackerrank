package main

import "fmt"

func main() {
	n := 3
	alice := make([]uint64, n)
	bob := make([]uint64, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&alice[i])
	}

	for i := 0; i < n; i++ {
		fmt.Scan(&bob[i])
	}

	alicePoints := 0
	bobPoints := 0

	for i := 0; i < n; i++ {
		if alice[i] > bob[i] {
			alicePoints = alicePoints + 1
		}

		if alice[i] < bob[i] {
			bobPoints = bobPoints + 1
		}
	}
	fmt.Printf("%d %d", alicePoints, bobPoints)
}
