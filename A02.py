"""
d = distance between A and B
v = speed of A
a = deceleration of A
t = time
s = distance travelled by A in t
"""
#Get values of d, v and t from user and check if they are in range

def getVal():
    
    d = float(input('Please enter the distance between A and B in the range [5, 10]: '))

    while d < 5 or d > 10:
        print('\nThe value is out of range')
        d = float(input('Please enter the distance between A and B in the range [5, 10]: '))

    v = float(input('Please enter the speed of A in the range [1, 10]: '))

    while v < 1 or v > 10:
        print('\nThe value is out of range')
        v = float(input('Please enter the speed of A in the range [1, 10]: '))
        
    t = float(input('Please enter the time in the range (0, 10): '))

    while t <= 0 or t >= 10:
        print('\nThe value is out of range')
        t = float(input('Please enter the time in the range (0, 10): '))
        
    return d, v, t

####################################################################################

#Ask what the user wants to do

choose = int(input('To check if A and B will collide, press 1 \nTo find the critical value of a, press 2 \n'))

while choose != 1 and choose != 2:
    print('Invalid choice. Please try again')
    choose = int(input('To check if A and B will collide, press 1 \nTo find the critical value of a, press 2 \n'))

#Check user's choice

#Check for collision

if choose == 1:                                 
    
    d, v, t = getVal()
    
    #Get the value of a from user
    
    a = float(input('Please enter the deceleration of A in the range [-100, 0]: '))

    while a < -100 or a > 0:                    #Check if a is in range
        print('\nThe value is out of range')
        a = float(input('Please enter the deceleration of A in the range [-100, 0]: '))
        
    sTemp = (v*t)+(0.5*a*t*t)                   #Calculate s
    s = max(0, sTemp)
    
    print('s = ',s)
    
    if s >= d:                                  #Check if A and B collide and print
        print('A and B will collide')
        
    else:
        print('A and B will not collide')
        
#Calculate CV

else:                                           
    
    #loop = True
    
    #while loop:                                 #Loop till a CV is found         
    
        d, v, t = getVal()
       
        a = -50
        i = 0.2
        
        while a >= -50: #and a <= 0:
            
            sTemp = (v*t)+(0.5*a*t*t)            #Calculate s
            s = max(0, sTemp)
            #print(format(a, '0.2f'),'\t',s)    #<-Test
            
            if s == d:                          #a = critical value
                print('\nThe critical value is '+format(a, '0.2f')+' m/s^2')
                #loop = False
                break
                
            elif s < d:                         
                a += i                          #increase a
                    
            else:
                i = 0.5*i
                a -= i                          #decrease a
            #print(a,"\t\t", s)
            
            #if a > 0:                           #s!=d for all values of a within the range
                #print('\nThere is no critical value. Please try again')



