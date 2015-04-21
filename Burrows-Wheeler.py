#!/usr/bin/python
#-*- coding:utf-8 -*-

def transformation(chaine):
	"""Transforme une chaine de caractère selon l'algorithme de la transformée de Burrows-Wheeler"""

	chaine = '^' + chaine #On met un délmiteur en début de chaine qui permettra de décoder par la suite
	L = len(chaine)
	tableau = ["" for i in range(L)] #on crée une liste de chaînes de caractères (qui sont des listes) avec L entrées
	chaineTransformee = "" #texte transformé

	#CONSTRUCTION DE LA MATRICE	
	for i in range(L):
		tableau[i] = chaine[i:] + chaine[:i] #avec un peu d'astuce, cette ligne permet de prendre les lettres après i et d'y ajouter celles avant i
	tableau.sort() #On trie la matrice avec la méthode sort() de l'objet liste

	#TRANSFORMATION DE LA CHAINE	
	for i in range(L):
		chaineTransformee += tableau[i][L-1:] #la chaîne transformée est celle composée des derniers caractères de chaque chaîne du tableau => la dernière colonne 
	return chaineTransformee #on retourne l'index de la chaîne originale dans le tableau trié suivi de la chaîne transformée

def decodage(chaine):
        """décode une chaine transformée selon l'algorithme de Burrows-Wheeler"""

        L = len(chaine)
        tableau = ["" for i in range(L)]
        
	#RESTITUTION DE LA MATRICE
        for j in range(0,L):
                #A chaque étape, on concatène chaque chaine du tableau avec les caractères de la chaine puis on le trie par ordre alphabêtique
                for i in range(0,L):
                        tableau[i] = chaine[i] + tableau[i] 
                tableau.sort()        
        
	#RECUPERATION DE LA CHAINE INITIALE
        for i in tableau:
                if(i[0] == '^'): 
                        return i[1:] #On renvoie la chaine sans son premier caractère, qui correspond au délimiteur
        return None #La chaine ne contient pas le délimiteur, elle n'est donc pas transformée, on renvoie None
        
print(transformation("BANANA"))
print(decodage("BNN^AAA"))
