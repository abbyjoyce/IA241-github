'''
lecture 4
dictionary and tuple
'''

my_tuple = 'a','b','c','d','e'
print(my_tuple)

my_2nd_tuple = ('a','b','c','d','e')
print(my_2nd_tuple)

#not_a_tuple = ('a')

is_a_tuple = ('a',)
print(is_a_tuple)

print(my_tuple[1])
print(my_tuple[1:3])
print(my_tuple[ :3])
print(my_tuple [ : ])

my_car = {'color':'silver','maker':'toyota','year':2019}

print(my_car['year'])
print(my_car['color'])
print(my_car['maker'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get('year'))

my_car['model'] = 'Corolla'
print(my_car['model'])
print(my_car)

print (len(('this is a string').split()))
lambda = 1
print(lambda)