class Maze(object):

    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, filename):
        """
        each cell of a maze receives a number from 0 to the number of cells -1, cells by cells, line by line
        maze is represented by a dictionary whose keys are the cell numbers and values the list of possible DIRECTIONS
            from this cell
        start cell is number 0 (top, left) and exit cell is the last one (bottom, right)

        :param filename:  the name file containing the maze description
        :type filename: string
        :UC: filename must contain a valid Maze file
        """
        self.__cells = {}
        self.__file = filename
        self.__width = 0
        self.__height = 0
        self.init_cells(filename)
        self.__start = 0                     # index of starting cell
        self.__exit = len(self.__cells) - 1  # index of exit cell

    def init_cells(self, filename):
        """
        read a text file describing the maze from a "picture" made of | + - and spaces
        cells are stored in a dictionary, the key is the cell number (built line by line)
        the value is the string made of N,S,E,W corresponding to available directions for leave the cell

        :param filename: the name of the file containing the aze description
        :type filename: string
        :return: the dictionary corresponding to the maze description
        :rtype: dictionary (int : list(DIRECTIONS))
        :UC: filename must contain a valid Maze file
        """
        def read_content(input_stream):
            hole = ' '  # a hole means a path

            def handle_horizontal_path(chain):
                for col in range(1, self.__width):
                    car = chain[2 * col]
                    if car == hole:
                        cells[line * self.__width + col - 1] += 'E'
                        cells[line * self.__width + col] += 'W'

            def handle_vertical_path(chain):
                for col in range(0, self.__width):
                    car = chain[2 * col + 1]
                    if car == hole:
                        cells[line * self.__width + col] += 'S'
                        cells[(line + 1) * self.__width + col] += 'N'
            # read_content body
            line = input_stream.readline().rstrip().split(';')  # first line of file
            self.__width, self.__height = int(line[0]), int(line[1])      # define __width and __height fields
            cells = dict((i, '') for i in range(self.__width * self.__height))
            lines = input_stream.readlines()                              # all other lines
            for line in range(self.__height):
                handle_horizontal_path(lines[2 * line + 1])  # odd lines => horizontal path
                handle_vertical_path(lines[2 * line + 2])    # even lines => vertical path
            return cells

        # init_cells body
        try:
            with open(filename, 'r', encoding="utf-8") as input_s:
                self.__cells = read_content(input_s)
        except FileNotFoundError:
            raise FileNotFoundError('Unknown file')

    def get_size(self):
        """
        :return: the number of cells of this maze
        :rtype: int
        """
        return self.__width * self.__height

    def try_path(self, path, get_visited=False):
        """
        Path is tried from entry point, step by step.
        Course stops either as soon as a wall is met, or it returns to an already visited cell, or reaches the exit.
        Successful steps are steps until stop.

        :param path: a sequence of DIRECTIONS corresponding to moves.
        :type path: an sequence (actually a string but could be list) of DIRECTIONS
        :return: a tuple containing number of successful steps using path and manhattan
                 distance between reached cell and exit
        :param get_visited: if True, returns
        :type get_visited: boolean
        :rtype: (int, int)
        :UC: none
        """
        visited = []
        nb_steps = 0
        current_cell = self.__start
        while current_cell != self.__exit and \
                nb_steps < len(path) and \
                current_cell not in visited and \
                path[nb_steps] in self.__cells[current_cell]:
            visited.append(current_cell)
            current_cell = current_cell + self.offset(path[nb_steps])
            nb_steps += 1
        if current_cell == self.__exit:
            visited.append(self.__exit)  # Used when drawing path through maze
        return (nb_steps, self.manhattan_distance(current_cell, self.__exit)) if not get_visited else visited

    def offset(self, direction):
        """
        consider a move towards DIRECTION,
        and compute the offset to apply to the current cell number to obtain the destination cell number

        :param direction: the direction to convert
        :type direction: an element of DIRECTIONS
        :return: the offset corresponding to direction
        :rtype: int
        """
        if direction == 'E':
            return + 1
        elif direction == 'N':
            return - self.__width
        elif direction == 'W':
            return - 1
        elif direction == 'S':
            return + self.__width

    def manhattan_distance(self, first, second):
        """
        :param first: coordinate of first cell
        :type first: int
        :param second: coordinate of second cell
        :type second: int
        :return: the manhattan distance between coordinates first and second
        :rtype: int
        :UC: none
        """
        col_first, line_first = first % self.__width, first // self.__width
        col_second, line_second = second % self.__width, second // self.__width
        return abs(col_first - col_second) + abs(line_first - line_second)

    def get_width(self):
        """
        Returns the width of the maze
        This function was added because the maze width is needed in the naive fitness evaluation
        :rtype: int
        :UC: none
        """
        return self.__width

    def draw_path(self, individual):
        """
        Draws the maze and the path of individual within it
        :type individual: Individual
        :return: none
        :UC: none
        """
        path = self.try_path(individual.get_value(), True)
        with open(self.__file, 'r') as file:
            file.readline()  # Get rid of the maze size
            maze = file.readlines()
        cell_index = -1
        for i in range(1, len(maze), 2):
            is_cell = True
            new_line = ''
            for c in maze[i][:-1]:
                is_cell = not is_cell
                if is_cell:
                    cell_index += 1
                if cell_index not in path or not is_cell:
                    new_line += c
                else:
                    new_line += '*'
            maze[i] = new_line + '\n'
        print(''.join(maze))


if __name__ == "__main__":
    m = Maze('maze2.txt')
    print(m.try_path('EEESWWSESWSEESENEESENENNNS'))
    print(m.try_path('EEESWWSESWSEESENEES'))
    print(m.try_path('SSENEESENNEESWSSE'))
