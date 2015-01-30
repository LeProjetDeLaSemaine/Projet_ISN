#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Utilitaires import isInt, erreur

def construireDict(content):
	dico = {}
	for c in content:
		if c in dico:
			dico[c] += 1
		else:
			dico[c] = 1
	return dico
	
def construireArbre(dico):
	tas = [(n, c) for n, c in dico.items()]
	#implémenter la réorganisation du tas pour que ce soit vraiment un tas
	#while len(tas) >= 2:
	return tas
	
def compression(content):
        print("non implémenté")
	
def decompression(content):
	print("non implémenté")
	
