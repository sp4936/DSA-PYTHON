def find_sum(a,s,l):
    for i in range(1,l-1):
        for j in range(i+1,l):
            if a[i] + a[j] == s:
                return True
    else:
        return False



if __name__ == "__main__":
    a = [10,20,30,40,50]
    s = 60
    l = len(a)
    
    if find_sum(a,s,l):
        print("sum exist")
    else:
        print("sum not exist")