def Second_Largest_Smallest(arr):
    small, second_small = int('inf'), int('inf')
    large, second_large = int('-inf'), int('-inf')
    
    for num in arr:
        if num>large:
            second_large = large
            large = num
        elif num> second_large and num != large:
            second_large = num
            
        if num>large:
            second_large = large
            large = num
        elif num> second_large and num != large:
            second_large = num
    
    
        
    


if __name__=="__main__":
    print("Input an array ")
    arr = input()
    arr = list(map(int,arr.split(' ')))
    
    max_element = Second_Largest_Smallest(arr) 
    print("Maximum number of an array is ",max_element)
    
    