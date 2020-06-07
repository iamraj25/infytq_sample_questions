def find(lis):
    for i in range(4):
        if lis[i] == 9:
            return True
    else:
        return False


lis = list(map(int, input().split(",")))
print(find(lis))