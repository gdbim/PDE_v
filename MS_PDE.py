import numpy as np


def pack(a, b):
    """
    a and b are 2 arrays defined on the domain of size (nx,ny). Flatten will convert them into 2 vectors
    of sizes (nx*ny). Finally, concatenate will build a vector of size (2*nx*ny) containing the unknowns of both a and b.
    
    `flatten`: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html
    `concatenate`: https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
    """
    # TODO: return the concatenated array [a,b]

def unpack(X, steps):
    """
    X is a vector of size (2*nx*ny). The first nx*ny elements belong to a and the nx*ny following belong to b.
    X[:n] will be a vector of size (nx*ny). Reshape it will convert it to an array of size (nx,ny).
    
    `reshape`: https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
    `prod`: https://numpy.org/doc/stable/reference/generated/numpy.prod.html
    """
    # TODO: return the extracted arrays a and b


# Diffusion part of the MS model
def Div(v, r, dx2, dy2, nx, ny, scar):
    v[scar] = 0

    # d will be the result of the laplacian operator
    # We will fill its nx*ny elements
    d = np.empty((nx, ny))
    
    # TODO: implement the finite differences (9 cases)
    # 1. start with the interior of the domain
    # 2. shift the scheme for borders
    # 3. finally double shift for the corners

    d[scar] = 0
    return d
