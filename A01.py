"""
1 - rock
2 - paper
3 - scissors
4 - spock
5 - lizard
"""

import random
import time

#convert choice number to choice name

def numToName(pnum):
    if pnum == 1:
        pc = 'rock'

    elif pnum == 2:
        pc = 'paper'
        
    elif pnum == 3:
        pc = 'scissors'

    elif pnum == 4:
        pc = 'spock'

    else:
        pc = 'lizard'
        
    return pc

#countdown and delay

print('\n3!')
time.sleep(1)
print('2!')
time.sleep(1)
print('1!')
time.sleep(1)
print('Go!')
time.sleep(1)

#generate a random numbers for player 1 and player 2

p1 = random.randint(1, 5)
p2 = random.randint(1, 5)

#check what Player 1 and 2 chose

p1c = numToName(p1)
p2c = numToName(p2)
    
#print the choices

print('\nPlayer 1 chooses ', p1c, '\n')
print('Player 2 chooses ', p2c, '\n')


#check who wins and print the result

if p1 != p2:                                #player 1 and 2 chose different moves?
    if p1 == 1:                             #player 1 chooses rock
        if p2 == 3 or p2 == 5:
            print('Player 1 Wins!')
        
        else:
            print('Player 2 Wins!')
    
    elif p1 == 2:                           #player 1 chooses paper
        if p2 == 1 or p2 == 4:
            print('Player 1 Wins!')
        
        else:
            print('Player 2 Wins!')
            
    elif p1 == 3:                           #player 1 chooses scissors
        if p2 == 2 or p2 == 5:
            print('Player 1 Wins!')
        
        else:
            print('Player 2 Wins!')
            
    elif p1 == 4:                           #player 1 chooses spock
        if p2 == 3 or p2 == 1:
            print('Player 1 Wins!')
        
        else:
            print('Player 2 Wins!')
            
    else:                                   #player 1 chooses lizard
        if p2 == 4 or p2 == 2:
            print('Player 1 Wins!')
        
        else:
            print('Player 2 Wins!')
            
else:
    print('It\'s a tie! Try again!!' )      #player 1 and 2 chose the same move
    
