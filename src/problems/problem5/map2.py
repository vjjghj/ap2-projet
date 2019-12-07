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
            res = list()
            for line in mat :
                l += [line.split(',')]
            for i in l:
                res += [[int(el) for el in i]]
                i[-1] = i[-1][:-1]
        return res
    
    
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
        
    def neighbourhood_close3(self, indexville=0):
        a=0
        l = deepcopy(self.__graph)
        liste = [indexville]
        while len(l) != len(liste):
            i = l[a]
            print(i)
            a += 1
            c = i.copy()
            c.remove(0)
            p = i.index(min(c))
            if p not in liste:
                liste += [p]
            else:
#                i[i.index(min(c))]=0
                c[i.index(min(c))]=0
                a -= 1
        return liste
#        return liste[indexville] #Indexville c'est 0 pour la ville 1 etc... et 3 pour la ville 4
 
 
    def idee(self):
        l= deepcopy(self.__graph)
        liste=[0]
        a=0
        c=l[0].copy()
        c.remove(0)
        while a < len(l):
            i = l[a]
            a+=1
            return (i, c)
            p = i.index(min(c))

            c= i.copy()
            c.remove(0)
            if p not in liste:
                liste += [p]
            else:
                c.remove(min(c))
        return liste
            
    def test(self):
        l = deepcopy(self.__graph)
        liste=[0]
        c=l[0].copy()
        c.remove(0)
        for i in l :
            p = i.index(min(c))
            c = i.copy()
            c.remove(0)
            if p not in liste:
                liste+= [p]
            else:
                c.remove(min(c))
                
        return liste

 

    def neighbourhood_close4(self, indexville=0):
        l = deepcopy(self.__graph)
        liste = [indexville]
        while len(l) != len(liste):
            i = l[liste[-1]]
            c = i.copy()
            c.remove(0)
            p = i.index(min(c))
            print(p)
            if p not in liste:
                liste+= [p]
            else:
                i[i.index(min(c))]=0
        return liste
    