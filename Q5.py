from Morpion import PM
from mctsq5 import JmctsM
from time import time

def comparer_performances(jmcts1, jmcts2, nb_parties=100):
    victoires_jmcts1 = 0
    victoires_jmcts2 = 0
    parties_nulles = 0

    for _ in range(nb_parties):
        partie = PM()
        jmcts1.NouvellePartie()
        jmcts2.NouvellePartie()

        while True:
            coup_jmcts1 = jmcts1.Jouer(partie)
            partie.EffectuerCoup(coup_jmcts1)

            if partie.nbcoups == 0 or partie.eval != 0:
                break

            coup_jmcts2 = jmcts2.Jouer(partie)
            partie.EffectuerCoup(coup_jmcts2)

            if partie.nbcoups == 0 or partie.eval != 0:
                break

        if partie.eval == 1:
            victoires_jmcts1 += 1
        elif partie.eval == 2:
            victoires_jmcts2 += 1
        else:
            parties_nulles += 1

    print(f"Résultats après {nb_parties} parties:")
    print(f"{jmcts1.__class__.__name__} (max_sim={jmcts1.max_sim}): {victoires_jmcts1} victoires, {parties_nulles} parties nulles")
    print(f"{jmcts2.__class__.__name__} (max_sim={jmcts2.max_sim}): {victoires_jmcts2} victoires, {parties_nulles} parties nulles")

# Comparer les performances
jmcts1 = JmctsM(a=1, max_sim=24)
jmcts2 = JmctsM(a=1, max_sim=100)

comparer_performances(jmcts1, jmcts2, nb_parties=100)
