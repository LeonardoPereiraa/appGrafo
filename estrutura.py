from tkinter import *
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
class No :
    def __init__(self,nome,peso,canva, x, y):
        self.canva = canva
        self.nome = nome
        self.peso = peso
        self.arestas = []
        self.desenharNo(x,y)
    def desenharNo(self, x , y):
        self.x = x
        self.y = y
        self.canvaNoId = canvas.create_oval(self.x, self.y,self.x +20, self.y +20,fill="#BBB",outline="") 
        self._desenharPeso()
        self._desenharIdentificadorNo()
    def _desenharPeso(self):         
        self.pesoId = canvas.create_text(self.x + 10,self.y + 10,text=self.peso,fill="yellow")
    def _desenharIdentificadorNo(self):
        self.IdNomeNo = canvas.create_text(self.x + 25,self.y ,text=self.nome,fill="yellow")
    def apagarDesenhoIdentificadorNo(self):
        self.canva.delete(self.IdNomeNo)
        self.IdNomeNo=None
    def apagarDesenhoNo(self):
        self.apagarDesenhePeso()
        self.apagarDesenhoIdentificadorNo()
        self.canva.delete(self.canvaNoId)
        self.canvaNoId=None
    def apagarDesenhePeso(self):
        self.canva.delete(self.pesoId)
        self.pesoId =None
    def addAresta(self,aresta):
        self.arestas.append(aresta)
    def buscarAresta(self,NomeNo1,NomeNo2):
        for i in range(len(self.arestas)) :
            if self.arestas[i].nome == (NomeNo1 + NomeNo2) or  self.arestas[i].nome == (NomeNo2 + NomeNo1) :
                return self.arestas[i]
        return None

##  remove apenas uma das aresta do no 
    def removeAresta(self,NomeNo1,NomeNo2):
        for i in range(len(self.arestas)) :
            if self.arestas[i].nome == (NomeNo1 + NomeNo2) or  self.arestas[i].nome == (NomeNo2 + NomeNo1) :
                arestaparaDel =self.arestas[i]
                del(self.arestas[i])
                arestaparaDel.NumeroDeNosDeletado = arestaparaDel.NumeroDeNosDeletado +1 
                arestaparaDel.apagarAresta(self)
                return
##  remove todas as arestas daquele no 
    def removeAllAresta(self) :
        tamanho = len(self.arestas)
        for i in range(tamanho) :
            self.removeAresta(self.arestas[0].no1.nome,self.arestas[0].no2.nome)
    def apagarNo(self):
        self.removeAllAresta()
        self.apagarDesenhoNo()
        self.canva = None
        self.nome = None
        self.peso = None
        self.arestas = None

    def updatePeso(self,peso):
        self.peso = peso
        self.apagarDesenhePeso()
        self._desenharPeso()

## classe da aresta
class Aresta:
    def __init__(self,no1,no2,comp,canva):
        self.canva = canva
        self.nome=no1.nome + no2.nome
        self.no1=no1
        self.no2=no2
        self.comp = comp
        self.no1.addAresta(self)
        self.no2.addAresta(self)
        self.NumeroDeNosDeletado=0
        self.desenharAresta()

## essa função so deve ser usada pelo No quado for preciso remover uma aresta
    def apagarAresta(self,no):
        if self.NumeroDeNosDeletado == 2 :
            self.no1 = None
            self.no2 = None
            self.NumeroDeNosDeletado=None
            self.apagarDesenhoAresta()
            return
        if self.no1 != no :
            self.no1.removeAresta(self.no1.nome,self.no2.nome)
            return
        if self.no2 != no :
            self.no2.removeAresta(self.no1.nome,self.no2.nome)
            
    def desenharAresta(self):
        self.no1.apagarDesenhoNo()
        self.no2.apagarDesenhoNo()
        self.idDesenhoAresta = canvas.create_line(self.no1.x+10, self.no1.y+10, self.no2.x+10, self.no2.y+10,fill="#fff",width =3)
        self.desenhaCompAresta()
        self.no1.desenharNo(self.no1.x,self.no1.y)
        self.no2.desenharNo(self.no2.x,self.no2.y)

    def apagarDesenhoAresta(self):
        self.apagarDesenhaCompAresta()
        self.canva.delete(self.idDesenhoAresta)
        self.idDesenhoAresta= None

    def desenhaCompAresta(self):
        mediaX = (self.no1.x+10 + self.no2.x+10) / 2
        mediaY = (self.no1.y+10 + self.no2.y+10) / 2
        self.IdCompAresta = canvas.create_text(mediaX,mediaY ,text=self.comp,fill="red")

    def apagarDesenhaCompAresta(self):
        self.canva.delete(self.IdCompAresta)
        self.IdCompAresta =None
    def updateComprimento(self, comp):
        self.comp = comp
        self.apagarDesenhaCompAresta()
        self.desenhaCompAresta()
# class espece
class especeGrafo:
    def __init__(self):
        self.espece = {}
## adiciona um nó ao espaço de grafos
    def addNo(self,noId,peso,px,py,canvas):
        if self.espece.get(noId) is None :
            self.espece[noId]= No(noId,peso,canvas,px,py)
            return
        return
## procura um nó do espaço de grafos
    def procurarNo(self,id):
        return self.espece.get(id)
## remove um nó do espaço de grafos
    def removerNo(self, id):
        if self.espece.get(id) is not None :
            self.espece[id].apagarNo()
            del(self.espece[id])
            return
        return
## remove uma areste de um nó do espaço de grafo
    def removerAresta(self,id1,id2):
        if self.espece.get(id1) is not None :
            self.espece[id1].removeAresta(id1,id2)
## adiciona uma areste a um par de nós do espaço de grafo
    def addAresta(self,id1,id2,comprimeto,canvas):
        if self.espece.get(id1) is not None and self.espece.get(id2) is not None :
            Aresta(self.espece.get(id1),self.espece.get(id2),comprimeto,canvas)
            return
        return
    def updatePesoNo(self,peso,idNo):
        no=self.procurarNo(idNo)
        if no is not None:
            no.updatePeso(peso)
    def updateComprimentoAresta(self,no1,no2,comprimento):
        no = self.procurarNo(no1)
        if no is None:
            return
        no = self.procurarNo(no2)
        if no is None:
            return
        aresta= no.buscarAresta(no1,no2)
        if aresta is not None:
            aresta.updateComprimento(comprimento)

e=especeGrafo()
#e.addNo("l",2,20,20,canvas)
#e.addNo("f",2,80,70,canvas)
#e.addNo("a",2,80,120,canvas)
#e.addNo("b",2,80,170,canvas)
#e.addAresta("l","f",canvas)
#e.addAresta("l","a",canvas)
#e.addAresta("l","b",canvas)
#e.removerAresta("l","f")
#e.removerNo("l")
sair = False
while not sair:

    s = input('entrada 0 a 4 > ')
    if s == "0":
        sNome = input('nome do nó para remover > ')
        e.removerNo(sNome)
        root.update()
    if s == "1":
        s = input('0 para criar no e 1 para atualizar > ')
        if s == "0" :
            sNome = input('nome do nó para criar > ')
            speso = input('peso do nó  > ')
            sX = int(input('coordenadaX do nó  > '))
            sY = int(input('coordenadaY do nó  > '))
            e.addNo(sNome,speso,sX,sY,canvas)
            root.update()
        if s == "1":
            sNome = input('nome do nó  > ')
            speso = input('peso do nó  > ')
            e.updatePesoNo(speso,sNome)
            root.update()
    if s == "2":
        s = input('0 para criar aresta e 1 para atualizar comprimento > ')
        if s =="0":
            sNome1 = input('nome do primeiro nó da aresta > ')
    
            sNome2 = input('nome do segundo nó da aresta > ')
            sComp = input('comprimento aresta > ')
            e.addAresta(sNome1,sNome2,sComp,canvas)
            root.update()
        if s =="1":
            sNome1 = input('nome do primeiro nó da aresta > ')
    
            sNome2 = input('nome do segundo nó da aresta > ')
            sComp = input('novo comprimento aresta > ')
            e.updateComprimentoAresta(sNome1,sNome2,sComp)
            root.update()

    if s == "3":

        sNome1 = input('nome do primeiro nó da aresta para remover > ')
    
        sNome2 = input('nome do segundo nó da aresta para remover  > ')
        e.removerAresta(sNome1,sNome2)
        root.update()
    if(s=="4"):
        sair = True
#while True :    
#root.mainloop()