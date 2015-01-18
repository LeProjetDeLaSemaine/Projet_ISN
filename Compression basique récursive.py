# VERSION RECURSIVE DE LA FONCTION GROUPER POUR LES PROLONGATIONS



def grouper(content, indexInitial=0, chaineCompresse = ""): #grouper est une fonction recursive terminale, retirant le risque de l'erreur Stack Overflow
        #renvoie la chaine de caractère passée en premier argument sous forme compressée selon la compression basique décrite ci-dessus
        #content: chaine de caractère à compresser
        #indexInitial: argument privé à ne pas modifier à l'appel
        #chaineCompresse: argument privé à ne pas modifier à l'appel, contient la chaine compressée élaboré au fil des récursions
    compteur = 0
    indexCourant = indexInitial 
    while(content[indexCourant] == content[indexInitial]):
            #On boucle tant que l'on trouve toujours le même caractère
            if(indexCourant + 1 != len(content)): #On verifie qu'on est pas au dernier caractère de la chaine
                    indexCourant +=1 #On passe au caractère suivant
                    compteur +=1 
            else:
                    #Toute la chaine est compressée, on renvoie la chaine.
                    return (chaineCompresse + (str(compteur+1) if compteur>1 else "") + content[indexInitial])
    #On a trouvé un caractère différent, on fait une recursion pour les caractères suivants
    return grouper(content, indexCourant , (chaineCompresse + (str(compteur) if compteur>1 else "") + content[indexInitial]))
