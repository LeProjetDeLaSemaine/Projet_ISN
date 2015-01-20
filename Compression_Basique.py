#!/usr/bin/env python
# -*- coding: utf-8 -*-

# COMPRESSION BASIQUE
# Principe : On remplace les répétitions d'un caractère par le nombre de
# répétitions, suivi du caractère lui-même : aaabbc => 3a2bc


def isInt(s):
	try: #Oui, j'utilise un try/except, honte à moi...
		int(s)
		return True
	except ValueError:
		return False

def compresser(content):
	cntnt = "" #cntnt est la version compressée de content (eh oui lololol)
	precedent = content[0]
	n = 1 #compteur de lettres
	for c in content[1:]: #on boucle dans la chaîne à décompresser (sauf la 1ere lettre, qui est déjà dans precedent) 
		if c == precedent: #si identique au caractère pécédent
			n += 1 #on incrémente le compteur de lettres
		else: #sinon
			cntnt += str(n if n > 1 else "") + precedent #on ajoute à cntnt le nombre de répétitions suivi de la lettre
			n = 1 #on reset le compteur
			precedent = c #et on affecte le caractère actuel au précédent
	cntnt += str(n if n > 1 else "") + precedent #il faut mettre le dernier caractère manuellement... A peaufiner 
	return (cntnt if len(cntnt) < len(content) else content) #on retourne la chaîne compressée si elle est plus courte que l'originale

def compressionFichier(fichier,destinataire,operation):
        #Compresse un fichier texte brut
        #fichier: chemin du fichier devant être traité
        #destinataire : chemin du fichier de destination du traitement
        #operation: determine l'operation qui va être effectuée: 'c' pour une compression, 'd' pour une decompression
        #Renvoie True si la compression/decompression n'a rencontré de problème, sinon False
        
        if ((fichier[-4:] == ".txt") and (destinataire[-4:] == ".txt")) : #On vérifie que les fichier passés en argument sont bien du type txt (en detectant l'extention .txt)
                with open(fichier,'r') as file: # on ouvre le fichier devant être traité en mode lecture
                        content = file.read()
                        file.close      #On ferme le fichier
                if(operation == 'c'): # On determine l'operation devant être effectuée
                        newStr = compresser(content)
                elif(operation == 'd'):
                        newStr = decompresser(content)
                else:
                        #L'operation est inexistante, on renvoie False
                        return False 
                with open(destinataire ,'w') as file: #On ouvre le fichier de destination en mode ecriture
                        file.write(newStr) #On écrit le texte compressé dans le fichier
                        file.close # On ferme le fichier
                return True # L'opération s'est passé normalement, on renvoie True
        else:
                return False # le fichier n'est pas de type txt, on renvoie False

        
        

def decompresser(content):
	d = "" #d contiendra la chaîne décompressée
	n = 0 #compteur
	for c in content:#on boucle dans la chaîne à décompresser
		if isInt(c): #si c'est un int
			n = 10*n + int(c) #décalage pour formater le nombre
		else: #sinon c'est un caractère, donc on le dégroupe
			for j in range((n+1 if n<1 else n)): #on l'ajoute currentNum fois au résultat (ou une fois si currentNum = 0)
				d += c #on ajoute n fois le caractère à c
			n = 0 #on reset pour passer au caractère suivant
	return d #on retourne d (you don't say)

#Tests de compression de chaine

print(compresser("AAADDDDEEEEEDDDBBBBCDGKHEJGFDJFFFFFFFFFFFFFFFFFFFFF"))
print(decompresser("3A4D5E3D4B1C1D1G1K1H1E1J1G1F1D1J21F"))

#Tests de compression de fichier

compressionFichier("Fichiers\\CompressionBasique\\TexteInitial.txt","Fichiers\\CompressionBasique\\TexteCompressé.txt", 'c')
compressionFichier("Fichiers\\DécompressionBasique\\TexteCompressé.txt","Fichiers\\DécompressionBasique\\TexteDecompressé.txt",'d')
