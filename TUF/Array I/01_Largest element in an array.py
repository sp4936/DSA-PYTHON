def largest_element_of_array(arr):
    
    # If size of array is zero then it return None
    if len(arr) == 0:
        return None
    
    # Set max_element to first index of an array
    max_element = arr[0]
    
    # Traverse the array using loop method and find the largest element by comparing previous largest element
    for i in arr:
        if i > max_element:
            max_element = i
    return max_element

if __name__=="__main__":
    print("Input an array ")
    arr = input()
    arr = list(map(int,arr.split(' ')))
    
    max_element = largest_element_of_array(arr) 
    print("Maximum number of an array is ",max_element)
    
    