l = [10,20,30,30,20,10,50]
d ={}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
print(d)