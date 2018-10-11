import numpy as np
import fractions
from fractions import Fraction

A=np.matrix([[3,-2,1],[1,1,1],[3,-2,-1]])
B=np.matrix([[7],[2],[3]])


A_inverse=np.linalg.inv(A)

y=A_inverse * B

print(y)
# print(Fraction(x))
