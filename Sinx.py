# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:47:15 2021

@author: Julio C. Torreblanca
"""
import math

def coef_n(n: int,x: float ) -> float:
    """Esta función calcula recursivamente el n-ésimo coeficiente 
    del desarrollo en series de potencias de la función sen(x)"""
    a_n=0
    if x == 0.0: #Si x=0, entonces todo vale cero
        return a_n
      
    if n ==1:
        a_n = x
        return a_n 
    
    if n == 2:
        a_n = -x**3/6
        return a_n
  
    if n > 2:
       a_n = -(x**2)/( (2*n - 2) * (2*n - 1) ) * coef_n(n-1,x)

    return a_n

def suma(n: int, x: float)-> float:
    """Esta función suma los primeros n términos del desarrollo en 
    serie de potencias de la función sen(x)"""
    suma = 0.0
    
    if x == 0.0:
      return suma  
    
    for i in range(n):
        suma += coef_n(i+1,x)
    return suma

def n_lim(x = 1.0, n = 1) ->int:
    """Esta función obtiene el número n que hace referencia a la cantidad 
    de términos que debe considerarse en el desarrollo en series de potencias
    de la función sen(x) para tener una paroximación con error absolto menor a 
    una parte en 10^8"""
    
    if x == 0.0:
        return 0
    
    while True:
        try: 
            if abs(coef_n(n,x)/suma(n-1, x)) > 10**(-8):
                n += 1
            else:
                break
        except ZeroDivisionError:
            n += 1        
    return n
 
def sen_serie_potencias(x: float)->float:
    """Esta función obtiene una aproximación para sex(x) mediante el 
    desarrollo por serie de potencias"""
    


    if abs(x) >= 2 * math.pi:
        x2 = math.floor(abs(x/(2*pi))) #este me da el entero 2n pi
        if x>0:
            x = x - 2*x2*pi
        else:
            x = x + 2*x2*pi
    
    p1="N"
    p2="suma(N)"
    p3="error relativo"   
    print("Error rabsolto menor a 10^(-8):")     
    print(f"{p1:>3} | {p2:^25} | {p3:^25}") #Esto solo nos imprime los títulos de la tabla
    n = n_lim(x)
    senx = math.sin(x)#Esta variable nos almacenará el valor de sinx de python para obtener el error relativo
    for i in range(1,n+1):
        s = suma(i,x)
        
        
        if x == 0:
            error = 0
        else:
            error = abs((s - senx)/senx)
        print(f"{i:3d} | {s:25.15f} | {error:25.15f}")#Esto imprime los valores de la tabla




#aquí calculamos el error de máquina para el inciso (c)
epsilon = 1.0
uno_computacional = 1.0 + epsilon

while uno_computacional != 1.0:
    epsilon = epsilon/2
    uno_computacional = 1 + epsilon


#estas son la funciones modificadas para el inciso (c)    
def n_lim_modificada(x = 1.0, n = 1) ->int:
    """Esta función obtiene el número n que hace referencia a la cantidad 
    de términos que debe considerarse en el desarrollo en series de potencias
    de la función sen(x) para tener una aproximación con error absoluto menor a 
    una parte en 10^8"""
    
    if x == 0.0:
        return 0
    
    while True:
        try: 
            if abs(coef_n(n,x)/suma(n-1, x)) > epsilon: #modificación
                n += 1
            else:
                break
        except ZeroDivisionError:
            n += 1        
    return n    

def sen_serie_potencias_modificada(x: float)->float:
    """Esta función obtiene una aproximación para sex(x) mediante el 
    desarrollo por serie de potencias"""
    


    if abs(x) >= 2 * math.pi:
        x2 = math.floor(abs(x/(2*pi))) #este me da el entero 2n pi
        if x>0:
            x = x - 2*x2*pi
        else:
            x = x + 2*x2*pi
    
    n = n_lim_modificada(x)#parte modificada
    senx = math.sin(x) #Esta variable nos almacenará el valor de sinx de python para obtener el error relativo
    p1="N"
    p2="suma(N)"
    p3="error relativo"    
    print(f"Error absoluto menor a {epsilon} (error de máquina):")  
    print(f"{p1:>3} | {p2:^25} | {p3:^25}") #Esto solo nos imprime los títulos de la tabla
    for i in range(1,n+1):
        s = suma(i,x)
        
        if x == 0:
            error = 0
        else:
            error = abs((s - senx)/senx)
        print(f"{i:3d} | {s:25.15f} | {error:25.15f}")#Esto imprime los valores de la tabla




#En esta parte clacularemos el valor de sinx para ambos casos de los errores absolutos
pi = math.pi
x = - (33*pi/2) #Para calcular el valor de senx solo ingrese el valor de x


sen_serie_potencias(x)
print("-"*70)
sen_serie_potencias_modificada(x)





    