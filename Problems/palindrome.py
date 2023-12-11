import math

#palindrome - method 1 - in built
a = input("enter text to check")
reverse_string = ''.join(reversed(a))   
print(reversed(a))
print("reveresed string : ", reverse_string)
if a == reverse_string:
    print("palindrome")
else:
    print("not palindrome")





#palindrome - method 2
a = input("enter text to check")
flag = True
for i in range(0, math.ceil(len(a)/2)):
    if a[i]!=a[-(i+1)]:
        flag = False
if flag == True:
    print("palindrome")
else:
    print("not palindrome")
    



# Given number is odd or even
#***************************************************************************************************

number = int(input("enter number to check : "))
if number%2 == 0:
    print("Even")
else:
    print("odd")


