def jeu(jeu1_cartes=None, jeu2_cartes=None)->bool:
    # Intialisation des variables
    paquet = PaquetDeCarte()
    paquet.remplir()
    paquet.melanger()
    # Utilisation des jeux personnalisés si fournis
    if jeu1_cartes is not None and jeu2_cartes is not None:
        jeu1 = jeu1_cartes
        jeu2 = jeu2_cartes
    else:
        jeu1 = paquet.contenu[:26]
        jeu2 = paquet.contenu[26:]
        jeu1_cartes = jeu1
        jeu2_cartes =     tapis = []

    # Boucle principale
    while jeu1 and jeu2:

        # On utilise un comparateur pour comparer la valeur des cartes et un tapis qui contient des cartes de la class
        comparateur.append(jeu1[0].get_nom())
        comparateur.append(jeu2[0].get_nom())

        tapis.append(jeu1[0])
        tapis.append(jeu2[0])

        print(tapis)
        print(comparateur)

        jeu1.remove(jeu1[0])
        jeu2.remove(jeu2[0])


        if comparateur[0] > comparateur[1]:
            # Joueur 1 gagne -> il récupère les cartes du comparateur
            jeu1.append(tapis[0])
            jeu1.append(tapis[1])
            tapis = []
        elif comparateur[0] < comparateur[1]:
            # Joueur 2 gagne -> il récupère les cartes du comparateur
            jeu2.append(tapis[0])
            jeu2.append(tapis[1])   
            tapis = []
        elif comparateur[0] == comparateur[1]:
            # Bataille
            n= 1
            print(comparateur)
            print("BATAILLE")

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
                        print(comparateur)
                        for i in tapis: jeu1.append(i)
                        tapis = []
                        break
                    elif comparateur[n-1] < comparateur[n]:
                        print(comparateur)
                        for i in tapis: jeu2.append(i)
                        tapis = []
                        break
                # Si l'un des deux joueurs n'a pas assez de carte il perd la bataille automatiquement
                elif len(jeu1)<2:
                    print(comparateur)
                    for i in tapis: jeu2.append(i)
                    tapis = []                    
                    break
                elif len(jeu2)<2:
                    print(comparateur)
                    for i in tapis: jeu1.append(i)                    
                    tapis = []
                    break

    # On vérifie si un des deux joueurs n'a plus de carte
    if len(jeu1)==52 or len(jeu1) == len(jeu1_cartes)+len(jeu2_cartes):
        print("Joueur 1 à Gagné !")
        return True
    elif len(jeu2)==52 or len(jeu2) == len(jeu1_cartes)+len(jeu2_cartes):
        print('Joueur 2 à Gagné !')
        return True

    return False

# Lancer le jeu
'''
On peut lancer la fonction jeu sans paramètre, auquel cas le jeu se déroule avec un paquet de 52 cartes.
On peut aussi lancer la fonction jeu en fournissant deux listes de cartes, qui seront utilisées comme jeux de départ. Sous la forme :
jeu(
    [Carte('d', 4)], 
    [Carte('s', 3)]
)

Dans ce cas là le joueur 1 gagnera

Si on veut utiliser les cartes 'Valet', 'Dame', 'Roi', 'As' on doit faire : 
'Valet' = 11
'Dame' = 12 
'Roi' = 13
'As' = 14
'''
jeu(
    [Carte('d', 14)], 
    [Carte('s', 3)]
)
#joueur 1 gagne
"""
On peut lancer la fonction jeu sans paramètre, auquel cas le jeu se déroule avec un paquet de 52 cartes.
"""
jeu()
#Aléatoire
"""
On peut tester également si le joueur 2 peut gagner en faisant :
"""
jeu(
    [Carte('c', 3)], 
    [Carte('c', 14)]
)
#joueur 2 gagne
"""
On peut faire un test également avec une bataille, c'est a dire que les deux joueurs ont la même carte, par exemple :
"""
jeu(
    [Carte('c', 3), Carte('h', 3), Carte ('d',2)], 
    [Carte('d', 3), Carte('s', 3), Carte ('c',4)]
)
#joueur 2 gagne
"""
On peut faire un test avec une double bataille :
"""
jeu(
    [Carte('c', 3), Carte('h', 3), Carte ('d',2), Carte('s', 3), Carte ('c',4), Carte('c', 5)], 
    [Carte('d', 3), Carte('s', 3), Carte ('c',4), Carte('c', 3), Carte ('d',2), Carte('s', 8)]
)
#joueur 2 gagne
"""
On peut tester également une autre double bataille avec des cartes roi dame valet et as :
"""
jeu(
    [Carte('c', 3), Carte('h', 3), Carte ('d',2), Carte('s', 13), Carte ('c',14), ],
    [Carte('d', 3), Carte('s', 3), Carte ('c',2), Carte('c', 13), Carte ('d',12), ]
)
#joueur 1 gagne