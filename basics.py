# dict1 = {}
# N = int(input(" Enter Number of Elements: "))
# for i in range(N):
#     key, value = input().split(" ")
#     dict1.update({key: int(value)})
# print(dict1)
# dict1 = dict((k, v) for k, v in dict1.items() if v >= 200)
# print(dict1)


# import math
# lis = ['Mysore','Bangalore','Pune','Chennai']
# lis.sort()
# print(lis)
# c1 = len(lis[0])
# c2 = len(lis[-1])
# print(math.ceil(c1/c2))


# import numpy as np
# lis = list(map(int, input().split()))
# n = len(lis)
# lis =np.array(lis)
# for i in range(n-8):
#     temp = lis[i:i + 9]
#     np.reshape(temp, (3, 3))
#     if i + 9 <= n:
#         print(temp)

# x = input().split(" ")
# for i in x:
#     if '@' in i:
#         print(i)
#     else:pass

# lis = list(map(int, input().split()))
# print(list(map(lambda x: x*2, lis)))

# class change:
#     def __init__(self):
#         self.a = 'old'
#         self.disp(self.a)
#     def disp(self,var):
#         var  = 'new'
# x= change()
# print(x.a)


# di = {'Name':'Abc','Id':123,'Marks':'90%'}
# print("Name:",di.setdefault('Name',None))
# print("Subject:",di.setdefault('Subject',None))
# print(di)


l = [2445,133,12454,123]
print(max(l))