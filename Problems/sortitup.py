def sort_it_up(n,arr):
    left_bound = 0
    right_bound = n-1
    current = 0
       
    while current <= right_bound:
        if arr[current] == 2:
            temp = arr[right_bound]
            arr[right_bound] = arr[current]
            arr[current] = temp
            right_bound -= 1
            # current += 1
        elif arr[current] == 0:
            temp = arr[left_bound]
            arr[left_bound] = arr[current]
            arr[current] = temp
            left_bound += 1
            current += 1
        else:
            current += 1
    return arr
            
            
n = 5
arr = [2,2,0,1,2]
print("SORT IT UP", sort_it_up(n, arr))