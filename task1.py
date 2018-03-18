#
# Singular value decomposition tutorial
#

#
# Computing the singular value decomposition
#
import numpy as np

print("computing the svd")

m = np.array([[1.0,2.0,3.0,4.0],[3.0,4.0,5.0,6.0],[3.0,2.0,1.0,1.0]])
print(m)


U, s, V = np.linalg.svd(m, full_matrices = False)
D = np.diag(s)
print(U)
print(D)
print(s)
print(V)

print(np.dot(U,np.dot(D,V)))
print(m)
print(np.allclose(np.dot(U,np.dot(D,V)),m, 0.01))



#
# Approximation of matrix
#
'''
print("approximation of matrix using svd")
m = np.array([[1,2,3,2,1],[5,6,7,2,1],[9,10,11,9,8],[13,14,15,16,17]])
print(m)

U, d, V = np.linalg.svd(m, full_matrices = False)
d[3] = 0
D = np.diag(d)

print(U)
print(D)
print(d)
print(V)

print(U @ D @ V)
print(np.dot(U,np.dot(D,V)))
'''
