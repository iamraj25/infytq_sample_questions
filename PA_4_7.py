def sum_of_elements(num_list, number):
    sum = 0
    for i in range(1, n-1):
        if num_list[i] != number:
            if num_list[i-1] != number and num_list[i+1] != number:
                sum += num_list[i]
    if num_list[1] != number and num_list[0] != number:
        sum += num_list[0]
    if num_list[-2] != number and num_list[-1] != number:
        sum += num_list[-1]
    return sum


num_list = []
n = int(input())
for i in range(0, n):
    item = int(input())
    num_list.append(item)
number = int(input())
print(sum_of_elements(num_list, number))
