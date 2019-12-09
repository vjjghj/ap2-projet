from copy import deepcopy


class TspGraph(object):
    def __init__(self, graph_file):
        self.__graph = self.__init_graph(graph_file)
        self.__visited = [0]
        print(self.__graph)

    @staticmethod
    def __init_graph(graph_file):
        with open(graph_file, 'r') as graph_file:
            mat = graph_file.readlines()
            graph = list()
            for line in mat:
                graph.append([int(n) for n in line.split(',')])
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
        self.reset()
        while len(self.__visited) != len(self.__graph):
            self.go_to_closest()

    def get_visited(self):
        return self.__visited

    def go_to(self, n):
        self.__visited.append(n)

    def reset(self):
        self.__visited = [0]

    def cross(self, path):
        self.reset()
        length = 0
        for direction in path:
            if direction not in self.__visited:
                self.__visited.append(direction)
                length += self.__graph[self.__visited[-1]][self.__visited[-2]]
            else:
                break
        return len(self.__visited) == len(self.__graph), length


if __name__ == '__main__':
    x = TspGraph('problem5/graph_file.txt')
    x.visit_all()
    print(x.get_visited())
