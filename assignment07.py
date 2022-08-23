'''
Assignment 07
Nicole Wong
Date Created: 22 Aug 2022
Last Modified: 23 Aug 2022
'''
import pickle

# data -----------------------
one = input('enter your first integer: ')
two = input('now enter your second integer: ')

# processing -----------------
try:
    quot = int(one) / int(two)
    #pickling-----------------
    fil = open('pickle.dat', 'ab')
    pickle.dump(quot, fil)
    fil.close()
    #end pickle---------------
    print(quot)
except Exception as e: 
    print('there seems to be an error')
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())