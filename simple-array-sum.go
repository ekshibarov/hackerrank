package main
import "fmt"

func main() {
    var n int
    fmt.Scan(&n)
    arr := make([]uint64, n)

    for i:=0; i<n; i++ {
        fmt.Scan(&arr[i])
    }
    
    sum := 0
    for i:=0; i<n;i++ {
        sum = sum + int(arr[i])
    }
    fmt.Printf("%d", sum)
}