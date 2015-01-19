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

def compressionFichier(fichier,destinataire,Decompression = 0):
        #Si Decompression = 1, alors décompression, sinon compression
        #Le codeur intelligent comprendra de lui-même, il n'est plus l'heure de commenter
        if ((fichier[-3] + fichier[-2] + fichier[-1]) == "txt"):
                with open(fichier,'r') as file:
                        content = file.read()
                        file.close
                NewStr = (decompresser(content) if Decompression else compresser(content))
                with open(destinataire ,'w') as file:
                        file.write(NewStr)
                        file.close

        
        

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

compressionFichier("Fichiers\\CompressionBasique\\TexteInitial.txt","Fichiers\\CompressionBasique\\TexteCompressé.txt")
compressionFichier("Fichiers\\DécompressionBasique\\TexteCompressé.txt","Fichiers\\DécompressionBasique\\TexteDecompressé.txt",1)
