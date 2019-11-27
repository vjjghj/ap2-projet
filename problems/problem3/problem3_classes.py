from problem_interface import Problem
from individual_interface import Individual
from problems.problem3.maze import Maze
from random import choice
from math import floor


class LabyrinthProblem(Problem):
    """
    In this problem we want to find the shortest way out of a maze
    Individual's genome will be a list of directions
    """
    def __init__(self, **kwargs):
        """
        Creates a problem where the goal is to find the shortest way out of a maze
        Uses individuals with direction genes, with genome length equal to the number of cells in the maze
        :type maze_file: str
        :UC: maze_file has to be a valid path to a valid maze file
        """
        self.__maze = Maze(kwargs['maze_file'])
        self.__max_length = self.__maze.get_size()
        super(LabyrinthProblem, self).__init__(maximize=True, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome length equal to max_length
        :rtype: Individual
        :UC: none
        """
        return LabyrinthIndividual(self.__max_length)

    def evaluate_fitness(self, individual):
        """
        Returns the fitting score of the genome of individual in this problem
        Depends on the maze
        :type individual: Individual
        :rtype: int
        :UC: none
        """
        nb_steps, distance = self.__maze.try_path(individual.get_value())
        adapted_distance = floor(self.__maze.get_width() / 2) - distance
        score = max(0, adapted_distance) ** 2 + nb_steps
        if distance == 0:
            score += 1000
        return score

    def adapt(self, individual):
        """
        Considering we cant print the maze and the path of individual on each iteration,
            adapt will only return the genome of individual as a str
        :type individual: Individual
        :rtype: str
        :UC: none
        """
        return str(individual)

    def get_maze(self):
        """
        Returns the current maze
        :rtype: Maze
        :UC: none
        """
        return self.__maze


class LabyrinthIndividual(Individual):
    """
    Individuals with list of directions as genome
    """
    @staticmethod
    def get_random_gene():
        """
        Returns a random direction
        :rtype: str
        :UC: none
        """
        return choice(Maze.DIRECTIONS)

    @staticmethod
    def mutate_once(gene):
        """
        The gene takes the value of a random different valid direction
        :type gene: str
        :rtype: str
        :UC: none
        """
        new_gene = LabyrinthIndividual.get_random_gene()
        while gene == new_gene:
            new_gene = LabyrinthIndividual.get_random_gene()
        return new_gene
