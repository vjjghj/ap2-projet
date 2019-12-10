class TspGraph(object):
    """
    Used to represent a complete using a matrix
    We will use this as the graph to solve in a Travelling Salesman Problem
    As the matrix is symmetric we could only store half of the values, be we keep them all for convenience
    This change could be further added to the project to gain efficiency
    """
    def __init__(self, graph_file):
        self.__graph = self.__init_graph(graph_file)
        self.__visited = [0]

    @staticmethod
    def __init_graph(graph_file):
        """
        Imports the graph from a text file
        :type graph_file: str
        :rtype: list(list(int))
        """
        with open(graph_file, 'r') as graph_file:
            mat = graph_file.readlines()
            graph = list()
            for line in mat:
                graph.append([int(n) for n in line.split(',')])
        return graph

    def get_visited(self):
        """
        Returns the list of visited towns
        :rtype: list(int)
        """
        return self.__visited

    def reset(self):
        """
        Resets the visited towns to [0]
        :return: none
        """
        self.__visited = [0]

    def cross(self, path):
        """
        Attempts to cross
        :type path: list(int)
        :rtype: int
        """
        self.reset()
        length = 0
        for direction in path:
            if direction not in self.__visited:
                self.__visited.append(direction)
                length += self.__graph[self.__visited[-1]][self.__visited[-2]]
            else:
                break
        return length

    def get_length(self):
        """
        Returns the number of towns to visit
        :rtype: int
        """
        return len(self.__graph)
