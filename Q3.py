from Morpion import PM
from Partie import Partie
from mcts import Jmcts

def jouer_serie(nb_parties, parametres_joueur1, parametres_joueur2):
    victoires_joueur1 = 0
    victoires_joueur2 = 0
    parties_nulles = 0

    for i in range(nb_parties):
        # Création des instances des joueurs Jmcts avec des paramètres différents pour chaque série
        joueur1 = Jmcts(**parametres_joueur1)
        joueur2 = Jmcts(**parametres_joueur2)

        # Alternance des joueurs pour chaque série
        if i % 2 == 0:
            joueur1, joueur2 = joueur2, joueur1

        # Création d'une instance de la classe Partie avec les joueurs respectifs
        partie = Partie(joueur1, joueur2, PM())

        # Début de la partie
        resultat = partie.Commencer(affichage=False)

        # Analyse du résultat de la partie
        if resultat == 1:
            victoires_joueur1 += 1
        elif resultat == 2:
            victoires_joueur2 += 1
        else:
            parties_nulles += 1

    return victoires_joueur1, victoires_joueur2, parties_nulles

# Paramètres pour les joueurs Jmcts
parametres_joueur1 = {'a': 1, 'temps': 1}
parametres_joueur2 = {'a': 5, 'temps': 1}

# Nombre de parties par série
nb_parties_par_serie = 25

# Nombre de séries
nb_series = 2

# Initialisation des résultats finaux
total_victoires_joueur1 = 0
total_victoires_joueur2 = 0
total_parties_nulles = 0

# Jouer les séries et cumuler les résultats
for serie in range(nb_series):
    victoires_joueur1, victoires_joueur2, parties_nulles = jouer_serie(nb_parties_par_serie, parametres_joueur1, parametres_joueur2)
    
    # Mise à jour des résultats finaux
    total_victoires_joueur1 += victoires_joueur1
    total_victoires_joueur2 += victoires_joueur2
    total_parties_nulles += parties_nulles
    
    # Affichage des résultats de la série
    print(f"Résultats de la série {serie + 1} sur {nb_parties_par_serie} parties:")
    print(f"Joueur 1 (paramètres {parametres_joueur1}): {victoires_joueur1} victoires")
    print(f"Joueur 2 (paramètres {parametres_joueur2}): {victoires_joueur2} victoires")
    print(f"Parties nulles : {parties_nulles}")
    print("-" * 30)

# Affichage des résultats finaux de toutes les séries
print("\nRésultats finaux de toutes les séries:")
print(f"Total victoires Joueur 1: {total_victoires_joueur1}")
print(f"Total victoires Joueur 2: {total_victoires_joueur2}")
print(f"Total parties nulles : {total_parties_nulles}")
