#!/usr/bin/python
#-*- coding: utf-8 -*-
#Note : Cet algo semble (à ce que j'ai compris) avoir besoin qu'on lui précise
#tous les caractères qu'il peut rencontrer #CestNulOMG
#Pour l'instant, on remarquera que je ne le fais fonctionner qu'avec les majuscules

def moveToFront(texte, table):
	resultat = [] #on utilise une liste (hélas), puisque les éléments sont distincts
	for c in texte: #on boucle dans le texte
		index = table.index(c) #on récupère l'index de c dans la table
		resultat.append(str(index)) #c'est mieux en str, mais il faut repasser en int pour décoder... Que faire ?
		table = [table.pop(index)] + table #on déplace le caractère à table[index] au début de table
	return resultat
	
def moveToBack(liste, table): #moveToBack est l'inverse de moveToFront, logique :-P
	chaine = ""
	for i in liste: #on boucle dans la liste
		c = table[i] #c est le caractère à l'index i de table
		chaine += c #on ajoute c au texte décodé
		table = [table.pop(i)] + table #et on le move to front
	return chaine

a = moveToFront("MISSISSIPPI RIVER", list("ABCDEFGHIJKLMNOPQRSTUVWXYZ "))
print(a)
a = [int(i) for i in a] #donc là on les repasse en int...
print(moveToBack(a, list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")))