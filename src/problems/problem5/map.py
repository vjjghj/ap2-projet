"""
https://interstices.info/le-probleme-du-voyageur-de-commerce/
"""
#Problem 5
from copy import deepcopy


class AreaInitialization(object):
    
    def __init__(self, graph_file):
        self.__graph = self.__init_graph(graph_file)
        self.__visited = [0]
        self.__position = 0
        print(self.__graph)


    def __init_graph(self, graph_file):
        with open (graph_file,'r') as graph_file:
            mat = graph_file.readlines()
            l = list()
            for line in mat :
                l += [line.split(',')]
            for i in l:
                i[-1] = i[-1][:-1]
                for elem in i:
                    elem = int(elem)
        return l
    
    
    def get_position(self, graph_file):
        return self.__position
    
    
    def set_position(self, graph_file):
        newvalue = neighbourhood_close(self, graph_file, self.__position)
        self.__position = newvalue
        self.__visited += [self.__position]
        0
        """
        on a défini la prochaine position en f(x) du voisin ,
        il nous reste à modifié le voisin , si la ville est déjà dans les visités on y retourne pas "
        """
        

    def neighbourhood_close2(self, indexville):
        l = deepcopy(self.__graph)
        liste=list()
        for i in l :
            c = i.copy()
            i.remove('0')
            p = c.index(min(i))+1
            liste+= [p]
        return liste[indexville] #Indexville c'est 0 pour la ville 1 etc... et 3 pour la ville 4
        
    def neighbourhood_close3(self, indexville=0):
        a=0
        l = deepcopy(self.__graph)
        liste = [indexville]
        while len(l) != len(liste):
            i = l[a]
            for elem in i:
                elem=int(elem)
            return i
            a += 1
            c = i.copy()
            c.remove('0')
            p = i.index(min(c))
            if p not in liste:
                liste+= [p]
            else:
                i[i.index(min(c))]=0
                a -= 1
                
        return liste
#        return liste[indexville] #Indexville c'est 0 pour la ville 1 etc... et 3 pour la ville 4
    def neighbourhood_close4(self, indexville=0):
        l = deepcopy(self.__graph)
        liste = [indexville]
        while len(l) != len(liste):
            i = l[liste[-1]]
            c = i.copy()
            c.remove('0')
            p = i.index(min(c))
            print(p)
            if p not in liste:
                liste+= [p]
            else:
                i[i.index(min(c))]=0
        return liste        
    def neighbourhood_close(self, indexville=0):
        l = deepcopy(self.__graph)
        liste = [indexville]
        while len(l) != len(liste):
            i = l[liste[-1]]
            c = i.copy()
            c.remove('0')
            p = i.index(min(c))
            print(p)
            if p not in liste:
                liste+= [p]
            else:
                c[c.index(min(c))]=0
        return liste
#        return liste[indexville] #Indexville c'est 0 pour la ville 1 etc... et 3 pour la ville 4


    """
    On doit definir une fonction position before
    on delete cette position de la liste
    il nous restera 3 valeurs possibles et on prend le min
    """