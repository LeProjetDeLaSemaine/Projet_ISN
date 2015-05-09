from BurrowsWheeler import *
import Codage_par_plages
import Huffman
import time

def testerTemps(texte,*fonctions):
    temps = 0
    for i in range(0,100):
        heureDebut = time.time()
        for fonct in fonctions:
            fonct(texte)
        heureFin = time.time()
        temps += heureFin-heureDebut
    return temps/100

def repr_bin(chaine):
    s = ""
    for char in str.encode(chaine):
        s+= bin(char)[2:].zfill(8)
    return s

def testerCompression(texte,binreturn,*fonctions):
    valeurInit = len(repr_bin(texte))
    if(len(fonctions) == 2):
        valeurFinale = len(repr_bin(fonctions[0](fonctions[1](texte))))
    else:
        if binreturn:
            valeurFinale = len(fonctions[0](texte)[0])
        else:
            valeurFinale = len(repr_bin(fonctions[0](texte)))
    return (valeurFinale/valeurInit)*100
    
#Récuperation des textes:

fichier = open("texteLong.txt","r")
texteLong = str(fichier.readlines()) #Texte de 50000 caractères
fichier.close

fichier = open("texteMoyen.txt","r")
texteMoyen = str(fichier.readlines()) #Texte de 5000 caractères
fichier.close

fichier = open("texteCourt.txt","r")
texteCourt = str(fichier.readlines()) #Texte de 500 caractères
fichier.close

fichier = open("gnu.txt","r")
gpl = str(fichier.readlines()) #License GPL
fichier.close





#Temps

print("\nTESTS DE TEMPS")
input("DEBUT DES TESTS, TAPEZ SUR UNE TOUCHE POUR COMMENCER\n")

#Transformation

#Texte long entraine memory error
print("TEMPS D'EXECUTION DE BURROWS-WHEELER SUR LE TEXTE MOYEN:", testerTemps(texteMoyen,(transformation)))

#Codage par plages
print("TEMPS D'EXECUTION DE RLE SUR LE TEXTE LONG:", testerTemps(texteLong,(Codage_par_plages.compresser)))
print("TEMPS D'EXECUTION DE RLE SUR LE TEXTE MOYEN:", testerTemps(texteMoyen,(Codage_par_plages.compresser)))

#Huffman
print("TEMPS D'EXECUTION DE HUFFMAN SUR LE TEXTE LONG:", testerTemps(texteLong,(Huffman.compression)))
print("TEMPS D'EXECUTION DE HUFFMAN SUR LE TEXTE MOYEN:", testerTemps(texteMoyen,(Huffman.compression)))


#Compression

print("\n\nTESTS DE COMPRESSION")
input("DEBUT DES TESTS, TAPEZ SUR UNE TOUCHE POUR COMMENCER\n")

#RLE
print("TAUX DE COMPRESSION POUR RLE SUR LE TEXTE LONG:",testerCompression(texteLong,0,(Codage_par_plages.compresser)))
print("TAUX DE COMPRESSION POUR RLE SUR LE TEXTE MOYEN:",testerCompression(texteMoyen,0,(Codage_par_plages.compresser)))
print("TAUX DE COMPRESSION POUR RLE SUR LE TEXTE COURT:",testerCompression(texteCourt,0,(Codage_par_plages.compresser)))
print("TAUX DE COMPRESSION POUR RLE SUR LA GPL:",testerCompression(gpl,0,(Codage_par_plages.compresser)))


#RLE + BWT
#Stack overflow texte long
print("TAUX DE COMPRESSION POUR BWT + RLE SUR LE TEXTE MOYEN:",testerCompression(texteMoyen,0,Codage_par_plages.compresser,transformation))
print("TAUX DE COMPRESSION POUR BWT + RLE SUR LE TEXTE COURT:",testerCompression(texteCourt,0,Codage_par_plages.compresser,transformation))
print("TAUX DE COMPRESSION POUR BWT + RLE SUR LA GPL:",testerCompression(gpl,0,Codage_par_plages.compresser,transformation))


#Huffman
print("TAUX DE COMPRESSION POUR HUFFMAN SUR LE TEXTE LONG:",testerCompression(texteLong,1,(Huffman.compression)))
print("TAUX DE COMPRESSION POUR HUFFMAN SUR LE TEXTE MOYEN:",testerCompression(texteMoyen,1,(Huffman.compression)))
print("TAUX DE COMPRESSION POUR HUFFMAN SUR LE TEXTE COURT:",testerCompression(texteCourt,1,(Huffman.compression)))
print("TAUX DE COMPRESSION POUR HUFFMAN SUR LA GPL:",testerCompression(texteCourt,1,(Huffman.compression)))

#BWT + RLE + HUFFMAN

a = transformation(texteMoyen)
b = Codage_par_plages.compresser(a)
c = Huffman.compression(b)[0]
print("TAUX DE COMPRESSION POUR BWT + RLE + HUFFMAN SUR LE TEXTE MOYEN:",(len(c)/len(repr_bin(texteMoyen)))*100)

a = transformation(texteCourt)
b = Codage_par_plages.compresser(a)
c = Huffman.compression(b)[0]
print("TAUX DE COMPRESSION POUR BWT + RLE + HUFFMAN SUR LE TEXTE COURT:",(len(c)/len(repr_bin(texteCourt)))*100)

a = transformation(gpl)
b = Codage_par_plages.compresser(a)
c = Huffman.compression(b)[0]
print("TAUX DE COMPRESSION POUR BWT + RLE + HUFFMAN SUR LA GPL:",(len(c)/len(repr_bin(gpl)))*100)

input("Appuyez pour continuer")


