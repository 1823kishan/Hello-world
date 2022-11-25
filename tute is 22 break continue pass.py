#------BREAK----

av = 5
x = int(input('how many candis you want'))
i = 1
while i<=x:
    if i>av:
        print('out of stock')
        break
    print('candy')
    i+=1
print('bye')

#---------CONTINUE--------
for i in range(1, 101):
    if i%3==0 or i%5==0:#3 and 5 ne devide karata jeee avase tene print karase.
        continue
    print(i)
print('bye')

#-------PASS------

for i in range(1, 101):
    if i%2!=0:
        pass
    else:
        print(i)
print('bye')