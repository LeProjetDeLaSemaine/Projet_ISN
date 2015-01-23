#!/usr/bin/env python
# coding: utf-8

#FONCTIONS UTILES :
def isInt(s):
	try: #Oui, j'utilise un try/except, honte à moi...
		int(s)
		return True
	except ValueError:
		return False
		
def erreur(motif):
	print("[Erreur] " + motif)

	
#AVEC DES FICHIERS
def compressionFichier(origine, destination, op):
	#Compresse un fichier contenant du texte brut
	if op not in ('c', 'd'):
		erreur("Opération non reconnue.")
		return
	if ((origine[-4:] == ".txt") and (destination[-4:] == ".txt")) : #On vérifie que les fichiers passés comme arguments sont bien du type txt (en détectant l'extension .txt)
		with open(origine, 'r') as file: #on ouvre le fichier devant être traité en mode lecture
			content = file.read()
			file.close() #On ferme le fichier
		newStr = (compresser(content) if op == 'c' else decompresser(content))
		with open(destinatation ,'w') as file: #On ouvre le fichier de destination en mode écriture
			file.write(newStr) #On écrit le résultat dans le fichier
			file.close() # On ferme le fichier
	else:
		erreur("Type de fichier incorrect.")