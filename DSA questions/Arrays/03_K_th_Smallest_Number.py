def Kth_smallest(n,lst):
    lst.sort()
    return(lst[n-1])

if __name__ == "__main__":
    n = int(input())
    arr = input()
    lst = list(map(int,arr.split(" ")))
    no = Kth_smallest(n,lst)
    print(no)