def Sum_Min_Max(n,lst):
    if n < 2:
        return lst[0]
    
    if(lst[0]<lst[1]):
        min_no = lst[0]
        max_no = lst[1]
    else:
        min_no = lst[1]
        max_no = lst[0]
    
    for i in range(2,n):
        if(lst[i]>max_no):
            max_no = lst[i]
        if(lst[i]<min_no):
            min_no = lst[i]
            
    return max_no+min_no
        
        

if __name__ == "__main__":
    n = int(input())
    arr = input()
    lst = list(map(int,arr.split(" ")))
    sum = Sum_Min_Max(n,lst)
    print(sum)