import numpy as np

class PM:
    nbli = 9 ; nbco = 9
    nba = 5

    def __init__(self, j1aletrait=True):
        self.j1aletrait = j1aletrait
        self.pla = np.zeros((PM.nbli,PM.nbco), dtype='B')
        self.coups = [ (i,j) for i in range(PM.nbli) for j in range(PM.nbco) ]
        self.nbcoups = len(self.coups)
        self.eval = 0

    def __eq__(self,other):
        if self is None or other is None:
            return False
        if self.j1aletrait != other.j1aletrait:
            return False
        return np.all(self.pla == other.pla)

    def __hash__(self):
        return hash(bytes(self.pla))

    def Clone(self):
        p = PM()
        p.j1aletrait = self.j1aletrait
        p.pla[:,:] = self.pla
        p.coups = self.coups.copy()
        p.nbcoups = self.nbcoups
        p.eval = self.eval
        return p

    def EffectuerCoup(self, x):
        i0, j0 = x
        if self.j1aletrait:
             piece = 1
        else:
            piece = 2
        self.j1aletrait = not self.j1aletrait
        self.pla[i0, j0] = piece
        self.coups.remove(x) ; self.nbcoups -= 1

        nah = 1
        i = i0 + 1
        while i < PM.nbli and self.pla[i,j0]==piece:
            i+=1 ; nah += 1
        i = i0 - 1
        while i >= 0 and self.pla[i,j0]==piece:
            i-=1 ; nah += 1
        if nah >= PM.nba:
            self.nbcoups = 0 ; self.eval = piece ; return

        nav = 1
        j = j0 + 1
        while j < PM.nbco and self.pla[i0,j]==piece:
            j+=1 ; nav += 1
        j = j0 - 1
        while j >= 0 and self.pla[i0,j]==piece:
            j -= 1 ; nav += 1
        if nav >= PM.nba:
            self.nbcoups = 0 ; self.eval = piece ; return

        nad = 1
        i = i0 + 1 ; j = j0 + 1
        while i < PM.nbli and j < PM.nbco and  self.pla[i,j]==piece:
            i+=1 ; j+=1 ; nad += 1
        i = i0 - 1 ; j = j0 - 1
        while i >=0  and j>=0 and  self.pla[i,j]==piece:
            i -= 1 ; j -= 1 ; nad += 1
        if nad >= PM.nba:
            self.nbcoups = 0 ; self.eval = piece ; return

        nad2 = 1
        i = i0 + 1 ; j = j0 - 1
        while i < PM.nbli and j >= 0 and  self.pla[i,j]==piece:
            i += 1 ; j -= 1 ; nad2 += 1
        i = i0 - 1 ; j = j0 + 1
        while i >=0  and j<PM.nbco and  self.pla[i,j]==piece:
            i -= 1 ; j += 1 ; nad2 += 1
        if nad2 >= PM.nba:
            self.nbcoups = 0 ; self.eval = piece ; return

    def __str__(self):
        pieces = [ 'ˑ', '●', '○']
        if self.j1aletrait:
            aux = ['Trait aux noirs\n']
        else:
            aux = ['Trait aux blancs\n']
        aux += [ ' '.join(["   "] + [ chr(n)  for n in range(ord('a'), ord('a') + PM.nbco) ]), '\n']
        for i in range(PM.nbli):
            aux.append( '{:2} '.format(i+1) )
            aux += list(' ' + pieces[self.pla[i,j]] for j in range(PM.nbco) )
            aux.append('\n')
        return ''.join(aux)

if __name__ == "__main__":
    po = PM()
    po.EffectuerCoup((3,5))
    q = po.Clone()
    po.EffectuerCoup((3,6))
    #print(po)

    print(po == q)

    # import random
    #
    # for i in range(2):
    #     po.EffectuerCoup(random.choice(po.coups))
    #     print(po)
    #     if po.nbcoups == 0:
    #         break
