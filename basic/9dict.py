
# dictionary stores data in key value form.

dict1 = {'name':None, 'age':23 , 'city':'pune'}
dict2 = dict() # empty dict
dict2['name'] = None
dict3 = {}  #empty dict





print(dict1)
print(len(dict1)) # 3

print(dict1['age'])
print(dict1['name'])
print(dict1['city'])


dict1['cname'] = 'sinhgad'
print(dict1)
print(dict1.get('name'))

print(dict1.keys())
print(dict1.values())
print(dict1.items())


for k in dict1.keys():
    #print(dict1[k])
    if(dict1[k] == 'Suraj'):
        print('Suraj found')
        break
    else:
        print('Suraj not found')
        break

for k, v in dict1.items():
    print(k, v)




