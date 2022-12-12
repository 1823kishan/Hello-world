data = {1:'navin', 2:'kiran', 4:'harsh'}
#print(data)
#print(data[4])# value saw karase.
print(data.get(1))#secound method for fetchin value.
print(data.get(3, 'not found'))#data no hoy to.
#-----------------------------------------------------------

#list to dictionary
keys = ['navin', 'kiran', 'harsh']
values = ['python','java', 'js']
data = dict(zip(keys, values))#list ne dictinory ma covert karase
#print(data)
#print(data['kiran'])
data['monika'] = 'cs'#add karase.
print(data)
del data['harsh']#data delet karase.
print(data)
#------------------------------------------------------------

#list in dictinory and dictionary in list
prog = {'js':'atom', 'cs':'vs', 'python':['pycharm', 'vs code'], 
'java':{'jse', 'notebens'}, 'jee':'eclipse'}
#print(prog['js'])#kyu ide ee print karase.
#print(prog['python'] [1])#keys ni andar pan index work kare che.
print(prog['java'])