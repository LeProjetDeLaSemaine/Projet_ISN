#-*- coding: utf-8 -*-

class Dictionnaire(object):
    #Décrit un dictionnaire, construit à partir de deux listes

    #Propriétés
    cles = [] # Liste contenant les clefs
    contenu = [] # Liste contenant les éléments du dictionnaire

    #Constructeur
    
    def __init__(self,Cles,Contenu):
        #Instancie un dictionnaire
        #   Cles: Liste contenant les cles du dictionnaire
        #   Contenu: Liste contenant les éléments du dictionnaire
        assert(len(Cles) == len(Contenu)) #On vérifie que les deux listes sont de la même longueur, dans le cas contraire, on lève une exception
        self.cles = Cles 
        self.contenu = Contenu

    #Méthodes
    def ajouter(self,cle,objet):
        #Décrit une méthode permettant d'ajouter un élément au dictionnaire
        #   cle: clé de l'élément
        #   objet: élément devant être ajouté
        self.cles.append(cle)
        self.contenu.append(objet)

    def obtenirValeur(self, cle):
        #renvoie l'élément à la clé spécifiée
        #   cle: clé de l'élément voulu
        return self.contenu[self.cles.index(cle)]

    def supprimer(self,cle):
        #Décrit une méthode supprimant l'élement à la clé indiquée
        #   clé: clé de l'élement devant être supprimé
        self.contenu.remove(obtenirValeur(cle))
        self.cles.remove(cle)


#Tests
dico = Dictionnaire([2,3],[4,5])
print(dico.obtenirValeur(2))
dico.ajouter("azerty","uiop")
print(dico.obtenirValeur("azerty"))
