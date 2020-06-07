def counter(string):
    U, L, lis =0, 0, []
    for i in string:
        if i.isupper():
            U += 1
        elif i.islower():
            L += 1
        else:
            pass
    lis.append(U)
    lis.append(L)
    return lis

string = input()
print(counter(string))
