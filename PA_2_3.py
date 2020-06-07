def find_product(num1,num2,num3):
    if num1==7:
        return num2*num3
    elif num2==7:
        return num3
    elif num3==7:
        return -1
    else:
        return num1*num2*num3


n1,n2,n3=[int(x) for x in input().split(sep=',')]
product=find_product(n1,n2,n3)
print(product)