N = list(map(int, input().split(",")))
f = 0
for i in range(len(N)-1):
    if N[i] == 2 and N[i+1] == 2:
        print(True)
        break
else:
    print(False)
