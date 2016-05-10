
import numpy as np
import pylab as plt
import math
from sklearn import *

W = [ 1,2,3,4,5,6]
LAST = 3

def sigmoid(x):
	return 1/(1+math.exp(-x)

def dif_sigmoid(x):
	return sigmoid(x)*(1-sigmoid(x))

def Xi(j,X,W):
	res = 0
	for i in range(len(X)):
		res += W[i]*X[i]
	return res

def Output(i,j,X,W):
	if i == 1:
		return X[j]
	return sigmoid(Xi(j,X,W))

def ErrorDiff(i,j,X,W,Y):
	if i == LAST:
		return X[j] - Y[j]
	else:
		res = 0
		for k in range(len(X)):
			res += W[j]*ErrorDiff(i,k,X,W,Y)
		return res*dif_sigmoid(Xi(j,X,W))


