my_dict = {'Ivan': 2003,'Dima':1998,'Max':2004}
print(my_dict)
print(my_dict.get('Dima'))
my_dict.update({'Poly':2005,
                'Egor':2000})
print(my_dict)
(my_dict.pop('Dima'))
print(my_dict)


my_set = { 1,2,3,4,1,2,3, 'hous',(1,2,3,4,5,), True }
print(list(my_set))
my_set.add(6)
my_set.remove('hous')
print(my_set)