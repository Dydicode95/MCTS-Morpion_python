from Partie import Partie
from mcts import Jmcts
from Jhasard import Jhasard
from Morpion import PM

if __name__ == "__main__":
    pm_initial = PM()
    joueur_mcts = Jmcts(a=1, temps=1)
    joueur_hasard = Jhasard()
    parties_totales = 25
    victoires_mcts = 0
    victoires_hasard = 0

    for _ in range(parties_totales):
        partie = Partie(joueur_mcts, joueur_hasard, pm_initial)
        resultat = partie.Commencer(affichage=False)

        if resultat == 1:
            victoires_mcts += 1
        elif resultat == 2:
            victoires_hasard += 1

    # Affichage du résultat final
    print(f"Résultats sur {parties_totales} parties :")
    print(f"Victoires de Jmcts : {victoires_mcts}")
    print(f"Victoires de Jhasard : {victoires_hasard}")
    print(f"Défaites de Jmcts : {parties_totales - victoires_mcts}")
    print(f"Défaites de Jhasard : {parties_totales - victoires_hasard}")