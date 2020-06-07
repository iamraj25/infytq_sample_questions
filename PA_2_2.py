def close_number(num1, num2, num3):
    if abs(num1-num2) <= 1:
        if abs(num3-num1) >= 2 and abs(num3-num2) >= 2:
            return True
        else:
            return False
    elif abs(num1 - num3) <= 1:
        if abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2:
            return True
        else:
            return False
    elif abs(num2-num3) <= 1:
        if abs(num1-num2) >= 2 and abs(num1-num3) >= 2:
            return True
        else:
            return False
    else:
        return False
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(close_number(n1, n2, n3))

