N = list(map(int, input().split(",")))
f = 0
for i in range(len(N)-2):
    if N[i] == 1 and N[i+1] == 2 and N[i+2] == 3:
        f = 1
    else:pass
if f == 1:
    print(True)
else:
    print(False)
