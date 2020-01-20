import numpy as np

def baseline_matrix_multiply(a, b):
    '''
    baseline multiply
    '''
    dim1=a.shape[0]
    dim2=b.shape[1]
    dim3=b.shape[0]
    dim4=a.shape[1]
    c = np.zeros((dim1,dim2))
    for i in range(dim1):
        for j in range(dim2):
            for k in range(dim3):
                c[i,j] += a[i,k] * b[k,j]
    return c

