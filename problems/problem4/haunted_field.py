import random
import copy

EMPTY = ' '
MONSTER = 'M'
OBSTACLE = '*'
USED = '.'


class HauntedField(object):

    def __init__(self, height, width):
        """
        haunted field is a 2D array of height * width char,
        initially all cells are EMPTY
        cells coordinate range from (1,1) to (height,width)
        a border of OBSTACLE cells is added (line and column 0, line (height+1) and column (width+))

        :param height: height of the field
        :type height: int
        :param width: width of the field
        :type width : int
        """
        self.__width = width
        self.__height = height
        self.__field = [[EMPTY for _ in range(self.__width + 2)] for _ in range(self.__height + 2)]
        self.__init_borders()

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
        """
        for line in range(1, self.__height - 1):
            monster_columns = random.sample(range(1, self.__width + 1), random.randint(2, nb_monsters_per_lines))
            for column in monster_columns:
                self.set_cell(line + 1, column, MONSTER)

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

    def restore_field(self):
        """
        reset self's field to last 'backup field' (created using self.restore_field()),
        it is None if no backup had been made
        """
        self.__field = self.__backup_field

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
        a convenient string representation for pyhton console
        """
        return self.__str__()


if __name__ == "__main__":
    b = HauntedField(6, 6)
    b.init_monsters(4)
    print(b)
