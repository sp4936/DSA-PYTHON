def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        pivot = lst[0]
        lesser = [x for x in lst[1:] if x<= pivot]
        greater = [x for x in lst[1:] if x> pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
lst = [51,46,19,84,9,65,14,89,63,4]
output = quick_sort(lst)
print(output)