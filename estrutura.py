from tkinter import *
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
class No :
    def __init__(self,nome,peso,canva):
        self.canva = canva
        self.nome = nome
        self.peso = peso
        self.arestas = []
    def desenharNo(self, x , y):
        self.x = x
        self.y = y
        self.canvaNoId = canvas.create_oval(self.x, self.y,self.x +20, self.y +20,fill="#BBB",outline="") 
        self._desenharPeso()
    def _desenharPeso(self):
         
        self.pesoId = canvas.create_text(self.x + 10,self.y + 10,text=self.peso,fill="yellow")
       
    def addAresta(self,aresta):
        self.arestas.append(aresta)
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

class Aresta:
    def __init__(self,no1,no2,canva):
        self.canva = canva
        self.nome=no1.nome + no2.nome
        self.no1=no1
        self.no2=no2
        self.no1.addAresta(self)
        self.no2.addAresta(self)
        self.NumeroDeNosDeletado=0

## essa função so deve ser usada pelo No quado for preciso remover uma aresta
    def apagarAresta(self,no):
        if self.NumeroDeNosDeletado == 2 :
            self.no1 = None
            self.no2 = None
            self.NumeroDeNosDeletado=None
            return
        if self.no1 != no :
            self.no1.removeAresta(self.no1.nome,self.no2.nome)
            return
        if self.no2 != no :
            self.no2.removeAresta(self.no1.nome,self.no2.nome)

class especeGrafo:
    def __init__(self):
        self.espece = {}
## adiciona um nó ao espaço de grafos
    def addNo(self,no1):
        if self.espece.get(no1.nome) is None :
            self.espece[no1.nome]=no1
            return
        return
## procura um nó do espaço de grafos
    def procurarNo(self,id):
        return self.espece.get(id)
## remove um nó do espaço de grafos
    def removerNo(self, id):
        if self.espece.get(id) is not None :
            self.espece[id].removeAllAresta()
            del(self.espece[id])
            return
        return
## remove uma areste de um nó do espaço de grafo
    def removerAresta(self,id1,id2):
        if self.espece.get(id1) is not None :
            self.espece[id1].removeAresta(id1,id2)
## adiciona uma areste a um par de nós do espaço de grafo
    def addAresta(self,id1,id2):
        if self.espece.get(id1) is not None and self.espece.get(id2) is not None :
            Aresta(self.espece.get(id1),self.espece.get(id2))
            return
        return
c = No("leo",1, canvas)
c.desenharNo(0,0)
b= No("leo",2, canvas)
b.desenharNo(50,0)
a = No("leo",3, canvas)
a.desenharNo(100,0)
e = No("leo",4, canvas)
e.desenharNo(100,40)

root.mainloop()