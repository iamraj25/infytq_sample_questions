import math
N = int(input())
if N==0:
    print("$ "+str(0))
else:
    price = math.ceil((N*0.6*24)+3+(N-1)*0.75)
    print("$ "+str(price))
