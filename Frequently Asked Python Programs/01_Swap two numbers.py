first_number = int(input())
second_number = int(input())
#approach 1
# temp = first_number
# first_number = second_number
# second_number = temp

#apprach 2
first_number, second_number = second_number, first_number

print("first number after swap is ",first_number)
print("second number after swap is ",second_number)