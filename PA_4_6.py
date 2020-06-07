def exchange_list(number_list):
    for i in range(n//2):
        number_list[i], number_list[n//2 + i] = number_list[n//2 + i], number_list[i]
    number_list[0], number_list[2] = number_list[2], number_list[0]
    return number_list

number_list = []
n = int(input())
for i in range(0, n):
    item = int(input())
    number_list.append(item)

print(exchange_list(number_list))