'''
lab 5

if statements
'''

#3.1

alien_color = 'green'

if alien_color == 'green' :
    print('you have earned 5 points!!')

#3.2

if alien_color == 'green' :
    print('you have earned 5 points!!')
    
else:
    print('you have earned 10 points!!')
    
#3.3

favorite_fruits = ['apple','mango','pineapple']

if 'apple' in favorite_fruits:
    print('mangos are awesome')

if 'prune' in favorite_fruits:
    print('you are a liar')
    
if 'pineapple' in favorite_fruits:
    print('this is an exquisite fruit')
    
#3.4

Sebastian_Stan = 39

if Sebastian_Stan<10 :
    print('he is a kid')
    
elif 10<=Sebastian_Stan<20 :
    print('he is a teenager')

elif 20<=Sebastian_Stan :
    print('he is an adult')
    
if Sebastian_Stan >= 65 :
    print('he is also an elder')