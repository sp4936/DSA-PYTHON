def Sum_Min_Max(n,lst):
    return max(lst)+min(lst)

if __name__ == "__main__":
    n = int(input())
    arr = input()
    lst = list(map(int,arr.split(" ")))
    sum = Sum_Min_Max(n,lst)
    print(sum)
    