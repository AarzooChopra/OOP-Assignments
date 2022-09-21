"""
Dropping a Ball - Part B

h = height
u = initial speed
v = final speed
g = gravity
d = distance travelled
t = time

"""

import math
import matplotlib.pyplot as plt 

def main():
    
    t = 0
    tSteps = 0
    g = 10
    
    h, u, Ep = getInput()               #Call getInput()
    
    plt.xlabel('Time [s]') 
    plt.ylabel('Height [m]')
    
    while tSteps < 402:
        
        #Call motionSimulator()
        
        pos, v, t, g, d, tSteps = motionSimulator(h,u,g,t,tSteps,Ep)
        
        if pos != 0 or v != 0 or t != 0 or g != 0 or d != 0 or tSteps != 0:
            tTot = 0.04 * tSteps
            
            #Print results
            
            if pos == 'T' or pos == 'B':
                print(pos, '\t\t', format(v,'0.2f'), '\t\t', format(t,'0.2f') +
                      '\t\t', format(tTot,'0.2f'), '\t\t', tSteps)   
                
                u = v                           #Update u and g
                g = -g
                t = 0                           #Reset t
                
                if g == -10:                    #Update h if ball is going up
                    h = -(pow(u,2)/(2*g))
                    
            else: 
                plt.plot(tTot,d,'bo')           #Plot the graph
            
        else:
            break
        
#Get positive h, u and Ep from the user

def getInput():
    
    h = float(input('Please enter the initial height: '))
    
    while h < 0:
        h = float(input('Invalid Input\n\nPlease enter the initial height: '))
  
    u = float(input('Please enter the initial speed: '))
    
    while u < 0:
        u = float(input('Invalid Input\n\nPlease enter the initial speed: '))
        
    Ep = float(input('Please enter the % loss of energy as a decimal: '))
    
    while u < 0:
        Ep = float(input('Invalid Input\n\nPlease enter the % loss of energy as a decimal: '))
    
    print(' ')
    
    return h, u, Ep

#Simulate the motion of the ball

def motionSimulator(h,u,g,t,tSteps,Ep):
    
    for step in range(tSteps+1, 402):
        
        t += 0.04                               #Increment t

        #Calculate v and d
        
        v = u + (g * t)
        d = (u * t) + (0.5 * g * pow(t,2))
        
        #Check if ball is at the top or bottom position
        
        if v <= 0:
            v = 0
            pos = 'T'
            
        elif d >= h:
            pos = 'B'
            v = energyLoss(v,Ep)                #Call energyLoss()
                    
        #For the graph
        else:
            if g == 10:
                d = h - d
            
            pos = 'M'                               #Middle

        return pos, v, t, g, d, step
        
    return 0, 0, 0, 0, 0, 0                     #No more timesteps

#Calculate energy loss

def energyLoss(v,Ep):
    
    vf = math.sqrt(1-Ep) * v
    
    return vf
    
main()                                          #Call main()

