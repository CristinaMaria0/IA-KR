class NodArbore:
    def __init__(self, informatie, g=0, h=0, parinte=None):
        self.informatie = informatie
        self.parinte = parinte
        self.g=g
        self.h=h
        self.f=g+h

    def drumRadacina(self):
        nod=self
        l=[]
        while nod:
            l.append(nod)
            nod=nod.parinte
        return l[::-1]

    def inDrum(self,infonod):
        nod=self
        while nod:
            if nod.informatie==infonod:
                return True
            nod=nod.parinte
        return False

    def __eq__(self, other):
        return self.f==other.f and self.g==other.g

    def __lt__(self, other):
        return self.f<other.f or (self.f==other.f and self.h<other.h)

    def __str__(self):
        return  f"({self.informatie}, g:{self.g} f:{self.f})"

    #c (a->b->c)
    def __repr__(self):
        return f"{self.informatie}, ({'->'.join([str(x) for x in self.drumRadacina()])})"

class Graf:
    def __init__(self, matr, start, scopuri, h):
        self.matr=matr
        self.start=start
        self.scopuri=scopuri
        self.h=h

    def scop(self, informatieNod):
        return informatieNod in self.scopuri

    def estimeaza_h(self,infoNod):
        return self.h[infoNod]

    def succesori(self, nod):
        lSuccesori=[]
        for infoSuccesor in range(len(self.matr)):
            if self.matr[nod.informatie][infoSuccesor] > 0 and not nod.inDrum(infoSuccesor):
                lSuccesori.append(NodArbore(infoSuccesor, nod.g+ self.matr[nod.informatie][infoSuccesor], self.estimeaza_h(infoSuccesor), nod))
        return lSuccesori


m = [
[0, 3, 5, 10, 0, 0, 100],
[0, 0, 0, 4, 0, 0, 0],
[0, 0, 0, 4, 9, 3, 0],
[0, 3, 0, 0, 2, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 4, 0, 5],
[0, 0, 3, 0, 0, 0, 0],
]
start = 0
scopuri = [4,6]
h=[0,1,6,2,0,3,0]


def aStarSolMultiple(gr, nsol):
    coada=[NodArbore(gr.start)]
    while coada:
        nodCurent=coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol-=1
            if nsol==0:
                return
        coada+=gr.succesori(nodCurent)
        coada.sort()


gr=Graf(m,start,scopuri,h)
aStarSolMultiple(gr, 6)