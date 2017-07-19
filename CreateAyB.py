# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:27:19 2017

@author: User
"""
import numpy as np
#==============================================================================
# Este metodo crea un metodo a partir de un tamanio en un rango de 0, 99
#==============================================================================
def matrizC(n):
    sum=0
    A=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if(i==j):
                A[i][j]=np.random.randint(100*n,150*n)
            else:
                A[i][j]=np.random.randint(0,20)
            if j!=i:
                sum+=A[i][j] 
                
        sum=0
    return A    

#==============================================================================
# Este metodo crea un vector b para la matriz
#==============================================================================
def vectorB(n):
    A=np.zeros(n)
    A= np.random.randint(100,size=n)
    return A 


n=4
A=matrizC(n)
archivo= open("matrizA.txt","w")
for i in range(n):
    for j in range(n):
        if(j+1==n):
            archivo.write(str(A[i][j])+"\n")
        else:
             archivo.write(str(A[i][j])+";")
archivo.close

B=vectorB(n)
archivo1=open("vectorB.txt","w")
for i in range(n):
        if(i+1==n):
            archivo1.write(str(B[i])+"\n")
        else:
             archivo1.write(str(B[i])+";")
             
archivo1.close