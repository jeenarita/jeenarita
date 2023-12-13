# integers = input()
# int_array = sorted([eval(i) for i in integers.split(" ")])

# factors1 = []
# factors2 = []

# for i in range(1, int(int_array[0]/2)+1):
#     if int_array[0] % i == 0:
#         factors1.append(i)
#     if int_array[1] % i == 0:
#         factors2.append(i)

# common_fact = set(factors1).intersection(set(factors2))
# print(len(common_fact))
import math
a,b = map(int,input().split())
# integers = input()
# int_array = sorted([eval(i) for i in integers.split(" ")])

n = 0

for i in range(1, math.ceil(min(a,b)/2)+1):
    print(i)
    if a % i == 0 and b % i ==0:
        n +=1

print(n)