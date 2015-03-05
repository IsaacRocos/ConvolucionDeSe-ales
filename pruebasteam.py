#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
import math
import matplotlib.pyplot as plt

def graficarConvolucion():
	limiteSup = 5
	limiteInf = -5
	imp = [1,2,3,4,5,6,7,8,9,10,11]
	print type(imp)
	try:
		print "graficarConvolucion impulso"
		X = np.linspace(limiteInf, limiteSup , 11, endpoint=True)
		Y = np.array(imp)
		pl.stem(X,imp)
		#pl.step(X,imp)
		#fig, ax = plt.subplots()
		#ax.stem(X, Y)

		#plt.show()
		pl.show()

	except Exception as ex:
		print "Error inesperado en gaficarConvolucion(): " , type(ex)




graficarConvolucion()