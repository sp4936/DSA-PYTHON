def find_sum(a,s,leth):
    a.sort()
    print(a)
    l = 0
    r = leth-1
    while(l<r):
        if a[l] + a[r] == s:
            return True
        elif a[l] + a[r] < s:
            l += 1
        elif a[l] + a[r] > s:
            r -= 1
    return False


if __name__ == "__main__":
    a = [20,90,80,40,5]
    s = 60
    l = len(a)
    
    if find_sum(a,s,l):
        print("sum exist")
    else:
        print("sum not exist")