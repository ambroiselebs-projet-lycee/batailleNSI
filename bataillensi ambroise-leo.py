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
        if (VALEURS[self.valeur] == 'Valet'): return 11
        elif (VALEURS[self.valeur] == 'Dame'): return 12
        elif (VALEURS[self.valeur] == 'Roi'): return 13
        elif (VALEURS[self.valeur] == 'As'): return 14
        else: return int(VALEURS[self.valeur])

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

    def remove(self, carte):
        """Enlève la carte du paquet"""
        self.contenu.pop(carte)

    def melanger(self):
        """Mélange le paquet de cartes"""
        random.shuffle(self.contenu)


def jeu():
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()
    jeu1 = paquet.contenu[:26]
    jeu2 = paquet.contenu[26:]
    comparateur = []
    tapis = []

    while jeu1 and jeu2:

        comparateur.append(jeu1[0].get_nom())
        comparateur.append(jeu2[0].get_nom())
        tapis.append(jeu1[0])
        tapis.append(jeu2[0])
        print(tapis)
        print(comparateur)
##        print(f"comparateur : {comparateur}")

        jeu1.remove(jeu1[0])
        jeu2.remove(jeu2[0])

        if comparateur[0] > comparateur[1]:
            # Joueur 1 gagne -> il récupère les cartes du comparateur
            jeu1.append(tapis[0])
            jeu1.append(tapis[1])

            comparateur = []
            tapis = []
        elif comparateur[0] < comparateur[1]:
            # Joueur 2 gagne -> il récupère les cartes du comparateur
            jeu2.append(tapis[0])
            jeu2.append(tapis[1])

            comparateur = []
            tapis = []
        elif comparateur[0] == comparateur[1]:
            # Bataille
            n= 1
##            print(comparateur)
##            print("BATAILLE")

            while comparateur[n-1] == comparateur[n]:
                # On vérifie si les deux joueurs ont assé de cartes pour jouer la bataille complète
                if len(jeu1)>=2 and len(jeu2)>=2:
                    # On pose une première fois une carte retournée puis une seconde carte qui sera utilisé pour faire la comparaison
                    for i in range(2):
                        comparateur.append(jeu1[0].get_nom())
                        comparateur.append(jeu2[0].get_nom())
                        tapis.append(jeu1[0])
                        tapis.append(jeu2[0])
                        n+=2
                        jeu1.remove(jeu1[0])
                        jeu2.remove(jeu2[0])
                    if comparateur[n-1] > comparateur[n]:
##                        print(comparateur)
                        for i in tapis: jeu1.append(i)
                        comparateur = []
                        tapis = []
                        break
                    elif comparateur[n-1] < comparateur[n]:
##                        print(comparateur)
                        for i in tapis: jeu2.append(i)
                        tapis = []
                        comparateur = []
                        break
                    break
                # Si l'un des deux joueurs n'a pas assez de carte il perd la bataille automatiquement
                elif len(jeu1)<2:
##                    print(comparateur)
                    for i in tapis: jeu2.append(i)
                    tapis = []
                    comparateur = []
                    break
                elif len(jeu2)<2:
##                    print(comparateur)
                    for i in tapis: jeu1.append(i)
                    comparateur = []
                    tapis = []
                    break
    if len(jeu1)==52:
        print("Joueur 1 à Gagné !")
    elif len(jeu2)==52:
        print('Joueur 2 à Gagné !')

    return True

jeu()
