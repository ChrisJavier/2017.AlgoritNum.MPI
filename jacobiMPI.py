from mpi4py import MPI
import numpy as np
import math as m
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


A = np.array([[10,1,3,2],[2,13,2,3],[2,3,17,3],[2,6,1,12]],dtype=float)
n = len(A)
b = np.array([1,6,2,7])
D = np.zeros((n,n))
D1 = np.diag(A)
Dinverse = D
for i in range(n):
    D[i][i]=D1[i]
    if(D1[i]!=0):
         Dinverse[i][i] = 1/float(D1[i])
X1=X0= np.zeros(n)
#compruebo si X es igual a cero valorando en la matriz A
def comprobar(X):
    global A
    global b
    global n
    sol =0.0
    for i in range(n):
        sol += np.dot(X,A[i]) - b[i]
    if sol>= -1e-10 and sol<1e-10:
        return True
    else:
        return False





#calculo los inicios y fin para cada proceso
inicio = int(m.floor(n/size))*rank
if rank !=size -1:
    fin    = inicio + int(m.floor(n/size))
else:
    fin = n

flag=False

#nota X1 con cada envio y recivo en la iteracion delos procesos
#tiene que llegar a converguer


while(flag==False):
    X0 = X1

    #cada proceso con su inicio y fin calcula su parte
    X1[inicio:fin] = X0[inicio:fin] + np.matmul(Dinverse[inicio:fin],b - np.matmul(A,X0))



    enviar = (X1[inicio:fin],inicio,fin)
    #envio a todos excepto a mi mismo (esto lo realiza cada proceso)
    #lo que calcule y mi inicio y fin
    for i in range(size):
        if i!=rank:

            comm.send(enviar, dest= i,tag=12)
    #recivo lo calculado de los otros y actualizo el X1
    #con los valores que calcularon los demas procesos

    for k in range(size):

        if(k!=rank):

            recivo = comm.recv(source=k,tag=12)
            aux = []
            for j in range(recivo[2]-recivo[1]):
                aux.append(recivo[0][j])
            X1[recivo[1]:recivo[2]]=np.array(aux)

    #verifico si ya convergue de manera que sale del while




    flag = comprobar(X1)


#se supone con cada envio y recivo X1 se actualiza por lo que al final debe mostrar el valor final



if rank == size -1:
    print "soluciones \n",X1
