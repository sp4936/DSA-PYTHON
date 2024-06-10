number = int(input("Enter a Number "))
i = 2

while i<number:
    if (number%i==0):
        print("The given number is not prime")
        break
    i += 1
if (i==number):
    print("Given number is Prime Number")