N = int(input())
print("* "*(2*N-1))
for i in range(N-1):
    for j in range(2*N-1,0,-1):
        if j < N-i or j > N+i:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
