N = int(input())
for i in range(N):
    for j in range(i, 0, -1):
        print(2**(j-1), end=" ")
    print()
