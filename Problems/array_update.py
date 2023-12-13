# n = input("enter array size")
# array_values = input("enter array values : ")

# array_elem = array_values.split(" ")[slice(int(n))]

# array_elem_new = [eval(i) for i in array_elem]
# if int(n) >=1 and int(n) <=1000000 and all(x < 1000 for x in array_elem_new) and len(array_elem_new)== int(n):
#     for i in range(1,int(n)):
#         new_array_sum = i * int(n) 
#         if new_array_sum > sum(array_elem_new):
#             print(i)
#             break



n = input()
array_values = input()

array_elem = array_values.split(" ")
array_elem_new = [eval(i) for i in array_elem]
for i in range(1,int(n)):
    print(i)
    new_array_sum = i * int(n) 
    if new_array_sum > sum(array_elem_new):
        print(i)
        break
    