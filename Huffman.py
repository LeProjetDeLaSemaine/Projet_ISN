#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Utilitaires import isInt, erreur, compressionFichier

def construireDico(content): #Construire un dictionnaire qui associe à chaque caractère sa fréquence
	dico = {} #on crée un dictionnaire
	for c in content: #pour chaque caractère c dans la chaîne à compresser
		if c in dico: #si c est déjà dans le dictionnaire
			dico[c] += 1 #on incrémente le compteur d'occurences de c de 1
		else: #sinon
			dico[c] = 1 #on initialise le compteur d'occurrences de c à 1
	return dico #on retourne le dictionnaire
	
def construireArbre(dico): #construit un arbre (tas binaire) petit à petit en mode yolo (je suis fatigué ok ???)
	#tas = [(n, c) for n, c in dico.items()]
	tas = {} #le tas sera un dictionnaire de la forme {0: branche_gauche, 1: branche_droite}
	while len(dico.keys()) >= 2: #tant qu'on a plus de deux caractères non traités
		n1 = min(dico.values()) #la plus petite des valeurs -> le plus petit poids
		noeud1 = [key for key in dico if dico[key] == n1][0] #on cherche la clé associée à la plus petite valeur (pardon)
		dico.pop(noeud1) #on le supprime puisqu'il est traité
		
		#idem pour le deuxième plus petit poids
		n2 = min(dico.values())
		noeud2 = [key for key in dico if dico[key] == n2][0]
		dico.pop(noeud2)
		print(dico)
		#tas = {0: ???, 1: {0: noeud1, 1:noeud2}}
		#Ajouter au tas un nouveau node qui a n1+n2 comme poids et n1 et n2 comme fils
	return tas #ou un pop de tas ?
	
def genererCode(arbre, cod = {}, prefixe = ''):
	for nd in arbre: #on boucle pour chaque noeud dans l'arbre
		if len(arbre[nd]) == 1: #si le noeud n'a qu'une longueur de 1, c'est à dire s'il ne contient pas de "branches"
			cod[arbre[nd]] = prefixe+str(nd) #on l'ajoute au code avec pour clé la valeur binaire et pour valeur la lettre
		else: #sinon
			genererCode(arbre[nd], cod, prefixe+str(nd)) #jolie récursion : on appelle la fonction avec cod et l'arbrisseau qu'est nd
	return cod #on retourne enfin le code
	
def encoder(content, cod):
	binaire = ""
	for c in content:
		binaire += cod[c]
	return binaire

def compression(content):
	dico = construireDico()
	arbre = construireArbre(dico)
	cod = genererCode(arbre)	
	chn = encoder(content, cod)
	
def decompression(content):
	pass
	
print(construireArbre(construireDico("BLABLABLA")))