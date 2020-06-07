s = input().split()
s1 = input()
if s1 in s:
    if s1.isupper() or s1.islower() or s1.istitle():
        print(True)
    else:
        print(False)
else:
    print(False)