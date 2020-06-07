def seed_no(number, ref_no):
    product = number
    temp = number
    while temp > 0:
        product = product*(temp % 10)
        temp //= 10
    if product == ref_no:
        return True
    else:
        return False


n1, n2 = input().split(",")
number = int(n1)
ref_no = int(n2)
print(seed_no(number, ref_no))