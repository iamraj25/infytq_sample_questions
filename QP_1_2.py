N = input().replace(" ","")
lis = []
for i in N:
    if N.count(i) > 1:
        lis.append(i)
    else:pass
lis = list(set(lis))
for i in N:
    for j in lis:
        if j == i:
            print(i, end=" ")
            lis.remove(j)