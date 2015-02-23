#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
import math

listaSenialesContinuas = []

#Funcion principal para convolución de señales continuas.
#Invoca a la funciónes correspondientes a la selección del usuario para generar su señal.
def continuas():
	print "\n------------------\nSEÑALES CONTINUAS\n------------------\n"
	print "1)Seno [Sin(t)] \n2)Coseno[Cos(t)] \n3)Compuerta[ACd(t)] \n4)Recta[t] \n5)Exponencial[e^t]"
	entrada = input('>>Seleccion[s1,s2]: ')
	seniales = {1 : creaFunSeno,
                2 : creaFunCoseno,
                3 : creaFunCompuerta,
                4 : creaFunRecta,
                5 : creaFunExponencial,
	}
	try:
		seniales[int(entrada[0])]()
		seniales[int(entrada[1])]()
		pl.show()
	except KeyError:
		print "Valor no definido como opcion"
	except Exception as ex:
		print "Error inesperado en funcion: Continuas"

def creaFunSeno():
	print "Señal Seno"
	intervalo = input('>>Intervalo[li1,ls]: ')
	numeroMuestras = input('>>Muestras: ')
	X = np.linspace(intervalo[0], intervalo[1], numeroMuestras, endpoint=True)
	S = np.sin(X)
	pl.plot(X,S)
	listaSenialesContinuas.append(S)

def creaFunCoseno():
	print "Señal Coseno"
	intervalo = input('>>Intervalo[li1,ls]: ')
	numeroMuestras = input('>>Muestras: ')
	X = np.linspace(intervalo[0], intervalo[1], numeroMuestras, endpoint=True)
	C = np.cos(X)
	pl.plot(X,C)
	listaSenialesContinuas.append(C)

def creaFunCompuerta():
	print "Aun no definida"

def creaFunRecta():
	print "Aun no definida"

def creaFunExponencial():
	print "Aun no definida"

def discretas():
	print "Discretas no definidas aún"


def main():
	print "\n**************\n* CONVOLUCION *\n**************\n"
	print ">>Seleccione el tipo de señales que quiere usar:"
	print "1)Señales continuas\n2)Señales discretas"
	opciones = {1 : continuas,
                2 : discretas,
	}
	try:
		opciones[int(input())]()
	except KeyError:
		print "Valor no definido como opcion"
	except Exception as ex:
		print "Error inesperado: " , type(ex)


def prueba():
	lista1 = [1,0,-1,0,1,0,-1] #coseno(nPI)
	lista2 = [0,1,0] #impulso desplazado
	lista3 = []
	for i in range(len(lista1)+len(lista2)-1):
		lista3.append(0)
	convoluciona(lista1,lista2,lista3)
	imrpimeRes(lista3)

#Funcion que convoluciona dos señales.
def convoluciona(senial1,senial2,senialRes):
    i=0
    j=0
    for i in range (len(senial1)):
    	for j in range (len(senial2)):
            senialRes[i+j]=senialRes[i+j]+senial1[i]*senial2[j]

def graficar(senial1,senial2,senialRes):
	print ""

#Imprime los elementos de una lista, en este caso, se usa para imprimir el resultado de la convolucion.
def imrpimeRes(resultado):
	for valor in resultado:
		print valor


main()