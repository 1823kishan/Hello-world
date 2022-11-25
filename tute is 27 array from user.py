from array import *
arr = array('i', [])
n = int(input('enter the lenght of the array'))#ketala array store karava che.
for i in range(n):
    x = int(input('eneter the next value'))
    arr.append(x)
print(arr)

val = int(input('eneter the value for search'))
k = 0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))#ana lidhe tamare for loop ni jarur padati nathi.
