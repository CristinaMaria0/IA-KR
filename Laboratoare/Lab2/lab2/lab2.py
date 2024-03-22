
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
  def __init__(self,start,scopuri):
    self.start=start
    self.scopuri=scopuri

  def scop(self,infoNod):
    return infoNod in self.scopuri
  
  #(numar_misionari_mal_initial, numar_canibali_mal_initial, mal_curent)
  # mal_initial=1; mal_final=0
  #mal_curent=mal_cu_barca
  
  def succesori(self,nod):
    def testConditie(m,c):
       return m==0 or m>=c

    lSuccesori=[]
    if nod.info[2]==1:
       misMalCurent=nod.info[0]
       canMalCurent=nod.info[1]
       
       misMalOpus=Graph.N-nod.info[0]
       canMalOpus=Graph.N-nod.info[1]
    else: 
       misMalOpus=nod.info[0]
       canMalOpus=nod.info[1]
       
       misMalCurent=Graph.N-nod.info[0]
       canMalCurent=Graph.N-nod.info[1]
    maxMisBarca=min(Graph.M, misMalCurent)
    for mb in range(maxMisBarca+1):
        if mb==0:
            minCanBarca=1
            maxCanBarca=min(Graph.M,canMalCurent)
        else:
            minCanBarca=0
            maxCanBarca=min(Graph.M-mb, canMalCurent,mb)
        for cb in range(minCanBarca, maxCanBarca+1):
            misMalCurentNou=misMalCurent-mb
            canMalCurentNou=canMalCurent-cb
            misMalOpusNou=misMalOpus+mb
            canMalOpusNou=canMalOpus+cb
            if not testConditie(misMalCurentNou, canMalCurentNou):
                continue
            if not testConditie(misMalOpusNou, canMalOpusNou):
                continue
            if nod.info[2]==1:
                infoSuccesor=(misMalCurentNou, canMalCurentNou)
            else:
                infoSuccesor=(misMalOpusNou,canMalOpusNou)
            if not nod.inDrum(infoSuccesor):
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


#####       LAB 2
f=open("input.txt", "r")
[Graph.N, Graph.M]=f.readline().strip().split()
Graph.N=int(Graph.N)
Graph.M=int(Graph.M)

#(numar_misionari_mal_initial, numar_canibali_mal_initial, mal_curent)
start=(Graph.N,Graph.N,1)
scopuri=[(0,0,0)]
gr=Graph(start,scopuri)
breadthFirst(gr,nsol=4)