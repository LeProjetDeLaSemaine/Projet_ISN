#!/usr/bin/env python
#-*- coding: utf-8 -*-

debug = 0 #on active le debug, afin que le programme affiche plus d'informations

def construireDico(content):
	"""Construit un dictionnaire qui associe à chaque caractère sa fréquence dans la chaîne passée en argument"""
	
	dico = {} #on initialise un dictionnaire vide
	for c in content: #pour chaque caractère c dans la chaîne à compresser
		if c in dico: #si c est déjà dans le dictionnaire
			dico[c] += 1 #on incrémente le compteur d'occurences de c de 1
		else: #sinon
			dico[c] = 1 #on initialise le compteur d'occurrences de c à 1
	return dico #on retourne le dictionnaire
	
def construireArbre(dico):
	"""Construit un arbre d'Huffman (voir dossier pour des détails) à partir du dictionnaire passé en argument"""
	
	tmp = [(n, c) for c, n in dico.items()]
	tmp = sorted(tmp, reverse=True) #bof, mais confère une sûreté : si deux lettres ont le même nombre d'occurrences, le loop dans le dico échange parfois leur place (du fait de la nature non ordonnée des dictionnaires) -> le codage obtenu est donc toujours le même d'un test à l'autre
	while len(tmp) >= 2:
		if debug: print("TAS = ", tas)
		tmp = sorted(tmp, key=lambda tup: tup[0], reverse=True) #on trie de façon décroissante (basé sur le 1er objet des tuples contenus dans la liste)
		n1, noeud1 = tmp.pop() #on récupère le noeud de plus petit poids (la méthode pop renvoie et retire le dernier élément de la liste)
		n2, noeud2 = tmp.pop() #et le 2e noeud de plus petit poids
		if debug: print('(' + str(n1) + ", " + str(noeud1) + ')\n' + '(' + str(n2) + ", " + str(noeud2) + ')\n')
		tmp.append((n1+n2, {0: noeud1, 1: noeud2})) #on remet notre arbrisseau dans le tas, ou il sera traité en fonction de son poids 
		
	return tmp[0][1] #à la fin, on a une liste contenant un unique tuple (d'où le [0]), qui contient un poids suivi d'un dictionnaire, que l'on veut (d'où le [1])
	
def genererCode(arbre, cod = {}, prefixe = ''):
	"""Génère de manière récursive le code correspondant à l'arbre passé en argument, en parcourant les branches de celui-ci"""
	
	for nd in arbre: #on boucle pour chaque noeud dans l'arbre
		if len(arbre[nd]) == 1: #si le noeud n'a qu'une longueur de 1, c'est à dire s'il ne contient pas de "branches"
			cod[arbre[nd]] = prefixe + str(nd) #on l'ajoute directement au code avec pour clé la valeur binaire et pour valeur la lettre
		else: #sinon
			genererCode(arbre[nd], cod, prefixe + str(nd)) #on rappelle la fonction avec cod (le code généré et le parcours d'arbrisseau qu'est nd
	return cod #on retourne enfin le code
	
def encoder(content, cod):
	"""Remplace chaque caractère du texte passé en argument par son équivalent encodé selon le code passé en second argument"""
	
	binaire = ""
	for c in content: #on boucle à travers les caractères de la chaîne à encoder
		binaire += cod[c] #on ajoute à la représentation binaire du texte le mot binaire correspondant à chaque caractère
	return binaire
	
def decoder(binaire, cod):
	"""Retrouve la chaîne initiale à partir de la chaîne encodée et du code ayant servi à l'encoder (passés en argument)"""
	
	cod = {n: c for c, n in cod.items()} #on inverse les clés et leurs valeurs, afin de pouvoir accéder aux lettres à partir du binaire
	texte, tmp = "", "" #tmp est une chaîne temporaire
	for b in binaire: #on boucle dans notre chaîne binaire
		tmp += b #on ajoute le caractère 
		if tmp in cod: #si tmp correspond au mot binaire associé à un caractère de notre code
			texte += cod[tmp] #on ajoute ce caractère au texte décodé
			tmp = "" #et on vide tmp
	return texte

def compression(content):
	"""Compresse un texte en effectuant toutes les étapes de l'algorithme d'Huffman"""
	
	dico = construireDico(content)
	arbre = construireArbre(dico)
	cod = genererCode(arbre)	
	binaire = encoder(content, cod)
	return binaire, cod	


#DEMONSTRATION (PAS A PAS):
dico = construireDico("MISSISSIPPI RIVER")
arbre = construireArbre(dico)
cod = genererCode(arbre)
binaire = encoder("MISSISSIPPI RIVER", cod)
print(binaire)
print(decoder(binaire, cod))
