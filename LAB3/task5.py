import numpy as np
import matplotlib.pyplot as plt

import ortho_test as ot

#define constants
PI = np.pi
MUL = 3

#define signals params
T = 0.25

f = 1  / T

F_s = 1000

# set timeline
t = np.arange(0, T+0.3, 1/F_s)

k = [-6, 4, -2, 3, 5, 7]
n = [6, 4, -3, -5, 2, 5]

ot.ortho_test(k, n, F_s, f, t)
