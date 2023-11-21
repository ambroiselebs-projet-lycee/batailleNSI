# Léo & Ambroise

import random

VALEURS = ['','', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']

class Carte:
    """Initialise couleur (de 1 à 4), et valeur (de 2 à 14)"""

    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        if (VALEURS[self.valeur] == 'Valet') return '11'
        elif (VALEURS[self.valeur] == 'Dame') return '12'
        elif (VALEURS[self.valeur] == 'Roi') return '13'
        elif (VALEURS[self.valeur] == 'As') return '14'
        else return VALEURS[self.valeur]

    def get_couleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
        return COULEURS[self.couleur]

class PaquetDeCarte:
    """Initialise un paquet de cartes, avec un attribut contenu, de type list, vide"""

    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes : en parcourant les couleurs puis les valeurs"""
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]

    def get_carte_at(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        if 0 <= pos < 52:
            return self.contenu[pos]


paquet = PaquetDeCarte()
paquet.remplir()
jeu1 = paquet.contenu[:26]
jeu2 = paquet.contenu[26:]
tapis = []

while jeu1 != [] or jeu2 != []:
    tapis.append(jeu1[0])
    tapis.append(jeu2[0])

    if int(tapis[0].get_nom()) > int(tapis[1].get_nom()):
        # Joueur 1 gagne -> il récupère les cartes du tapis
        jeu1.append(tapis[0])
        jeu1.append(tapis[1])

        # Joueur 2 perd -> il retire sa carte
        jeu2.remove(tapis[1])

        tapis = []
    elif int(tapis[0].get_nom() < int(tapis[1].get_nom())):
        # Joueur 2 gagne -> il récupère les cartes du tapis
        jeu2.append(tapis[0])
        jeu2.append(tapis[1])

        # Joueur 1 perd -> il retire sa carte
        jeu1.remove(tapis[0])

        tapis = []
    elif int(tapis[0].get_nom() == int(tapis[1].get_nom())):
        tapis.append(jeu1[1])
        tapis.append(jeu2[1]) 

