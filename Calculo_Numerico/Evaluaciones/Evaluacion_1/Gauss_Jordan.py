import numpy as np

class Gauss_Jordan:
    def __init__(self):
        self.a = ''
        self.b = ''
        self.matriz = []
    def set_Matriz(self, a):
        print(a)
        self.matriz = a
        self.a = np.array(a)
        self.b = self.a[:, -1]
        self.a = self.a[:, :-1]
        print(self.a)
        print(self.b)
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
        print(x)
        return x
"""
    def main(self):
        n,c=np.shape(self.a)
        r=np.linalg.matrix_rank(self.a)
        ab=np.c_[self.a,self.b]
        ra=np.linalg.matrix_rank(ab)

        print('rango (A) ={} rango (Ab) ={} n ={}'.format(r, ra, n))

        if (r == ra == n):
            print('solución única')
        x= self.gaussJordan()
        print(x)

        if (r == ra < n):
            print('múltiples soluciones')

        if (r < ra):
            print('sin solución')

    if __name__ == "__main__": 
        main()"""

