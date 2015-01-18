#!/usr/bin/env python
# -*- coding: utf-8 -*-

# COMPRESSION BASIQUE
# Principe : On remplace les répétitions par un caractère par le nombre de fois
# où ce caractère est présent dans la série, suivi du caractère lui-même

#On pourrait en avoir besoin, pour les longues chaînes :
#from sys import setrecursionlimit, getrecursionlimit
#setrecursionlimit(2*getrecursionlimit())

def isInt(s):
	try: #Oui, j'utilise un try/except, honte à moi...
		int(s)
		return True
	except ValueError:
		return False

def grouper(content, start=0, newstr = ""): #grouper est une fonction recursive terminale, retirant le risque de l'erreur Stack Overflow
    i = start
    j = 0
    try:
        while(content[i] == content[start]):
            i+=1
            j+=1
    except IndexError:
        return (newstr + (str(j) if j>1 else "") + content[start])
    return grouper(content, i , (newstr + (str(j) if j>1 else "") + content[start]))

def compresser(content):
	c = grouper(content) #on compresse
	return (c if len(c) < len(content) else content) #on retourne la chaîne compressée si elle est plus courte que l'originale

def decompresser(content):
	#IL FAUT UTILISER UNE RECURSION SI POSSIBLE (C'EST POSSIBLE, MAIS J'AI PAS LE TEMPS DE L'IMPLEMENTER)
	d = str() #initialisation de la variable qui contiendra la chaîne décompressée
	currentNum = 0 #compteur
	for i in range(len(content)): #on boucle dans la longueur de la chaîne à décompresser
		if isInt(content[i]): #si c'est un int
			currentNum = 10*currentNum + int(content[i]) #décalage stupide pour formater le nombre
		else: #sinon c'est un caractère
			for j in range((currentNum+1 if currentNum<1 else currentNum)): #on l'ajoute currentNum fois au résultat (ou une fois si currentNum = 0)
				d += content[i]
			currentNum = 0 #on reset pour passer au caractère suivant
	return d #on retourne d (you don't say)


print(compresser("AAADDDDEEEEEDDDBBBBCDGKHEJGFDJFFFFFFFFFFFFFFFFFFFFF"))
print(decompresser("3A4D5E3D4B1C1D1G1K1H1E1J1G1F1D1J21F"))
