import numpy as np
def mult_table(nrows, ncols):
    res = np.arange(1,nrows+1).reshape((nrows,1)) * np.arange(1,ncols+1).reshape((1,ncols))
    return res
    
exec(input().strip()) 