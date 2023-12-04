# Léo & Ambroise

import random
"""
from Objects.JeuObject import Jeu
from Objects.JoueurObject import Joueur
from Objects.PaquetObject import PaquetDeCarte
from Objects.TapisObject import Tapis
"""

VALEURS = ['', '', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 's', 'h', 'd', 'c']

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        # Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi
        if VALEURS[self.valeur] == 'Valet':
            return 11
        elif VALEURS[self.valeur] == 'Dame':
            return 12
        elif VALEURS[self.valeur] == 'Roi':
            return 13
        elif VALEURS[self.valeur] == 'As':
            return 14
        else:
            return int(VALEURS[self.valeur])

    def get_couleur(self):
        """Renvoie la couleur de la Carte (parmi s, h, d, c)"""
        return COULEURS[self.couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenuPaquetDeCarte = []

    def remplir(self):
        # Remplir le paquet de carte
        self.contenuPaquetDeCarte = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]

    def get_carte_at(self, pos):
        if 0 <= pos < len(self.contenuPaquetDeCarte):
            return self.contenuPaquetDeCarte[pos]

    def remove(self, carte_a_retirer):
        self.contenuPaquetDeCarte.pop(carte_a_retirer)

    def melanger(self):
        random.shuffle(self.contenuPaquetDeCarte)

class Tapis:
    def __init__(self):
        self.contenuTapis = []

    def get_carte_at(self, pos: int):
        return self.contenuTapis[pos]

    def remove(self, carte: Carte):
        self.contenuTapis.pop(carte)

    def add(self, carte: Carte):
        self.contenuTapis.append(carte)

    def redistribuer(self, jeu):
        for i in self.contenuTapis:
            jeu.add(i)
        self.clean()

    def clean(self):
        self.contenuTapis = []

class Joueur():
    def __init__(self, cartes, tapis: Tapis):
        self.cartesJoueur = cartes
        self.tapis = tapis

    def get_carte_at(self, pos: int):
        return self.cartesJoueur[pos]

    def remove(self, carte: Carte):
        self.cartesJoueur.pop(carte)

    def add(self, carte: Carte):
        self.cartesJoueur.append(carte)

    def ajouterTapis(self):
        if len(self.cartesJoueur) >= 2:
            self.tapis.add(self.cartesJoueur[0])
            self.cartesJoueur.pop(0)
        else:
            self.tapis.redistribuer(self)

class Jeu():
    def __init__(self, joueur1: Joueur, joueur2: Joueur, tapis: Tapis, paquet: PaquetDeCarte):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tapis = tapis
        self.paquet = paquet
        self.n = 0

    def comparaison(self):
        jeu1 = int(self.tapis.get_carte_at(self.n).get_nom())
        jeu2 = int(self.tapis.get_carte_at(self.n+1).get_nom())

        if jeu1 > jeu2:
            #Joueur 1 gagne
            for i in self.tapis.contenuTapis:
                self.joueur1.add(i)

            # Vider le tapis et remettre n à 0
            self.tapis.clean()
            self.n = 0

        if jeu1 < jeu2:
            # Joueur 2 gagne
            for i in self.tapis.contenuTapis:
                self.joueur2.add(i)

            # Vider le tapis et remettre n à 0
            self.tapis.clean()
            self.n = 0

        if jeu1 == jeu2:
            # Bataille
            return self.bataille()

    def bataille(self):
        # Ajouter les cartes au tapis (une face cachée et l'autre face visible)
        self.n += 2

        self.joueur1.ajouterTapis()
        self.joueur2.ajouterTapis()
        self.joueur1.ajouterTapis()
        self.joueur2.ajouterTapis()

        # Re comparer les cartes
        self.comparaison()

    def victoire(self)->str:
        if len(self.joueur1.cartesJoueur) == len(self.paquet.contenuPaquetDeCarte):
            # Joueur 1 gagne
            return "joueur1"
        if len(self.joueur2.cartesJoueur) == len(self.paquet.contenuPaquetDeCarte):
            # Joueur 2 gagne
            return "joueur2"
        else:
            # Pas encore de gagnant
            return "aucun"

def partie(joueur1Cartes=None, joueur2Cartes=None):
    # Paquet de carte
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()

    # Tapis
    tapis = Tapis()

    # Joueur
    if joueur1Cartes is not None and joueur2Cartes is not None:
        joueur1 = Joueur(joueur1Cartes, tapis, paquet)
        joueur2 = Joueur(joueur2Cartes, tapis, paquet)
    else:
        joueur1 = Joueur(paquet.contenuPaquetDeCarte[:26], tapis)
        joueur2 = Joueur(paquet.contenuPaquetDeCarte[26:], tapis)

    # Fonctions de jeu
    fonctionJeu = Jeu(joueur1, joueur2, tapis, paquet)

    # Boucle principale
    while len(joueur1.cartesJoueur) != len(paquet.contenuPaquetDeCarte) or len(joueur2.cartesJoueur) != len(paquet.contenuPaquetDeCarte):
        joueur1.ajouterTapis()
        joueur2.ajouterTapis()

        fonctionJeu.comparaison()
        if fonctionJeu.victoire() != "aucun":
            break

    print(f"Le vainceur est {fonctionJeu.victoire()}")

partie()
