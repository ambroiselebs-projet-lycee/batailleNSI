import random

# Définition des variables
VALEURS = ['', '', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 's', 'h', 'd', 'c']

class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()

    def est_vide(self):
        return len(self.elements) == 0

    def get(self):
        return self.elements[0]
    def __len__(self):
        return len(self.elements)


class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
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
        return COULEURS[self.couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenuPaquetDeCarte = []

    def remplir(self):
        self.contenuPaquetDeCarte.extend(Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15))

    def remove(self, carte):
        self.contenuPaquetDeCarte.remove(carte)

    def melanger(self):
        random.shuffle(self.contenuPaquetDeCarte)

class Tapis:
    def __init__(self):
        self.contenuTapis = Pile()

    def get_carte(self):
        return self.contenuTapis.get()

    def remove(self, carte):
        return self.contenuTapis.depiler()

    def add(self, carte: Carte):
        self.contenuTapis.empiler(carte)

    def clean(self):
        self.contenuTapis = Pile()

class Joueur:
    def __init__(self, cartes, tapis: Tapis):
        self.cartesJoueur = Pile()
        for carte in cartes:
            self.cartesJoueur.empiler(carte)
        self.tapisJoueur = tapis

    def get_carte(self):
        return self.cartesJoueur.get()

    def remove(self, carte):
        self.cartesJoueur.depiler()

    def add(self, carte):
        self.cartesJoueur.empiler(carte)

    def ajouter_tapis(self):
        self.tapisJoueur.add(self.cartesJoueur.depiler())

class Jeu:
    def __init__(self, j1: Joueur, j2: Joueur, t1: Tapis, t2: Tapis, paquet: PaquetDeCarte):
        self.joueur1 = j1
        self.joueur2 = j2
        self.tapis1 = t1
        self.tapis2 = t2
        self.paquet = paquet

    def comparaison(self):
        # Ajouters carte aux tapis
        self.joueur1.ajouter_tapis()
        self.joueur2.ajouter_tapis()

        jeu1 = self.tapis1.get_carte().get_nom()
        jeu2 = self.tapis2.get_carte().get_nom()

        print(f"{jeu1} | {jeu2}")

        # Comparaison
        if jeu1 > jeu2:
            # Jouer 1 gagne => donner carte des tapis au joueur 1
            while not self.tapis1.contenuTapis.est_vide():
                self.joueur1.add(self.tapis1.remove(self.tapis1.contenuTapis.get()))

            while not self.tapis2.contenuTapis.est_vide():
                self.joueur1.add(self.tapis2.remove(self.tapis2.contenuTapis.get()))

        if jeu1 < jeu2:
            # Jouer 2 gagne => donner carte des tapis au joueur 2
            while not self.tapis1.contenuTapis.est_vide():
                self.joueur2.add(self.tapis1.remove(self.tapis1.contenuTapis.get()))

            while not self.tapis2.contenuTapis.est_vide():
                self.joueur2.add(self.tapis2.remove(self.tapis2.contenuTapis.get()))

        if jeu1 == jeu2:
            # Battaille
            print("Bataille")
            return "bataille"

    def bataille(self):
        # Verifier si les joueurs ont assez de cartes
        if len(self.joueur1.cartesJoueur) < 2:
            # Joueur 1 n'a pas assez de cartes => joueur 2 gagne
            while not self.joueur1.cartesJoueur.est_vide():
                self.joueur2.add(self.joueur1.remove(self.joueur1.cartesJoueur.get()))
            return "joueur 2"

        if len(self.joueur2.cartesJoueur) < 2:
            # Joueur 2 n'a pas assez de cartes => joueur 1 gagne
            while not self.joueur2.cartesJoueur.est_vide():
                self.joueur1.add(self.joueur2.remove(self.joueur2.cartesJoueur.get()))
            return "joueur 1"

        # Ajouter les cartes face cachée au tapis (les 2 autres se font dans la comparaison)
        self.joueur1.ajouter_tapis()
        self.joueur2.ajouter_tapis()

        #Comparaison
        self.comparaison()

    def victoire(self):
        if self.joueur1.cartesJoueur.est_vide():
            return "joueur 2"
        if self.joueur2.cartesJoueur.est_vide():
            return "joueur 1"
        else:
            return "aucun"

def partie(joueur1cartes=None, joueur2cartes=None):
    # Création des paquets de cartes
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()

    # Création des tapis
    tapis1 = Tapis()
    tapis2 = Tapis()

    # Création des joueurs
    if joueur1cartes is None:
        joueur1cartes = [paquet.contenuPaquetDeCarte.pop() for i in range(26)]
    if joueur2cartes is None:
        joueur2cartes = [paquet.contenuPaquetDeCarte.pop() for i in range(26)]

    joueur1 = Joueur(joueur1cartes, tapis1)
    joueur2 = Joueur(joueur2cartes, tapis2)

    # Création du jeu
    jeu = Jeu(joueur1, joueur2, tapis1, tapis2, paquet)

    # Début de la partie
    while True:
        if jeu.comparaison() == "bataille":
            jeu.bataille()
        if jeu.victoire() != "aucun":
            break

    print(f"Le gagnant est {jeu.victoire()}")

# Lancer le jeu
partie()
"""
Dans ce cas ci, le joueur 1 gagne
partie(
    [Carte(3, 14)],
    [Carte(1, 3)]
)
"""
#joueur 1 gagne
"""
On peut tester si le joueur 2 peut gagner en faisant :
partie(
    [Carte(4, 3)],
    [Carte(4, 14)]
)
"""
#joueur 2 gagne
"""
On peut faire un test également avec une bataille, c'est a dire que les deux joueurs ont la même carte, par exemple :
partie(
    [Carte(4, 3), Carte(2, 3), Carte (3,2)],
    [Carte(3, 3), Carte(1, 3), Carte (4,4)]
)
"""
#joueur 2 gagne
"""
On peut faire un test avec une double bataille :
partie(
    [Carte(4, 3), Carte(2, 3), Carte (3,2), Carte(1, 3), Carte (4,4), Carte(4, 5)],
    [Carte(3, 3), Carte(1, 3), Carte (4,4), Carte(4, 3), Carte (3,2), Carte(1, 8)]
)
"""
#joueur 2 gagne
"""
On peut tester également une autre double bataille avec des cartes roi dame valet et as :
partie(
    [Carte(4, 3), Carte(2, 3), Carte (3,2), Carte(1, 13), Carte (4,14), ],
    [Carte(3, 3), Carte(1, 3), Carte (4,2), Carte(4, 13), Carte (3,12), ]
)
"""