import csv
from random import randint


def file_number():
    """
    Returns the number of the first none existing file
    :rtype: int
    """
    n = 0
    while True:
        try:
            with open('graph_file_{}.txt'.format(n)):
                n += 1
        except FileNotFoundError:
            return n


def generate_graph(size, max_value):
    """
    Generates a random symmetric matrix of shae size * size
    :type size: int
    :type max_value: int
    :rtype: list(list(int))
    """
    graph = list()
    for i in range(size):
        row = list()
        for j in range(size):
            if i == j:
                row.append(0)
            elif len(graph) >= j:
                row.append(graph[j][i])
            else:
                row.append(randint(1, max_value))
        graph.append(row)
    return graph


if __name__ == '__main__':
    import sys
    if not len(sys.argv) == 3:
        raise ValueError('Invalid argument number')
    size, max_value = map(int, sys.argv[1:])
    graph = generate_graph(size, max_value)
    target_file = 'graph_file_{}.txt'.format(file_number())
    with open(target_file, 'w', newline='') as target:
        writer = csv.writer(target, delimiter=',')
        for line in graph:
            writer.writerow(line)
