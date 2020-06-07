N = input()
l, d, lis = 0, 0, []
for i in N:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1
    else:
        pass
lis.append(l)
lis.append(d)
print(lis)