#!/usr/bin/env python3
"""matrix concatenation"""


import numpy as np

def np_cat(mat1, mat2, axis=0):
    """concatenate two matrices"""
    import numpy as np
    return np.concatenate((mat1, mat2), axis=axis)
