# Léo & Ambroise

import random

VALEURS = ['','', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 's', 'h', 'd', 'c']

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
        """Renvoie la couleur de la Carte (parmi s, h, d, c)"""
        return COULEURS[self.couleur]
    

class PaquetDeCarte:
    """Initialise un paquet de cartes, avec un attribut contenu, de type list, vide"""

    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes : en parcourant les couleurs puis les valeurs"""
        for couleur in range(1, 5):
            for valeur in range(2, 15):
                self.contenu.append(Carte(couleur, valeur))

    def get_carte_at(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        if 0 <= pos < len(self.contenu):
            return self.contenu[pos]

    def remove(self, carte):
        """Enlève la carte du paquet"""
        self.contenu.remove(carte)

    def melanger(self):
        """Mélange le paquet de cartes"""
        random.shuffle(self.contenu)

class Tapis:
    def __init__(self) -> None:
        self.cartes = []

    def get_cartes_at(self, pos):
        print(f"Vérification à la position {pos+1} d'un tapis de {len(self.cartes)} cartes")
        return self.cartes[pos]
    
    def get_cartes(self):
        return self.cartes
    
    def remove(self, carte):
        self.cartes.pop(carte)

    def add(self, carte):
        self.cartes.append(carte)

    def redistribuer(self, jeu):
        for i in self.cartes:
            jeu.add(i)
        self.clean()
    
    def clean(self):
        self.cartes = []

class joueur:
    def __init__(self, cartes, tapis) -> None:
        self.cartes = cartes
        self.tapis = tapis

    def get_cartes(self):
        return self.cartes
    
    def get_cartes_at(self, pos):
        return self.cartes[pos]
    
    def remove(self, carte):
        self.cartes.pop(carte)

    def add(self, carte):
        self.cartes.append(carte)
    
    def ajouterTapis(self):
        if (len(self.cartes) > 2):
            self.tapis.add(self.cartes[0])
            self.cartes.pop(0)
        else:
            self.tapis.redistribuer(self)
            print(f"Redistribution des cartes, le joueur a donc :{len(self.cartes)} cartes")
    
        
class jeu:
    def __init__(self, jeu1, jeu2, tapis):
        self.jeu1 = jeu1
        self.jeu2 = jeu2
        self.tapis = tapis
        self.n = 1


    def comparaison(self):
        print(f"{self.jeu1.get_cartes_at(0).get_nom()} vs {self.jeu2.get_cartes_at(0).get_nom()}")
        """Renvoie si la carte A est plus grande que la carte B"""
        if (int(self.tapis.get_cartes_at(self.n-1).get_nom()) > int(self.tapis.get_cartes_at(self.n).get_nom())):
            for i in self.tapis.get_cartes(): self.jeu1.add(i)
            self.tapis.clean()
            self.n = 1
            return "jeu1"
        if (int(self.tapis.get_cartes_at(self.n-1).get_nom()) < int(self.tapis.get_cartes_at(self.n).get_nom())):
            for i in self.tapis.get_cartes(): self.jeu2.add(i)
            self.tapis.clean()
            self.n = 1

            return "jeu2"
        if (int(self.tapis.get_cartes_at(self.n-1).get_nom()) == int(self.tapis.get_cartes_at(self.n).get_nom())):
            print(f"{self.tapis.get_cartes_at(self.n-1).get_nom()} : {self.tapis.get_cartes_at(self.n).get_nom()}")
            self.bataille()
        
    def bataille(self):
        print("Bataille")
        
        # Ajouter les cartes au tapis (face cachée et face visible)
        for i in range(2):
            self.n+=1

            self.jeu1.ajouterTapis()
            self.jeu2.ajouterTapis()
        # Re comparer les cartes
        self.comparaison()

    def victoire(self):
        if len(self.jeu1.get_cartes()) == len(PaquetDeCarte().contenu):
            # Joueur 1 gagne
            return "jeu1"
        elif len(self.jeu2.get_cartes()) == len(PaquetDeCarte().contenu):
            # Joueur 2 gagne
            return "jeu2"
        else:
            # Aucun gagnant
            return "aucun"
        

# Fonction principale
def partie(jeuContenu1=None, jeuContenu2=None):
    print("JEU")
    # Paquet de carte
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()

    tapis = Tapis()

    # Jeux
    if jeuContenu1 is not None and jeuContenu2 is not None:
        jeu1 = joueur(jeuContenu1, tapis)
        jeu2 = joueur(jeuContenu2, tapis)
    else:
        jeu1 = joueur(paquet.contenu[:26], tapis)
        jeu2 = joueur(paquet.contenu[26:], tapis)

    FonctionJeu = jeu(jeu1, jeu2, tapis)

    # Boucle principale
    while len(jeu1.get_cartes()) != 0 or len(jeu2.get_cartes()) != 0:
        jeu1.ajouterTapis()
        jeu2.ajouterTapis()

        print(f"Jeu 1 : {len(jeu1.get_cartes())} cartes")
        print(f"Jeu 2 : {len(jeu2.get_cartes())} cartes")

        FonctionJeu.comparaison()
        if FonctionJeu.victoire() != "aucun":
            break
    
    # Fin du jeu
    print("Le gagnant est le joueur", FonctionJeu.victoire())


partie()