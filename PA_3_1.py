str1 = input()
if len(str1) < 3:
    print(str1)
elif str1[-3:] == "ing":
    print(str1+"ly")
elif str1[-3:] != "ing":
    print(str1+"ing")