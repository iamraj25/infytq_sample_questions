str1 = input().split()
dict1 = {}
for i in str1:
    dict1[i] = []
for k in dict1.keys():
    for i in range(len(str1)):
        if k == str1[i]:
            dict1[k].append(i)
print(dict(sorted(dict1.items())))