def booble_sort(arr):
    l = len(arr)
    i = l - 1
    while(i>=1):
        f = 0
        s = 1
        while(s<= i):
            if(arr[f]<arr[s]):
                f += 1
                s += 1
                continue
            else:
                temp = arr[f]
                arr[f] = arr[s]
                arr[s] = temp
                
                f += 1
                s += 1
        i = i - 1
    return arr

if __name__ == "__main__":
    arr = [50,10,91,80,43,65,8,93,72,64,81,65,2]
    output = booble_sort(arr)
    print(output)
    
                