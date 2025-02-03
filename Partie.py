from random import choice
from time import time

class Partie:
    def __init__(self, j1, j2, pinitiale):
        self.j1 = j1
        self.j2 = j2
        self.pcourante = pinitiale.Clone()

    def NouveauMatch(self,pinitiale):
        self.pcourante = pinitiale.Clone()

    def Commencer(self, affichage = True):
        self.j1.NouvellePartie()
        self.j2.NouvellePartie()
        t0 = time()
        while self.pcourante.nbcoups > 0:
            if affichage:
                print(self.pcourante)
                t1 = time()
            if self.pcourante.j1aletrait:
                print(self.j1, 'joue')
                self.pcourante.EffectuerCoup(self.j1.Jouer(self.pcourante.Clone()))
            else:
                print(self.j2, 'joue')
                self.pcourante.EffectuerCoup(self.j2.Jouer(self.pcourante.Clone()))
            if affichage:
                print(f"({time()-t1:3.3f} s)")
            print(self.pcourante)
        if self.pcourante.eval == 1:
            print(self.j1, 'a gagné contre',self.j2,'en', time()-t0,'s')
        elif self.pcourante.eval == 2:
            print(self.j2, 'a gagné contre',self.j1,'en', time()-t0,'s')
        else:
            print('partie nulle')
        return self.pcourante.eval
