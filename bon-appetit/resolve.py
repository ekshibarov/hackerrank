if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    b = int(input().strip())
    pick = c.pop(k)
    total = 0
    for price in c:
        total += price

    actual = total / 2
    if (b > actual):
        print(int(b - actual))
    else:
        print("Bon Appetit")
