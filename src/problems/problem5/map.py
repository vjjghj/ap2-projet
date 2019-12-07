from copy import deepcopy


class TspGraph(object):
    def __init__(self, graph_file):
        self.__graph = self.__init_graph(graph_file)
        self.__visited = [0]
        self.__position = 0

    @staticmethod
    def __init_graph(graph_file):
        with open(graph_file, 'r') as graph_file:
            mat = graph_file.readlines()
            graph = list()
            for line in mat:
                graph.append(list(map(lambda cell: int(cell.rstrip('\n')), line.split(','))))
        return graph

    def go_to_closest(self):
        graph = deepcopy(self.__graph)
        position = self.__visited[-1]
        directions = sorted(graph[position].copy())
        i = 0
        while directions[i] in self.__visited:
            i += 1
        self.__visited.append(graph[position].index(directions[i]))

    def visit_all(self):
        while len(self.__visited) != len(self.__graph):
            self.go_to_closest()

    def get_visited(self):
        return self.__visited

    def go_to(self, n):
        self.__visited.append(n)

    def reset(self):
        self.__visited = [0]


if __name__ == '__main__':
    x = TspGraph('problem5/graph_file.txt')
    x.visit_all()
    print(x.get_visited())
