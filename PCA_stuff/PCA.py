import numpy as np
from scipy import linalg

def calculate_PCA_SVD(raw_matrix):
    A = np.array(raw_matrix, dtype=np.float64)
    normalization_matrix(A)
    #добавить центрирование
    U, s, Vt = linalg.svd(A, full_matrices=False)
    V = Vt.T
    S = np.diag(s)
    T = np.dot(U,S)
    P = V
    #R = T.dot(P.T)
    return T, P



def normalization_matrix(A):
    col_sum = A.sum(axis=0)
    average_columns = A.sum(axis=0)[:] / float(A.shape[0])
    rationing =[]
    for j in range(A.shape[1]):
        s = 0
        for i in range(A.shape[0]):
            s += (A[i,j] - average_columns[j])**2
        s = (s/float(A.shape[0]))**0.5
        rationing.append(s)
    for j in range(A.shape[1]):
        for i in range(A.shape[0]):
            if rationing[j] ==0:
                A[i,j] = 0
            else:
                A[i,j] = (A[i,j] - average_columns[j]) / float(rationing[j])
