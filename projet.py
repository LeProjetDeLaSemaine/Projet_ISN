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

def grouper(content, indexInitial=0, chaineCompresse = ""): #grouper est une fonction recursive terminale, retirant le risque de l'erreur Stack Overflow
        #renvoie la chaine de caractère passée en premier argument sous forme compressée selon la compression basique décrite ci-dessus"""
        #content: chaine de caractère à compresser"""
        #indexInitial: argument privé à ne pas modifier à l'appel"""
        #chaineCompresse: argument privé à ne pas modifier à l'appel, contient la chaine compressée élaboré au fil des récursions"""
    compteur = 0
    indexCourant = indexInitial 
    while(content[indexCourant] == content[indexInitial]):
            #On boucle tant que l'on trouve toujours le même caractère
            if(indexCourant + 1 != len(content)): #On verifie qu'on est pas au dernier caractère de la chaine
                    indexCourant +=1 #On passe au caractère suivant
                    compteur +=1 
            else:
                    #Toute la chaine est compressée, on renvoie la chaine.
                    return (chaineCompresse + (str(compteur+1) if compteur>1 else "") + content[indexInitial])
    #On a trouvé un caractère différent, on fait une recursion pour les caractères suivants
    return grouper(content, indexCourant , (chaineCompresse + (str(compteur) if compteur>1 else "") + content[indexInitial]))

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
