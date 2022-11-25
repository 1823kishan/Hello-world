#8 types of data type(none),(numeric),(list),(tuple),(set),(string),(range),(dictinoary).
#--------NONE--------

#--------NUMERIC-----
#int____
a = 5
print(type(a))
#float____
b = 7.7
print(type(b))
b = int(b)
#complex___
c = 9+6j
print(type(c))
#bool____
a = 5
b = 7
bool = a>b
bool = a<b
print(bool)
#--------list-----
lst = [23, 43, 67, 77]
print(type(lst))
#--------set------
s = {34, 65, 77, 78}
print(type(s))
#-------tuple-----
t = (32, 34, 67, 77)
print(type(t))
#------string-----
str = 'kishan'
print(type(str))
#------range------
range (0,10)
print(type(range(10)))
#------dictionary------
d = {'navin':'samsung', 'rahul':'iphone', 'kiran':'oneplus'}
print(d)
print(d.keys())#badhi key print karase.
print(d.values())#badhi vlue print karase.
print(d['kiran'])#particuler velue print karase.