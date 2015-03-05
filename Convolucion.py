#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np
import math
import matplotlib.pyplot as plt
from decimal import Decimal

#Lista que almacena las seniales y su convolucion. Las seniales son de tipo np.array
listaSenialesContinuas = []
limiteSup = 0
limiteInf = 0

# -------------------------------------------------------
# FUNCION PRINCIPAL
# -------------------------------------------------------
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


# -------------------------------------------------------
# Funcion principal para convolución de señales CONTINUAS.
# Invoca a la funciónes correspondientes a la selección del usuario para generar su señal.
# -------------------------------------------------------
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
		print "Error inesperado en funcion: Continuas()" , type(ex)


# --------------------------------------------------------
# Funcion principal para convolución de señales DISCRETAS.
# --------------------------------------------------------
def discretas():
	print "\n------------------\nSEÑALES DISCRETAS\n------------------\n"
	origenS1 = 0
	origenS2 = 0
	try:
		print "Introduzca las dos seniales por convolucionar. (Separe con coma cada muestra, indique con * la muestra en el origen)"
		entrada1 = raw_input('>>Senial 1 [\n')
		print "]"
		entrada2 = raw_input('\n>>Senial 2 [\n')
		print "]"

		#Tratamiento de entrada del usuario

		origenS1 = obtenerOrigen(entrada1)
		origenS2 = obtenerOrigen(entrada2)
		
		print "Origen S1 en: ", origenS1
		print "Origen S2 en: ", origenS2

		senial1 = transfInASenial(entrada1)
		senial2 = transfInASenial(entrada2)

		senialResultante = convolucionDiscreta(senial1,senial2)

		origenSenialRes  = ((-1)*origenS1) + ((-1)*origenS2)
		
		plt.rc('lines', linewidth=3)
		fig, (ax0, ax1)  = plt.subplots(nrows=2)
		ax0.grid(color='g', linestyle='-', linewidth=0.5)
		ax1.grid(color='g', linestyle='-', linewidth=0.5)
		#plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
		ax0.set_color_cycle(['c', 'm', 'y', 'k'])
		ax0.set_title('Seniales de Entrada')
		ax1.set_title('Senial convolucion')


		print "Graficando S1"
		graficarSDiscreta(senial1,origenS1,ax0)
		print "Graficando S2"
		graficarSDiscreta(senial2,origenS2,ax0)
		print "Graficando SR"
		graficarSDiscreta(senialResultante,origenSenialRes,ax1)
		pl.show()
	except Exception as ex:
		print "Ocurrio un error en discretas() " , type(ex) , ex


# -------------------------------------------------------
# Funciones para creacion de señales continuas
# -------------------------------------------------------
def creaFunSeno():
	print "|Señal Seno|"
	intervalo = input('>>Intervalo[t0,t]: ')
	amplitud = input('>>Amplitud: ')
	
	global limiteSup 
	global limiteInf
	
	linferior = int(intervalo[0])
	lsuperior = int(intervalo[1])
	
	limiteInf = limiteInf + linferior
	limiteSup = limiteSup + lsuperior
	X = np.linspace(linferior, lsuperior, 50, endpoint=True)
	S = np.sin(X)
	amplificar(S,amplitud)
	pl.plot(X,S)
	listaSenialesContinuas.append(S)

def creaFunCoseno():
	print "|Señal Coseno|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limiteSup 
	global limiteInf
	linferior = int(intervalo[0])
	lsuperior = int(intervalo[1])
	
	limiteInf = limiteInf + linferior
	limiteSup = limiteSup + lsuperior
	X = np.linspace(linferior, lsuperior, 50, endpoint=True)
	C = np.cos(X)
	amplificar(C,amplitud)
	pl.plot(X,C)
	listaSenialesContinuas.append(C)

def creaFunCompuerta():
	print "|Señal Compuerta|"
	intervalo = input('>>Intervalo[t0=0,t]: ')
	amplitud = input('>>Amplitud: ')
	global limiteSup 
	global limiteInf
	linferior = int(intervalo[0])
	lsuperior = int(intervalo[1])
	
	limiteInf = limiteInf + linferior
	limiteSup = limiteSup + lsuperior
	X = np.linspace(linferior, lsuperior, 50, endpoint=True)
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
	global limiteSup 
	global limiteInf
	linferior = int(intervalo[0])
	lsuperior = int(intervalo[1])
	
	limiteInf = limiteInf + linferior
	limiteSup = limiteSup + lsuperior
	X = np.linspace(linferior, lsuperior, 50, endpoint=True)
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
	global limiteSup 
	global limiteInf
	linferior = int(intervalo[0])
	lsuperior = int(intervalo[1])
	limiteInf = limiteInf + linferior
	limiteSup = limiteSup + lsuperior
	X = np.linspace(linferior, lsuperior, 50, endpoint=True)
	C = np.exp(X)
	amplificar(C,amplitud)
	exp = np.array(C)
	pl.plot(X,exp)
	listaSenialesContinuas.append(exp)	


def amplificar(senial,amplitud):
	for i in range (len(senial)):
		senial[i]=senial[i]*amplitud

# Transforma la entrada del usuario (una cadena) a una lista
def transfInASenial(entrada):
	senial = []
	for muestra in (entrada.split(",")):
		senial.append(Decimal(muestra.replace("*","")))
	return senial

	

# Para seniales discretas. Devuelve el indice en el que el usaurio indicó que se encuentra el origen.
def obtenerOrigen(entrada):
	origen = 0
	indice = 0
	if ("*" in entrada):
		pseudoSenial = entrada.split(",")
		#print "Senial" , pseudoSenial
		for muestra in pseudoSenial:
			indiceAsterisco = muestra.find("*")
			if indiceAsterisco != -1:
				origen = indice
				break
			indice = indice+1
	return origen;
	


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


def convolucionDiscreta(senial0,senial2):
	senial1 = senial0[::-1]
	try:
		senialRes = []
		for a in range(len(senial1)+len(senial2)-1):
			senialRes.append(0)
		i=0
		j=0
		for i in range (len(senial1)):
			for j in range (len(senial2)):
				senialRes[i+j]=senialRes[i+j]+senial1[i]*senial2[j]
		return senialRes
	except Exception as ex:
			print "Error en convolucionDiscreta()" , ex
			return senialRes



def graficarConvolucion(senialRes):
	global limiteSup 
	global limiteInf
	try:
		X = np.linspace(limiteInf, limiteSup , len(senialRes), endpoint=True)
		pl.plot(X,senialRes)
	except Exception as ex:
		print "Error inesperado en gaficarConvolucion(): " , type(ex)



def graficarSDiscreta(senial , origen, objGraficar):
	try:
		print "Intervalo [",origen , "," ,len(senial)-(origen+1),"]"
		X = np.linspace(origen*-1, len(senial)-(origen+1) , len(senial), endpoint=True)
		print senial
		print X
		print ""
		objGraficar.stem(X,np.array(senial),markerfmt='bo',basefmt='r-')
	except Exception as ex:
		print "Error inesperado en gaficarSDiscreta(): " , type(ex)

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
