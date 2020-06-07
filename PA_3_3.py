def bracket(str1):
    if str1[0] == ")" or str1[len(str1)-1] == "(":
        return False
    elif str1.count(")") == str1.count("("):
        return True
    else:
        return False


str1 = input()
print(bracket(str1))
