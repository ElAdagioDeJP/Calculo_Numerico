import numpy as np

def gauss_jordan(a, b):
    w = np.shape(a)
    A = np.c_[a, b]
    for i in range(w):
        for j in range(w):
            if (A[j,i] != 0 and A[ i, i] != 0 and i != j):
                f = A[j,i] / A[i,i]
                A[j, i+1: w+1] = A[j, i+1: w+1] - f * A[i, i+1: w+1]
    x = np.zeros(w)
    for i in range(w):
        x[i] = A[i,w] / A[i,i]
    return x
def main():
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    b = np.array([1,2,3])
    w = np.shape(a)
    r = np.linalg.matrix_rank(a)
    ab = np.c_[a,b]
    ra = np.linalg.matrix_rank(ab)
    
    print('rango (A) = {} rango (Ab) = {} w = {}'.format(r,ra,w))
    
        
    