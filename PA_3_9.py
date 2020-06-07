T = int(input())
lis =[]
if 1 <= T <= 200:
    for i in range(T):
        lis.append(input())
    for i in range(T):
        if lis[i][0].isupper():
            print(lis[i].upper())
        else:
            print(lis[i].casefold())