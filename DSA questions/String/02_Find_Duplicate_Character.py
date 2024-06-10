def Find_Duplicate_elementes(s):
    
    dict  = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    lst = []
    for char,value in dict.items():
        if value > 1:
            lst.append(char)
    return lst

if __name__ == "__main__":
    s = input()
    output= Find_Duplicate_elementes(s)
    print(output)