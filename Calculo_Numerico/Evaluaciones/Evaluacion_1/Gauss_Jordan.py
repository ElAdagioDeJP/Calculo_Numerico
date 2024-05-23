import numpy as np

class Gauss_Jordan:
    def __init__(self):
        self.a = ''
        self.b = ''
        self.matriz = []
    def set_Matriz(self, a):
        self.matriz = a
        self.a = np.array(a)
        self.b = self.a[:, -1]
        self.a = self.a[:, :-1]
        return self.a, self.b


    def gaussJordan (self):
        n,_=np.shape(self.a)
        A=np.array(self.matriz)
        for i in range(n):
            for j in range(n):
                if (A[j,i] != 0 and A[i,i] != 0 and i != j):
                    f=A[j,i]/A[i,i]
                    A[j,i+1:n+1]= A[j,i+1:n+1] - f*A[i,i+1:n+1]
        x=np.zeros(n)
        for i in range(n):
            x[i]=A[i,n]/A[i,i]
        return x