"""
d = distance between A and B
v = speed of A
a = deceleration of A
t = time
s = distance travelled by A in t
"""

def main():
    
    #Ask what the user wants to do
    
    choose = int(input('To check if A and B will collide, press 1 \nTo find the critical value of \'a\', press 2 \n'))
    
    while choose != 1 and choose != 2:
        print('Invalid choice. Please try again')
        choose = int(input('To check if A and B will collide, press 1 \nTo find the critical value of \'a\', press 2 \n'))
    
    #Check user's choice
    
    #Check for collision
    
    if choose == 1:                                 
        
        d = getValD(5)
        v = getValV()
        t = getValT()
        
        #Get the value of a from user
        
        a = float(input('Please enter the deceleration of A in the range [-100, 0]: '))
    
        while a < -100 or a > 0:                    #Check if a is in range
            print('\nThe value is out of range')
            a = float(input('Please enter the deceleration of A in the range [-100, 0]: '))
            
        sTemp = (v*t)+(0.5*a*t*t)                   #Calculate s
        s = max(0, sTemp)
        
        #print('s = ',s)
        
        if s >= d:                                  #Check if A and B collide and print
            print('\nA and B will collide')
            
        else:
            print('\nA and B will not collide')
            
    #Calculate CV
    
    else:
        
        d = getValD(0)
        v = getValV()
    
        a = -50                                     #Initialize a and increments for a
        aInc = 0.02
    
        while a >= -50 and a <= 0:                  # While a is betwen -50 and 0
            t = 0                                   #Initialize t and increments for t
            tInc = 0.2
            
            while t <= 60:                          #While t is under 60 seconds
                sTemp = (v*t)+(0.5*a*t*t)           #Calculate s
                s = max(0, sTemp)
                
                if s == d:                          #Check if collision has occured yet
                    cv = a
                    break                           #If yes, break out of loop
                
                elif s < d:                         #If no, increment t
                    t += tInc
                    
                else:                               #If s is negative, break out of loop
                    break
                
            if s == d:                              #If collision, break out of loop
                break
            
            elif s < d:                             
                a += aInc                           #Increment a
                
            else:                                   #If s exceeds d, shorten aInc
                aInc = 0.5*aInc
                a -= aInc                           #Decrement a
        
        aBefore = a - 0.01
        aAfter = a + 0.01
        
        sBefore = max(0, (v*t)+(0.5*aBefore*t*t))
        sAfter = max(0, (v*t)+(0.5*aAfter*t*t))
        
        #Print the result
               
        print('\nThe objects will collide in ' + format(t, '0.2f') + ' s')
        print('\nThe critical value of \'a\' for object A is ' + format(cv, '0.2f') + ' m/s^2\n')
        
        #Verify the critical value
        
        print('With a deceleration of ' + format(aBefore, '0.2f')+
              ' m/s^2, the distance covered is ' + format(sBefore, '0.2f') + ' m')
        print('With a deceleration of ' + format(aAfter, '0.2f')+
              ' m/s^2, the distance covered is ' + format(sAfter, '0.2f') + ' m\n')
        
        print('This proves that at a deceleration of ' + format(a, '0.2f') +
              ' m/s^2, object A just touches object B')

#Get values of d, v and t from user and check if they are in range
    
def getValD(l):
    
    d = float(input('Please enter the distance between A and B in the range [' +
                    format(l) + ', 10]: '))
    
    while d < l or d > 10:
        print('\nThe value is out of range')
        d = float(input('Please enter the distance between A and B in the range [' +
                        format(l) + ', 10]: '))
        
    return d

def getValV():
    
    v = float(input('Please enter the speed of A in the range [1, 10]: '))

    while v < 1 or v > 10:
        print('\nThe value is out of range')
        v = float(input('Please enter the speed of A in the range [1, 10]: '))
    
    return v

def getValT():
    
    t = float(input('Please enter the time in the range (0, 10): '))

    while t <= 0 or t >= 10:
        print('\nThe value is out of range')
        t = float(input('Please enter the time in the range (0, 10): '))
    
    return t

main()    
   
