import numpy as np
from scipy import linalg

def calculate_PCA_SVD (row_matrix):
    A = np.array(row_matrix)

    M,N = A.shape
    U,s,Vh = linalg.svd(A)
    Sig = linalg.diagsvd(s,M,N)
    P = Sig.dot(Vh)
    T = U
    r = T.dot(P)
    return T,P,r



