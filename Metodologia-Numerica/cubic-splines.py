import numpy as np

x = np.array([1,3,5,8])
y = np.array([2,3,9,10])

# Number of splines
n = len(x) - 1

# N splines 
# a0*x³ + b0*x² + c0*x + d0 -> [a0, b0, c0, d0]
splines = np.zeros((n, 4), dtype=float)

########### GET EQUATIONS #############

equations = np.zeros((4*n,4*n + 1),dtype=float)
# equations = [[equation0], [equation1], ..., [euqationN-1]]
# equationN = [a0, b0, c0, d0, a1, b1, c1, d1, ..., an-1, bn-1, cn-1, dn-1, r]
# r is the constant


# Pn(xn) = yn
for i in range(n):
    # Pn(xn) = yn
    # equation = [x[i]**3, x[i]**2, x[i], y[i]]
    equations[2*i][i*4]     = x[i]**3
    equations[2*i][i*4 + 1] = x[i]**2
    equations[2*i][i*4 + 2] = x[i]
    equations[2*i][i*4 + 3] = 1
    equations[2*i][4*n] = y[i]

    # Pn(xn+1) = yn+1
    equations[2*i+1][i*4]     = x[i+1]**3
    equations[2*i+1][i*4 + 1] = x[i+1]**2
    equations[2*i+1][i*4 + 2] = x[i+1]
    equations[2*i+1][i*4 + 3] = 1
    equations[2*i+1][4*n] = y[i]

print(equations)
