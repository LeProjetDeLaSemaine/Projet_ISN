#copyright © 2015 Ernest Foussard et Clément Doumergue
#!/usr/bin/python
#-*- coding:utf-8 -*-

def transformation(chaine):
	#Transforme une chaine de caractère selon l'algorithme de la transformée de Burrows-Wheeler
	#   chaine: chaine à transformer
	#renvoie une chaine de caractères transformée
	
	l = len(chaine) #bonnes pratiques :-P
	tableau = ["" for i in range(l)] #on crée une liste de chaînes de caractères (qui sont des listes) avec l entrées
	
	for i in range(l):
		tableau[i] = chaine[i:] + chaine[:i] #avec un peu d'astuce, cette ligne permet de prendre les lettres après i et d'y ajouter celles avant i #fierté #ilovepython
	tableau.sort() #On utilise ici une méthode de l'objet liste qu'il aurait été trop fastidieux de recoder
	
	chaineTransformee = "" #texte transformé
	index = int() #index du texte original dans tab
	
	for i in range(l):
		chaineTransformee += tableau[i][l-1:] #la chaîne transformée est celle composée des derniers caractères de chaque chaîne du tableau => la dernière colonne 
		if tableau[i] == chaine:
			index = i
	return str(index) + chaineTransformee #on retourne l'index de la chaîne originale dans le tableau trié suivi de la chaîne transformée

def decodage(chaine):
	pass #pas fait
	
print(transformation("MISSISSIPI RIVER"))
