s = input()
s1 = list(s)
s1.reverse()

s_reverse = "".join(s1)

if(s == s_reverse):
    print("String is palindrome")
else:
    print("Not Panlindrome")