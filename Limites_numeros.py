# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:05:41 2021

@author: Julio C. Torreblanca
"""

#Esta parte calcula el underflow y overflow
n = 0
underflow = 1.0

while underflow != 0: 
    underflow /= 2
    n+=1

print(f"Underflow = {1/(2**(n-1))}")
print("-"*50)

m=0             
overflow = 1.0
                      
while overflow != float('inf'): 
    overflow *= 2
    m+=1
     
print(f"Overflow = {2.0**(m-1)}")
print("-"*50)

#Esta parte calcula la precisión de máquina

epsilon = 1.0
uno_computacional = 1.0 + epsilon

while uno_computacional != 1.0:
    epsilon = epsilon/2
    uno_computacional = 1 + epsilon
    
print(f"Epsilon = {epsilon*2}" )




