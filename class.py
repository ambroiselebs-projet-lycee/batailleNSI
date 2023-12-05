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

class File:
    def __init__(self):
        self.elements = []

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if not self.est_vide():
            return self.elements.pop(0)

    def est_vide(self):
        return len(self.elements) == 0

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

    def __lt__(self, c2):
        return self.valeur < c2.valeur

    def __eq__(self, c2) -> bool:
        return self.valeur == c2.valeur

class PaquetDeCarte:
    def __init__(self):
        self.contenuPaquetDeCarte = []

    def remplir(self):
        self.contenuPaquetDeCarte.extend(Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15))

    def get_carte_at(self, pos):
        if 0 <= pos < len(self.contenuPaquetDeCarte):
            return self.contenuPaquetDeCarte[pos]

    def remove(self, carte_a_retirer):
        self.contenuPaquetDeCarte.pop(0)

    def melanger(self):
        random.shuffle(self.contenuPaquetDeCarte)

class Tapis:
    def __init__(self):
        self.contenuTapis = File()

    def get_carte_at(self, pos: int):
        return self.contenuTapis.elements[pos]

    def remove(self, carte: Carte):
        self.contenuTapis.elements.remove(carte)

    def add(self, carte: Carte):
        self.contenuTapis.enfiler(carte)

    def redistribuer(self, jeu):
        while not self.contenuTapis.est_vide():
            jeu.add(self.contenuTapis.defiler())

    def clean(self):
        self.contenuTapis = File()

    def __len__(self):
        return len(self.contenuTapis.elements)

class Joueur:
    def __init__(self, cartes, tapis: Tapis):
        self.cartesJoueur = Pile()
        for carte in cartes:
            self.cartesJoueur.empiler(carte)
        self.tapis = tapis

    def get_carte_at(self, pos: int):
        return self.cartesJoueur.elements[pos]

    def remove(self, carte: Carte):
        self.cartesJoueur.elements.remove(carte)

    def add(self, carte: Carte):
        self.cartesJoueur.empiler(carte)

    def ajouterTapis(self):
        if not self.cartesJoueur.est_vide():
            self.tapis.add(self.cartesJoueur.depiler())
        else:
            self.tapis.redistribuer(self)

class Jeu:
    def __init__(self, joueur1: Joueur, joueur2: Joueur, tapis: Tapis, paquet: PaquetDeCarte):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tapis = tapis
        self.paquet = paquet
        self.n = 0

    def comparaison(self):
        jeu1 = int(self.tapis.get_carte_at(self.n).get_nom())
        jeu2 = int(self.tapis.get_carte_at(self.n + 1).get_nom())

        jeu1_fullname = f"{self.tapis.get_carte_at(self.n).get_couleur()}{self.tapis.get_carte_at(self.n).get_nom()}"
        jeu2_fullname = f"{self.tapis.get_carte_at(self.n + 1).get_couleur()}{self.tapis.get_carte_at(self.n + 1).get_nom()}"

        print(f"{jeu1_fullname} | {jeu2_fullname}")

        if jeu1 > jeu2:
            for i in range(len(self.tapis)):
                self.joueur1.add(self.tapis.contenuTapis.defiler())
            self.tapis.clean()
            self.n = 0
            return True

        if jeu1 < jeu2:
            for i in range(len(self.tapis)):
                self.joueur2.add(self.tapis.contenuTapis.defiler())
            self.tapis.clean()
            self.n = 0
            return True

        if jeu1 == jeu2:
            print("----------BATAILLE-----------")
            return False

        return "fini"

    def bataille(self):
        if len(self.joueur1.cartesJoueur.elements) < 2:
            print("Joueur 1 n'a pas assez de cartes")
            for i in range(len(self.tapis)):
                self.joueur2.add(self.tapis.contenuTapis.defiler())
            return "joueur2"

        if len(self.joueur2.cartesJoueur.elements) < 2:
            print("Joueur 2 n'a pas assez de cartes")
            for i in range(len(self.tapis)):
                self.joueur1.add(self.tapis.contenuTapis.defiler())
            return "joueur1"

        self.n += 2

        self.joueur1.ajouterTapis()
        self.joueur2.ajouterTapis()
        self.joueur1.ajouterTapis()
        self.joueur2.ajouterTapis()

        self.comparaison()

    def victoire(self) -> str:
        if len(self.joueur1.cartesJoueur.elements) == 0:
            return "joueur2"
        if len(self.joueur2.cartesJoueur.elements) == 0:
            return "joueur1"
        else:
            return "aucun"

def partie(joueur1Cartes=None, joueur2Cartes=None):
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()

    tapis = Tapis()

    if joueur1Cartes is not None and joueur2Cartes is not None:
        joueur1 = Joueur(joueur1Cartes, tapis)
        joueur2 = Joueur(joueur2Cartes, tapis)
    else:
        joueur1 = Joueur(paquet.contenuPaquetDeCarte[:26], tapis)
        joueur2 = Joueur(paquet.contenuPaquetDeCarte[26:], tapis)

    fonctionJeu = Jeu(joueur1, joueur2, tapis, paquet)

    while len(joueur1.cartesJoueur.elements) != 0 or len(joueur2.cartesJoueur.elements) != 0:
        joueur1.ajouterTapis()
        joueur2.ajouterTapis()

        if not fonctionJeu.comparaison():
            fonctionJeu.bataille()

        if fonctionJeu.victoire() != "aucun":
            break

    print(f"Le vainqueur est le {fonctionJeu.victoire()}")

# Lancer le jeu
partie()