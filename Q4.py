if __name__ == "__main__":
    from Morpion import PM
    from Partie import Partie
    from Mcts import Jmcts, JmctsM  # Assurez-vous d'importer les classes nécessaires

    j1_mcts = Jmcts(a=1, temps=1)
    j2_mctsm = JmctsM(a=1, temps=1)

    victoires_mcts = 0
    victoires_mctsm = 0

    for _ in range(5):  # Organiser 40 parties
        pini = PM()

        # Jmcts contre JmctsM
        partie_mcts_vs_mctsm = Partie(j1_mcts, j2_mctsm, pini)
        resultat_mcts_vs_mctsm = partie_mcts_vs_mctsm.Commencer(affichage=False)
        if resultat_mcts_vs_mctsm == 1:
            victoires_mcts += 1
        elif resultat_mcts_vs_mctsm == 2:
            victoires_mctsm += 1

    print(f"Nombre de victoires de Jmcts : {victoires_mcts}")
    print(f"Nombre de victoires de JmctsM : {victoires_mctsm}")

    if victoires_mctsm > victoires_mcts:
        print("JmctsM est meilleur que Jmcts dans ces 40 parties.")
    elif victoires_mctsm < victoires_mcts:
        print("Jmcts est meilleur que JmctsM dans ces 40 parties.")
    else:
        print("Les deux méthodes ont des performances équivalentes dans ces 40 parties.")
