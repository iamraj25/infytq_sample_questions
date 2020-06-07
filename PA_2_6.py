def find_gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return find_gcd(num2, num1 % num2)


num1 = int(input())
num2 = int(input())
print(find_gcd(num1, num2))