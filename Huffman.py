#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Utilitaires import isInt, erreur, compressionFichier

def construireDict(content):
	dico = {}
	for c in content:
		if c in dico:
			dico[c] += 1
		else:
			dico[c] = 1
	return dico
	
def construireArbre(dico): #construit un arbre petit à petit en mode yolo (je suis fatigué ok ???)
	tas = [(n, c) for n, c in dico.items()]
	#implémenter la réorganisation du tas pour que ce soit vraiment un tas
	while len(tas) >= 2:
		print("pas fait")
		#n1, node1
		#n2, node2
		#Ajouter au tas un nouveau node qui a n1+n2 comme poids
	return tas[1] #ou un pop de tas ?
	
def compression(content):
	pass
	
def decompression(content):
	pass
	
print(construireDict("lalalalalalalaburegeuskrbrej"))