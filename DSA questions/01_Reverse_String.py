str = input("Enter a String")
str2 = str
str = str[::-1]
print(str)
print("--------------------------------------------")
# Apprach 2
lst = list(str2)
lst.reverse()
print("".join(lst))
