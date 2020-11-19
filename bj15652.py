n, m = map(int, input().split(' '))
check = [False] * (n + 1)
a = [0] * m

def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end = ' ')
        print()
        return
    
    for i in range(1, n + 1):
        if check[i]:
            continue
        a[index] = i
        for i in range(i):
            check[i] = True
        go(index + 1, n, m)
        for i in range(n + 1):
            check[i] = False

go(0, n, m) 