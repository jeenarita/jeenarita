

#Prime or not
number = int(input("enter number to check prime or not"))
flag = False

if number>1:
    
    for i in range(2, int(number/2)):
        if number%i == 0:     
            flag = True
            break
            
if flag == True :
    print("not PRime number")
    
else:
    print(" Prime")