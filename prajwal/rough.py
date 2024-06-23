# def apply(lst):
#     final = []
#     d = {}
#     for i in lst:
#         j = i
#         i = list(i)
#         i.sort()
#         i = "".join(i)
#         d.setdefault(i,[])
#         d[i].append(j)
                        
#     print(d.values())   

# lst = ['raj','jar','om','mo','pizaa']
# apply(lst)

data = {'name':['suraj','kaju','dugu'],'age':[22,21,20]}
import pandas as pd
df = pd.DataFrame(data)