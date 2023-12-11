import math

#palindrome - in built
a = input("enter text to check")
reverse_string = ''.join(reversed(a))   
print(reversed(a))
print("reveresed string : ", reverse_string)
if a == reverse_string:
    print("palindrome")
else:
    print("not palindrome")





# #palindrome
# a = input("enter text to check")
# flag = True
# for i in range(0, math.ceil(len(a)/2)):
#     if a[i]!=a[-(i+1)]:
#         flag = False
# if flag == True:
#     print("palindrome")
# else:
#     print("not palindrome")
    




# #Prime or not
# number = int(input("enter number to check prime or not"))
# flag = False

# if number>1:
    
#     for i in range(2, int(number/2)):
#         if number%i == 0:     
#             flag = True
#             break
            
# if flag == True :
#     print("not PRime number")
    
# else:
#     print(" Prime")












# x = 2
# x+=1 
# print(x)




# # Given number is odd or even
# #***************************************************************************************************

# number = int(input("enter number to check : "))
# if number%2 == 0:
#     print("Even")
# else:
#     print("odd")



# #***************************************************************************************************


#Occurence count
#**************************************************************************************************
#number_list = [1,2,3,4,2,3,4,2,3,4,2,2,2,1,1,'a','d','a','b']
# number_to_check = input("enter the number to check")

# count = number_list.count(int(number_to_check))
# print(count)
# print(type(number_to_check))


# oocurence = {}

# list_wo_rep = set(number_list)
# print(list_wo_rep)

# for each_num in list_wo_rep:
#     oocurence[each_num] = number_list.count(each_num)

# print(oocurence)
#************************************************************************************************** 


group the keys of same values
******************************
dict = {'a':1, 'b':2, 'd':3, 'c':2 }
print(dict.get(2))
result = {}
for key, value in dict.items():
    result[value] = result.get(value, []) + [key]
    print(value)
    print("result.get(value, [])----",result.get(value, []))
    print("reslt[value]---",result[value])
    print(result)

print(result)
*****************************************************************************************************



def group_by_owners(files):
    result = {}
    for key, value in files.items():
        result[value] = result.get(value, []) + [key]
    
    return result

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
