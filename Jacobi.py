# coding:utf8

import numpy as np
import math as m

EPS = 0.001
A = np.array ([[5, 5, 3], [5, -4, 1], [3, 1, 2]], "f")
iter = 0
while(1):
    iter = iter + 1
    print()
    print("ITERACIYA",iter)
    print()
    print("A = ",A)
    max = A[0][2]
    i = 0
    j = 2
    if(abs(A[1][2]) > abs(max)):
        max = A[1][2]
        i = 1
        j = 2
    if(abs(A[0][1]) > abs(max)):
        max = A[0][1]
        i = 0
        j = 1
    print("Max = ",max)

    x = max*2/(A[i][i]-A[j][j])
    f = 0.5*np.arctan(x)
    print("F = ",f)
    U = np.eye(3)
    U[i][i] = np.cos(f)
    U[i][j] = -np.sin(f)
    U[j][j] = np.cos(f)
    U[j][i] = np.sin(f)
    print("U=",U)
    UT = U.T
    A = np.dot(UT,A)
    A = np.dot(A,U)

    E = A[0][1]*A[0][1] + A[0][2]*A[0][2] + A[1][2]*A[1][2]
    eps = m.sqrt(E)
    print("Eps = ",eps)
    if(eps <= EPS):
        print()
        print()
        print("===========END===========")
        print()
        print(A)
        break

"""
b = np.array ([[0, 1, 2], [4, -1, 1]], "f")
print(b)


bt = b.T
print(bt)


c2 = np.dot(a, bt)
print(c2)
"""