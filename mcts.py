from random import choice
from time import time

# 2 classes auxiliaires
class Nvide:
    cross = 0
    win = 0
    p = None
nvide = Nvide()

class Noeud:
    def __init__(self, p, père):
        self.père = père
        self.p = p
        self.fils = { x : nvide for x in p.coups }
        self.cross = 0
        self.win = 0

    def CalculMeilleurFils(self, phi):
        if self.p.j1aletrait:
            self.indMeilleurFils = max( self.p.coups, key = lambda x: phi(self.fils[x].cross, self.fils[x].win ) )
        else:
            self.indMeilleurFils = max( self.p.coups, key = lambda x: phi(self.fils[x].cross, self.fils[x].cross - self.fils[x].win ) )

    def MeilleurFils(self):
        if self.fils[self.indMeilleurFils] is not nvide:
            return self.fils[self.indMeilleurFils]
        else:
            q = self.p.Clone()
            q.EffectuerCoup(self.indMeilleurFils)
            self.fils[ self.indMeilleurFils ] = Noeud( q, self)
            return self.fils[ self.indMeilleurFils ]

    def __str__(self):
        return f"{self.indMeilleurFils} w/c = {self.fils[self.indMeilleurFils].win}/{self.fils[self.indMeilleurFils].cross}"

class Jmcts:
    def __init__(self, a=1, temps=1):
        self.temps = temps
        self.a = a
        self.nbiter = 0 # contiendra le nombre d'itérations depuis le début de la partie

    def NouvellePartie(self):
        self.nbiter =0

    def __str__(self):
        return "JMCTS[{0}-temps={1}]".format( self.a , self.temps)

    def JeuHasard(p):
        q = p.Clone()
        while q.nbcoups >0:
            q.EffectuerCoup(choice(q.coups))
        return q.eval

    def Jouer(self, p):
        t0 = time() + self.temps
        racine = Noeud(p, nvide)
        while time() < t0:
            self.nbiter += 1
            # phase de sélection
            no = racine
            while True:
                no.CalculMeilleurFils(lambda c,w : (w+self.a)/(c+self.a))
                no = no.MeilleurFils()
                if no.cross == 0 or no.p.nbcoups == 0:
                    break
            # phase de simulation
            re = [.5, 1, 0][Jmcts.JeuHasard(no.p)]
            # phase de rétropropagation
            while no != nvide:
                no.cross += 1
                no.win += re
                no = no.père
        racine.CalculMeilleurFils(lambda c,w : (w+self.a)/(c+self.a))
        print(racine, self.nbiter)
        return racine.indMeilleurFils

if __name__ == "__main__":
    from Morpion import *
    from Partie import *
    j1 = Jmcts(1,1) ; j2 = Jmcts(1, 1)
    pini = PM()
    pa = Partie( j1, j2, pini )
    pa.Commencer()
