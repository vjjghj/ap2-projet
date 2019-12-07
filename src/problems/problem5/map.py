from copy import deepcopy


class AreaInitialization(object):
    def __init__(self, graph_file):
        self.__graph = self.__init_graph(graph_file)
        self.__visited = [0]
        self.__position = 0
        print(self.__graph)

    @staticmethod
    def __init_graph(graph_file):
        with open(graph_file, 'r') as graph_file:
            mat = graph_file.readlines()
            graph = list()
            for line in mat:
                graph.append(list(map(lambda cell: int(cell.rstrip('\n')), line.split(','))))
        return graph

    def neighbourhood_close4(self, indexville=0):
        graph = deepcopy(self.__graph)
        liste = [indexville]
        while len(graph) != len(liste):
            i = graph[liste[-1]]
            c = i.copy()
            c.remove(0)
            p = i.index(min(c))
            print(p)
            if p not in liste:
                liste += [p]
            else:
                i[i.index(min(c))] = 0
        return liste


if __name__ == '__main__':
    x = AreaInitialization('problem5/graph_file.txt')
