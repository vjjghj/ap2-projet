import random
import copy
from math import ceil
from enum import Enum


EMPTY = ' '
MONSTER = 'M'
OBSTACLE = '*'
USED = '.'
CELLS = [EMPTY, MONSTER, OBSTACLE]


class PlayerState(Enum):
    """
    This is used to define the possibles states of an individual through the haunted field
    An individual has five types of value:

    * ``active``
    * ``success``
    * ``monster``
    * ``blocked``
    * ``alive``
    """
    active = 1
    success = 2
    monster = 3
    blocked = 4
    alive = 5


class HauntedField(object):
    MOVES = {'u': (-1, 0), 'd': (1, 0), 'r': (0, -1), 'l': (0, 1)}

    def __init__(self, height, width, nb_monsters):
        """
        haunted field is a 2D array of height * width char,
        initially all cells are EMPTY
        cells coordinate range from (1,1) to (height,width)
        a border of OBSTACLE cells is added (line and column 0, line (height+1) and column (width+))

        :param height: height of the field
        :type height: int
        :param width: width of the field
        :type width : int
        :param nb_monsters: maximum number of monsters on each line
        :type nb_monsters: int
        :UC: 1 <= nb_monsters < width
        """
        self.__width = width
        self.__height = height
        self.__field = [[EMPTY for _ in range(self.__width + 2)] for _ in range(self.__height + 2)]
        self.__init_borders()
        self.init_monsters(nb_monsters)
        self.__player_pos = (1, ceil(self.__width / 2))
        self.__backup_field, self.__backup_pos = None, None

    def __init_borders(self):
        """
        set a border (OBSTACLE char) all around the field
        """
        for line in range(self.__height + 2):
            self.set_cell(line, 0, OBSTACLE)  # first column
            self.set_cell(line, self.__width + 1, OBSTACLE)  # last column
        for column in range(1, self.__width + 2):
            self.set_cell(0, column, OBSTACLE)  # first line
            self.set_cell(self.__height + 1, column, OBSTACLE)  # last line

    def init_monsters(self, nb_monsters_per_lines):
        """
        randomly set between 2 and nb_monsters_per_lines monsters in each line, first and last line excepted.
        Must be called to add monster to the field
        :UC: nb_monsters_per_lines < self.__width
        """
        for line in range(2, self.__height):
            monster_columns = random.sample(range(1, self.__width + 1), random.randint(2, nb_monsters_per_lines))
            for column in monster_columns:
                self.set_cell(line, column, MONSTER)

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_cell(self, line, column):
        return self.__field[line][column]

    def set_cell(self, line, column, value):
        self.__field[line][column] = value

    def is_monster(self, line, column):
        return self.get_cell(line, column) == MONSTER

    def is_obstacle(self, line, column):
        return self.get_cell(line, column) == OBSTACLE

    def is_empty(self, line, column):
        return self.get_cell(line, column) == EMPTY

    def is_used(self, line, column):
        return self.get_cell(line, column) == USED

    def backup_field(self):
        """
        Store a (deep) copy of self's field, thus it is possible to apply modifications to self's field and then
        to go back to initial field state using self.restore_field().

        It can be used to store field before trying to "cross it" in order to restore it after crossing attempt.
        """
        self.__backup_field = copy.deepcopy(self.__field)
        self.__backup_pos = self.__player_pos

    def restore_field(self):
        """
        reset self's field to last 'backup field' (created using self.restore_field()),
        it is None if no backup had been made
        """
        self.__field = self.__backup_field
        self.__player_pos = self.__backup_pos

    def get_front_view(self):
        """
        Returns a five letters word representing the view in front of the player
        The word describes the view from the right of the player to his left
        :rtype: list(str)
        """
        x, y = self.__player_pos
        right = [self.__field[x][y - 1]]
        left = [self.__field[x][y + 1]]
        front = self.__field[x + 1][y - 1:y + 2]
        return ''.join(right + front + left)

    @staticmethod
    def get_view_code(view):
        """
        Converts the view in a position in the command list
        :type view: list(str)
        :rtype: int
        :UC: view must be a valid view
        """
        return int(''.join([str(CELLS.index(cell)) for cell in view]), 3)

    def cross(self, individual):
        """
        Tries to cross the Field
        :type individual: Individual
        :rtype: int, int
        :UC: none
        """
        self.backup_field()
        commands = individual.get_value()
        used = 0
        individual.active()
        while individual.get_state() is PlayerState.active:
            used += 1
            view = self.get_front_view()
            code = self.get_view_code(view)
            direction = commands[code]
            move = HauntedField.MOVES[direction]
            target_line = self.__player_pos[0] + move[0]
            target_column = self.__player_pos[1] + move[1]
            target_cell_state = self.__field[target_line][target_column]
            if used >= self.__height * self.__width / 2:
                individual.alive()
            if target_cell_state == EMPTY:
                self.__player_pos = target_line, target_column
            elif target_cell_state == MONSTER:
                individual.monster()
            elif target_cell_state == OBSTACLE:
                individual.blocked()
            if self.__player_pos[0] == self.__height - 1:
                individual.success()
        self.restore_field()
        return self.__player_pos[0], used

    def __str__(self):
        """
        a string representation of self
        """
        result = ''
        for line in range(self.__height + 2):
            result = result + str(line) + ''.join(self.__field[line]) + '\n'
        # result = '\n'.join([''.join(self.__field[line]) for line in range(self.__height+2)])
        return result

    def __repr__(self):
        """
        a convenient string representation for python console
        """
        return self.__str__()


if __name__ == "__main__":
    b = HauntedField(6, 6, 4)
    print(b)
