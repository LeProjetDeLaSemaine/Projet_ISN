#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CODAGE PAR PLAGES
# Principe : On remplace les répétitions d'un caractère par le nombre de
# répétitions, suivi du caractère lui-même : aaabbc => 3a2bc

def isInt(s):
        #Cette fonction permet de tester si un caractère est un entier
	try:#On essaye de forcer le caractère dans un entier
		int(s)
		return True # Il n'y a pas eu d'erreur donc on renvoie True
	except ValueError: #Le caractère n'est pas un entier, l'instuction int(s) a levé une exception que l'on intercepte grâce à except
		return False #On renvoie False

#COMPRESSION/DECOMPRESSION
def compresser(content):
        """compresse une chaine selon l'algorithme du codage par plages"""
        chaineCompressee = ""
        precedent = content[0]
        n = 1 #compteur de lettres
        for c in content[1:]: #on boucle dans la chaîne à décompresser (sauf la 1ere lettre, qui est déjà dans precedent) 
                if c == precedent: #si identique au caractère précédent
                        n += 1 #on incrémente le compteur de lettres
                else: #sinon
                        chaineCompressee += str(n if n > 1 else "") + precedent #on ajoute à chaineCompressee le nombre de répétitions suivi de la lettre
                        n = 1 #on reset le compteur
                        precedent = c #et on affecte le caractère actuel au précédent
        chaineCompressee += str(n if n > 1 else "") + precedent #On ajoute le dernier caractère
        return (chaineCompressee if len(chaineCompressee) < len(content) else content) #on retourne la chaîne compressée si elle est plus courte que l'originale

def decompresser(content):
        """décompresse une chaine selon l'algorithme du codage par plages"""
        d = "" #d contiendra la chaîne décompressée
        n = 0 #compteur
        for c in content:#on boucle dans la chaîne à décompresser
                if isInt(c): #si c'est un int
                        n = 10*n + int(c) #décalage pour formater le nombre
                else: #sinon c'est un caractère, donc on le dégroupe
                        for j in range((n+1 if n<1 else n)): 
                                d += c #on ajoute n fois le caractère à c
                        n = 0 #on réinitialise pour passer au caractère suivant
        return d #on retourne d 


#Tests de compression de chaine
print(compresser("AAADDDDEEEEEDDDBBBBCDGKHEJGFDJFFFFFFFFFFFFFFFFFFFFF"))
print(decompresser("3A4D5E3D4B1C1D1G1K1H1E1J1G1F1D1J21F"))


