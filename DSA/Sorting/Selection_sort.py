def selection_sort(arr):
    length = len(arr)
    i = 0
    while(i < length):
        min_num = arr[i]
        index = i
        for j in range(i+1,length):
            if (min_num > arr[j]):
                min_num = arr[j]
                index = j

        arr[i],arr[index] = arr[index],arr[i]
        i += 1
        
    return arr

arr = [81,61,94,32,51,84,62,97]
output = selection_sort(arr)
print(output)
    
            
            