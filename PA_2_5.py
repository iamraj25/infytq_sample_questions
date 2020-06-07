def divisible_by_sum(number):
    sum1 = 0
    temp = number
    while temp > 0:
        sum1 += temp % 10
        temp //= 10
    if number % sum1 == 0:
        return True
    else:
        return False


number = int(input())
print(divisible_by_sum(number))