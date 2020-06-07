def create(prices):
    dict1 = {}
    dict1= dict((k, v) for k, v in prices.items() if v>200)
    return dict1


n = int(input())
prices = {}
for i in range(n):
    k, v = input().split()
    prices[k] = float(v)
print(create(prices))

