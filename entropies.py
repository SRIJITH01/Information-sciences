import math
import numpy as np

def Entropy(X):
	Y=0
	for i in range(len(X)):
		if X[i]==0:
			Y+=0
		else:
			Y+=(X[i]*math.log(X[i],2))
	Entropy = -Y
	return Entropy	

def cond_entropy(X,A):
	con=0
	for i in range(len(X)):
		for j in range(len(X)):
			con+=X[i]*(A[i,j]*math.log(A[i,j],2))
	return (-con)	
		
X = [0.08266906402,0.2769336515,0.6403972845]		
P = np.array([[0.1616880539,0.4343575576,0.4039543886],
             [0.3085662296,0.4748585777,0.2165751927],
             [0.5297457166,0.09078386473,0.3794704187]])
P1 = np.array([[0.1089720738,0.5196865747,0.3713413514],
             [0.7656101728,0.1966862846,0.03770354254],
             [0.1254177533,0.2836271407,0.590955106]])
                          
A = np.transpose(P)
Y = X@A
print(Y)
Hx = Entropy(X)
Hy = Entropy(Y)
Hy_x=cond_entropy(X,A)
Hxy= Hx+ Hy_x
Hx_y=Hxy - Hy
Ixy = Hx-Hx_y
print("H(X)",Entropy(X))
print("H(Y)",Hy)             	
print("H(Y|X)",Hy_x)
print("H(X,Y)",Hxy)
print("H(X|Y)",Hx_y)      			
print("I(X,Y)",Ixy)  
