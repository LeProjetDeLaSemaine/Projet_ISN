#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Utilitaires import isInt, erreur, compressionFichier
debug = 0

def construireDico(content): #Construire un dictionnaire qui associe à chaque caractère sa fréquence
	dico = {} #on crée un dictionnaire
	for c in content: #pour chaque caractère c dans la chaîne à compresser
		if c in dico: #si c est déjà dans le dictionnaire
			dico[c] += 1 #on incrémente le compteur d'occurences de c de 1
		else: #sinon
			dico[c] = 1 #on initialise le compteur d'occurrences de c à 1
	return dico #on retourne le dictionnaire
	
def construireArbre(dico): #construit un arbre (tas binaire) petit à petit en mode yolo (je suis fatigué ok ???)
	tas = [(n, c) for c, n in dico.items()]
	tas = sorted(tas, reverse=True) #bof, mais confère une sûreté : si deux lettres ont le même nombre d'occurrences, le loop dans le dico échange parfois leur place (du fait de la nature non ordonnée des dictionnaires)
	while len(tas) >= 2:
		if debug: print("TAS =", tas)
		tas = sorted(tas, key=lambda tup: tup[0], reverse=True) #on trie de façon décroissante, de façon à pouvoir utiliser pop() pour avoir l'élément de plus petit poids
		n1, noeud1 = tas.pop() #on récupère le noeud de plus petit poids
		n2, noeud2 = tas.pop() #et le 2e noeud de plus petit poids
		if debug: print('(' + str(n1) + ", " + str(noeud1) + ')')
		if debug: print('(' + str(n2) + ", " + str(noeud2) + ')')
		tas.append((n1+n2, {0: noeud1, 1: noeud2})) #on remet notre arbrisseau dans le tas, ou il sera traité en fonction de son poids 
		
	return tas[0][1] #à la fin, on a une liste contenant un unique tuple (d'où le [0]), qui contient un poids et un dictionnaire, que l'on veut (d'où le [1])
	
def genererCode(arbre, cod = {}, prefixe = ''):
	for nd in arbre: #on boucle pour chaque noeud dans l'arbre
		if len(arbre[nd]) == 1: #si le noeud n'a qu'une longueur de 1, c'est à dire s'il ne contient pas de "branches"
			cod[arbre[nd]] = prefixe+str(nd) #on l'ajoute au code avec pour clé la valeur binaire et pour valeur la lettre
		else: #sinon
			genererCode(arbre[nd], cod, prefixe+str(nd)) #jolie récursion : on appelle la fonction avec cod et le parcours d'arbrisseau qu'est nd
	return cod #on retourne enfin le code
	
def encoder(content, cod):
	binaire = ""
	for c in content: #on boucle à travers les caractères de la chaîne à encoder
		binaire += cod[c] #on ajoute à la représentation binaire du texte le mot binaire correspondant à chaque caractère
	return binaire
	
def decoder(binaire, cod):
	cod = {n: c for c, n in cod.items()} #on inverse les clés et leurs valeurs, afin de pouvoir accéder aux lettres à partir du binaire
	texte = ""
	tmp = ""
	for b in binaire: #on boucle dans notre chaîne binaire
		tmp += b #on ajoute le caractère 
		if tmp in cod: #si tmp correspond au mot binaire associé à un caractère de notre code
			texte += cod[tmp] #on ajoute ce caractère au texte décodé
			tmp = "" #et on réinitialise tmp
	return texte

def compression(content):
	dico = construireDico(content)
	arbre = construireArbre(dico)
	cod = genererCode(arbre)	
	binaire = encoder(content, cod)
	return binaire, cod	

dico = construireDico("MISSISSIPPI RIVER")
arbre = construireArbre(dico)
cod = genererCode(arbre)
binaire = encoder("MISSISSIPPI RIVER", cod)
print(binaire)
print(decoder(binaire, cod))