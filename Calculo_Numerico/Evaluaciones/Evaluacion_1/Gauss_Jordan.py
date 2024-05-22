import numpy as np

def gauss_jordan(a, b):
    w = np.shape(a)
    A = np.c_[a, b]
    for i in range(w):
        for j in range(w):
            if (A[j,i] != 0 and A[ i, i] != 0 and i != j):
                f = A[j,i] / A[i,i]
                A[j, i+1: w+1] = A[j, i+1: w+1] - f * A[i, i+1: w+1]