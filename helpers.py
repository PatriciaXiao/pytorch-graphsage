#!/usr/bin/env python

"""
    helpers.py
"""

from __future__ import print_function

import numpy as np

import torch
from torch.autograd import Variable

def set_seeds(seed=0):
    np.random.seed(seed)
    _ = torch.manual_seed(seed)
    if torch.cuda.is_available():
        _ = torch.cuda.manual_seed(seed)


def to_numpy(x):
    '''
    if isinstance(x, Variable):
        return to_numpy(x.data)
    
    return x.cpu().numpy() if x.is_cuda else x.numpy()
    '''
    x_numpy = x.cpu() if x.is_cuda else x
    try:
        x_numpy = x.numpy()
    except:
        x_numpy = x.detach().numpy()
    return x_numpy

