
class NodArbore:
  def __init__(self, info, parent=None):
    self.info=info
    self.parent=parent

  def drumRadacina(self):
    drum=[]
    nod=self
    while nod:
      drum.append(nod)
      nod=nod.parent
    return drum[::-1]
  def inDrum(self, infonod):
    nod=self
    while nod:
      if nod.info == infonod:
        return True
      nod=nod.parent
    return False

  def __str__(self):
    return str(self.info)
  def __repr__(self):
   # return "{} ({})".format(str(self.info), "->".join([str(x) for x in self.drumRadacina()]))
      sir = str(self.info) + "("
      drum = self.drumRadacina()
      sir += ("->").join([str(n.info) for n in drum])
      sir += ")"
      return sir
  
class Graph:
  def __init__(self,matr,start,scopuri):
    self.matr=matr
    self.start=start
    self.scopuri=scopuri
  def scop(self,infoNod):
    return infoNod in self.scopuri
  def succesori(self,nod):
    lSuccesori=[]
    for infoSuccesor in range(len(self.matr)):
      if self.matr[nod.info][infoSuccesor]==1 and not nod.inDrum(infoSuccesor):
        lSuccesori.append(NodArbore(infoSuccesor,nod))
    return lSuccesori


def breadthFirst(gr,nsol=1):
  c=[NodArbore(gr.start)]
  while c:
    nodCurent=c.pop(0)
    if gr.scop(nodCurent.info):
      print(repr(nodCurent))
      nsol-=1
      if nsol==0:
        return
    lSuccesori=gr.succesori(nodCurent)
    c+=lSuccesori

#### DepthFirst recursiv

def depth_first(gr, nsol=1):
    # vom simula o stiva prin relatia de parinte a nodului curent
    df(NodArbore(gr.start), nsol)


def df(nodCurent, nsol):
    if nsol <= 0: 
        return nsol
    if gr.scop(nodCurent.info):
        print("Solutie: ", end="")
        drum = nodCurent.drumRadacina()
        print(("->").join([str(n.info) for n in drum]))
        print("\n----------------\n")
        nsol -= 1
        if nsol == 0:
            return nsol
    lSuccesori = gr.succesori(nodCurent)
    for sc in lSuccesori:
        if nsol != 0:
            nsol = df(sc, nsol)

    return nsol


#### DepthFirst nerecursiv
def df_nerecursiv(nsol):
    stiva = [NodArbore(gr.start)]
    while stiva: #cat timp stiva nevida
        nodCurent=stiva.pop() #sterg varful
        if gr.scop(nodCurent.info):
            print("Solutie:")
            drum = nodCurent.drumRadacina()
            print(("->").join([str(n.info) for n in drum]))
            print("\n----------------\n")
            nsol -= 1
            if nsol == 0:
                return
        stiva+=gr.succesori(nodCurent)[::-1]


###BreadthFirst modificat
        

# Exemplu de utilizare
m = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

start = 0
scopuri = [5, 9]

gr = Graph(m, start, scopuri)

#depth_first(gr, nsol=3)
#df_nerecursiv(nsol=5)
