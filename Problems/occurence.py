#Occurence count
#**************************************************************************************************
number_list = [1,2,3,4,2,3,4,2,3,4,2,2,2,1,1,'a','d','a','b']
number_to_check = input("enter the number to check")
if number_to_check.isnumeric():
    count = number_list.count(int(number_to_check))
else:
    count = number_list.count(number_to_check)

print("occurence of '%s' in the given list is %d:"  %(number_to_check, count))
oocurence = {}

list_wo_rep = set(number_list)

for each_num in list_wo_rep:
    oocurence[each_num] = number_list.count(each_num)

print("occurence of each element in the list: ",oocurence)