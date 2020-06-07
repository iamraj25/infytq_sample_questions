def list_of_count(word_list):
    lis = []
    for i in word_list:
        lis.append(len(i))
    return lis

l = []
word_list = input().split(",")
for i in word_list:
    l.append(i)
print(list_of_count(word_list))