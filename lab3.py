'''
lab3
list and set
'''

#3.1
str_list = ['a','d','e','b','c']

str_list.sort()

print(str_list)

#3.2

str_list.append('f')
print(str_list)

#3.3

str_list.remove('d')
print(str_list)

#3.4

print(str_list[2])

#3.5

my_list= ['a','123',123,'b','B','False',False,123,None,'None']
print(len(set(my_list)))

#3.6

print(len("This is my third Python lab.".split()))

#3.7

num_list = [12,32,43,35]
print(num_list)
num_list.sort()
print(num_list)
print(num_list[0])
print

#3.8

game_board = [[0,0,0],[0,0,0],[0,0,0]]
print(game_board)
print(game_board[1])
game_board[1] = [0,1,0]
print(game_board)

print(game_board[1][1])