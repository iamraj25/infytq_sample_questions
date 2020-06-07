n,k=map(int,input().split())
if n & (1 << (k - 1)):
    print("SET")
else:
    print("NOT SET")
