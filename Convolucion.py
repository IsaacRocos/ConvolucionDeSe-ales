#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
import math

#Lista que almacena las seniales y su convolucion. Las seniales son de tipo np.array
listaSenialesContinuas = []
limite = 0

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
		convoluciona(listaSenialesContinuas)
		graficarConvolucion(listaSenialesContinuas[2])
		pl.show()
	except KeyError:
		print "Valor no definido como opcion"
	except Exception as ex:
		print "Error inesperado en funcion: Continuas" , type(ex)

def creaFunSeno():
	print "|Señal Seno|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limite 
	limite = limite + intervalo
	X = np.linspace(0, intervalo, 50, endpoint=True)
	S = np.sin(X)
	amplificar(S,amplitud)
	pl.plot(X,S)
	listaSenialesContinuas.append(S)

def creaFunCoseno():
	print "|Señal Coseno|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limite 
	limite = limite + intervalo
	X = np.linspace(0, intervalo, 50, endpoint=True)
	C = np.cos(X)
	amplificar(C,amplitud)
	pl.plot(X,C)
	listaSenialesContinuas.append(C)

def creaFunCompuerta():
	print "|Señal Compuerta|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limite 
	limite = limite + intervalo
	X = np.linspace(0, intervalo, 50, endpoint=True)
	tabAmplitud = []
	for i in range (len(X)):
		tabAmplitud.append(amplitud)
	C = np.array(tabAmplitud)
	pl.plot(X,C)
	listaSenialesContinuas.append(C)

def creaFunRecta():
	print "|Señal Recta|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limite 
	limite = limite + intervalo
	X = np.linspace(0, intervalo, intervalo, endpoint=True)
	C = []
	for i in range (len(X)):
		C.append(X[i])
		print C[i]
	amplificar(C,amplitud)
	pl.plot(X,np.array(C))
	listaSenialesContinuas.append(C)	


def creaFunExponencial():
	print "|Señal Exponencial|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limite 
	limite = limite + intervalo
	X = np.linspace(0, intervalo, 50, endpoint=True)
	C = np.exp(X)
	amplificar(C,amplitud)
	exp = np.array(C)
	pl.plot(X,exp)
	listaSenialesContinuas.append(exp)	

def discretas():
	print "Discretas no definidas aún"

def amplificar(senial,amplitud):
	for i in range (len(senial)):
		senial[i]=senial[i]*amplitud


#Funcion que convoluciona dos señales.
#@Param seniales: Es una lista con los valores de las 2 seniales a convolucionar.
#Agrega la lista resultante senialRes a la lista recibida seniales.
def convoluciona(seniales):
    senial1   = seniales[0][::-1]
    #print senial1
    senial2   = seniales[1]
    #print senial2
    senialRes = []
    for i in range(len(senial1)+len(senial2)-1):
		senialRes.append(0)
    i=0
    j=0
    for i in range (len(senial1)):
    	for j in range (len(senial2)):
            senialRes[i+j]=senialRes[i+j]+senial1[i]*senial2[j]
    seniales.append(np.array(senialRes)) # Cast de <list> a <np.array> para usarse en graficador
    #print senialRes

#FUNCION PRINCIPAL
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


def graficarConvolucion(senialRes):
	try:
		print "graficarConvolucion: Aun no definida correctamente"
		X = np.linspace(0, limite , len(senialRes), endpoint=True)
		pl.plot(X,senialRes)
	except Exception as ex:
		print "Error inesperado: " , type(ex)
	


#Imprime los elementos de una lista, en este caso, se usa para imprimir el resultado de la convolucion.
def imrpimeRes(resultado):
	for valor in resultado:
		print valor


#Funcion para probar funcionamiento de convolucion.
#Se definen un par de señales y se obtiene su convolucion.
def prueba():
	lista1 = [1,0,-1,0,1,0,-1] #coseno(nPI)
	lista2 = [0,1,0] #impulso desplazado
	lista3 = []
	for i in range(len(lista1)+len(lista2)-1):
		lista3.append(0)
	convoluciona(lista1,lista2,lista3)
	imrpimeRes(lista3)



main()
