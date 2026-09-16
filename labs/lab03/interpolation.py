import numpy as np

def lagrange_basis(X, j, x):
	"""
	Compute the j-th Lagrange basis polynomial at x.
	"""
	n = len(X) - 1
	L = np.ones_like(x)
	for i in range(n+1):
		if i!=j:
			L *= (x-X[i])/(X[j]-X[i])
	return L

def lagrange_interp(X, Y, x):
	"""
	Compute the Lagrange interpolant of the data (X, Y) evaluated at x.
	"""
	n = len(X) - 1
	p = np.zeros_like(x)
	for j in range(n+1):
		p += Y[j]*lagrange_basis(X,j,x)
	return p