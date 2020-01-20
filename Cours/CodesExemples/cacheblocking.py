import numpy as np

def fast_matrix_multiply_blocking(a, b,block):
    '''
    use blocking
    '''
    dim1=a.shape[0]
    dim2=b.shape[1]
    dim3=b.shape[0]
    dim4=a.shape[1]
    c = np.zeros((dim1,dim2))

    
    en1 = int(block * dim1/block)
    en2 = int(block * dim2/block)
    en3 = int(block * dim3/block)

    for ii in range(0, en1, block):
        for jj in range(0,en2,block):
            for kk in range(0, en3, block):
                for i in range(ii, ii + block):
                    for j in range(jj, jj + block):
                        sum = c[i,j]
                        for k in range(kk, kk + block):
                            sum += a[i,k] * b[k,j]
                        c[i,j] = sum
    return c
