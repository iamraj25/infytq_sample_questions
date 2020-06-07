def check_occurence(string):
    J, M = 0, 0
    for i in range(len(string)):
        if string[i] == "Jet" or string[i] == "jet":
            J += 1
        elif string[i] == "Mat" or string[i] == "mat":
            M += 1
        else:
            pass
    if J == M:
        return True
    else:
        return False
string = input().split(" ")
print(check_occurence(string))
