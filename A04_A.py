"""
Modeling Login Attempts

"""
from numba import jit
from tqdm import tqdm
import numpy as np
import math
import matplotlib.pyplot as plt

@jit
def main():
        
    S_true = getInputs()
    T, mu, A, B = setParameters()
    S_final, MSE_trend, A_final, B_final, mu_final, mse_final = getFit(T, mu, A, B)
    
    #Print the values
    print('\n\nThe value of A is: ', format(A_final, '0.2f'))
    print('The value of B is: ', format(B_final, '0.2f'))
    print('The value of mu is: ', format(mu_final, '0.2f'))
    print('The MSE predicted by our model is: ', format(mse_final, '0.3f'))
    
    t1 = [*range(0,120)]                    #x-axis for login attempts
    t2 = [*range(0,len(MSE_trend))]         #x-axis for MSE (iterations)

    #Plots
    plt.figure(figsize = (10,4))
    
    plt.subplot(1,2,1)
    plt.title('Login Attempts')
    plt.xlabel('Time')
    plt.ylabel('No. of Attempts')
    plt.plot(t1, S_true, 'bo', label = 'Data')
    plt.plot(t1, S_final, '--r', label = 'Model')
    plt.legend(loc = "lower left")
    
    plt.subplot(1,2,2)
    plt.title('Model Tuning')
    plt.xlabel('Iterations')
    plt.ylabel('MSE')
    plt.plot(t2, MSE_trend, '-b')
    
    plt.show()

@jit    
def getInputs():
    
    #Get inputs from file
    data1 = open('A04_sfwr_data_01.txt', 'r')
    
    s = data1.read()
    
    S_true = [float(n) for n in s.split('\n')]      #Convert string to float
    
    data1.close()
    
    return S_true

@jit      
def setParameters():
    
    #Set-up parameters 
    T = 120
    mu = list(np.arange(0, 2.05, 0.05))
    A = list(np.arange(0, 2.05, 0.05))
    B = list(np.arange(0, 2.05, 0.05))

    return T, mu, A, B

@jit  
def getFit(T, mu, A, B):
    
    n = 0                                           #Initialize counter
    
    S_true = getInputs()                            #Get data from file
    MSE_trend = []
        
    for muCalc in tqdm(mu):                         #Loop for mu values
        for ACalc in A:                             #Loop for A
            for BCalc in B:                         #Loop for B
                
                S_hat = []
                sDiff = [0]*T                       #Initialize difference list
                
                for t in range(T):                  #Loop for t
                    
                    #Calculate S_hat and add to list
                    S_hat.append(evaluateModel(T, muCalc, ACalc, BCalc, t))
                
                #Calculate MSE and keep track of the trend
                for i in range(T):
                    sDiff[i] = pow(S_hat[i] - S_true[i], 2)
                
                mse = (sum(sDiff))/T
                
                if n == 0:
                    
                    MSE_trend.append(mse)
                    msePrev = mse
                    
                    
                elif mse < msePrev:
                    
                    MSE_trend.append(mse)
                    msePrev = mse
                    
                    if mse < 1:
                        
                        #Keep track of optimal combination
                        if mse <= min(MSE_trend):
                            S_final = S_hat
                            A_final = ACalc
                            B_final = BCalc
                            mu_final = muCalc
                            mse_final = mse
                            
                n += 1
                

    return S_final, MSE_trend, A_final, B_final, mu_final, mse_final
                    
@jit      
def evaluateModel(T, mu, A, B, t):
    
    #Calculate S_hat
    kt = (2 * math.pi * t)/T
    
    S_hat = -((A * math.sin(kt) + mu) * math.exp(B * kt))
    
    return S_hat


main()