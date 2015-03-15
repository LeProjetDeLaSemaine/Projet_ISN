#-*- coding:utf-8 -*-

def transformation(chaine):
    #Transforme une chaine de caractère selon l'algorithme de la transformée de Burrows-Wheeler
    #   chaine: chaine à transformer
    #renvoie une chaine de caractères transformée
    chaineTransformee = ""
    iterateur = 0
    tableau = [[char for char in chaine] for i in range(0,len(chaine))]

    #ON CONSTRUIT LE TABLEAU DE TRANSFORMATION (sous forme de liste bidimensionelle)
    
    for i in range(0,len(tableau)-1):
        nouveauTableau = [tableau[i][j+1] for j in range(0,len(chaine)-1)]
        nouveauTableau.append(tableau[i][0])
        tableau[i+1] = nouveauTableau

    #ON TRANSFORME LE TABLEAU EN UNE LISTE DE CHAINES DE CARACTERE
        
    strTableau = ["" for i in range(0,len(chaine))]
    for i in range(len(chaine)):
        for j in range(len(chaine)):
            strTableau[i] += tableau[i][j]

    #ON TRIE LE TABLEAU PAR ORDRE ALPHABÊTIQUE

    strTableau.sort() #On utilise ici une méthode de l'objet liste qu'il aurait été trop fastidieux de recoder

    #ON RECUPERE L'INDEX DE LA CHAINE INITIALE DANS LE TABLEAU TRIE

    index = -1
    for i in range(len(chaine)):
        if(strTableau[i] == chaine):
            index = i

    #ON CONSTITUE ENFIN LA CHAINE TRANSFORMEE

    for liste in strTableau:
        chaineTransformee += liste[0]
    return str(index) + chaineTransformee

def decodage(chaine):
    pass
    

print(transformation("MISSISSIPI RIVER"))
