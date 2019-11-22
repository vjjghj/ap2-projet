from random import shuffle
from problem_interface import Problem
from base_class import Base


class AlgoGen(Base):
    """
    This class is used to solve a given problem by using a genetic algorithm
    Handles the population, its evolution, and returns the best fitted individual for the given problem
    """
    def __init__(self, **kwargs):
        """
        Creates a AlgoGen object
        :param problem: The problem the population is used to solve.
        :type problem: Problem
        :param population_size: The size of the population we want to create
        :type population_size: int
        :param mutation_probability: The probability a gene mutates
        :type mutation_probability: int or float
        :UC: population_size % 2 == 0 and population_size >= 5 and 0 <= mutation_probability < 1
        """
        self.__problem = kwargs['problem']
        self.__size = kwargs['population_size']
        self.__population = [self.__problem.create_individual() for _ in range(self.__size)]
        self.__mutation_probability = kwargs['mutation_probability']
        self.__export = kwargs.get('export', False)     # Default value is False
        self.__target_file = kwargs.get('target_file')  # Default value is None
        super(AlgoGen, self).__init__(**kwargs)
        print('Solver initialized')

    def shuffle(self):
        """
        Randomly shuffles the population
        :return: none
        """
        shuffle(self.__population)

    def iter_random_pairs(self):
        """
        Returns a zip object formed with pairs of individuals from population
        Each individual is taken exactly once unless self.size % 2 != 0
        :rtype: zip
        :UC: self.size % 2 == 0 and len(self.population) == self.size
        """
        self.shuffle()
        return zip(self.__population[:self.__size // 2], self.__population[self.__size // 2:])

    def next_gen_creator(self, selection_method):
        """
        Creates a list of individuals from self.population using selection_method
        :type selection_method: function
        :rtype: list(Individual)
        :UC: selection_method must a valid function with shape [Individual, Individual] -> Individual
        """
        return [selection_method(i1, i2) for i1, i2 in self.iter_random_pairs()]

    def next_gen(self):
        """
        Creates the next generation basis according to the problem
        :rtype: list(Individual)
        """
        next_gen1 = self.next_gen_creator(self.__problem.tournament)
        next_gen2 = self.next_gen_creator(lambda x, y: self.__problem.tournament(*x.cross_with(y)))
        return next_gen1 + next_gen2

    def mutate(self, population):
        """
        Make all individuals from population mutate
        :type population: list(Individual)
        :return: none
        """
        for individual in population:
            individual.mutate(self.__mutation_probability)

    def iter_gen(self):
        """
        Iterates a round of adaptation to self.population
        :return: none
        """
        best_five = self.__problem.sort_population(self.__population)[:5]
        next_gen = self.next_gen()
        self.mutate(next_gen)
        next_gen_best = self.__problem.sort_population(next_gen)[:-5]
        self.__population = best_five + next_gen_best

    def get_current_best(self):
        """
        Returns the current best fitted Individual in self.population and its fitness
        :rtype: Individual, depending on the problem, int or float
        """
        if self.__problem.get_maximize():
            current_best = max(self.__population, key=lambda x: x.get_score())
        else:
            current_best = min(self.__population, key=lambda x: x.get_score())
        return current_best, self.__problem.adapt(current_best), current_best.get_score()

    def current_best_str(self):
        current_best = self.get_current_best()
        return 'value: {}, fitness: {}'.format(*current_best[1:])

    @staticmethod
    def display_pop(population):
        """
        Used for debugging purposes,
        Prints every individual's fitness from population
        :type population: list(Individual)
        :return: none
        """
        print(', '.join([str(individual.get_score()) for individual in population]))

    def average_fitness(self):
        """
        Returns the average fitness score of population for problem
        :rtype: float
        """
        return sum([individual.get_score() for individual in self.__population]) / self.__size

    def solve(self, iterations):
        """
        Runs the genetic algorithm to solve the given problem
        On each round, prints the current best element of population
        :param iterations: number of iterations to run to optimize the solution
        :type iterations: int
        :rtype: Individual, depending on the problem, int or float
        :UC: iterations > 0
        """
        for i in range(iterations):
            self.iter_gen()
            average = self.average_fitness()
            best = self.current_best_str()
            print('Iterations {}; {}; average {}'.format(i, best, average))
        if self.__export:
            self.export_best()
        return self.get_current_best()

    def export_best(self):
        problem = self.__problem
        target_file = self.__target_file
        if not target_file:
            target_file = 'call_examples/' + str(problem.get_init_values()['Class']) + '.txt'
        with open(target_file, 'w') as target:
            target.write(str(self) + '\n')
            target.write(self.current_best_str())
        print('Exported')
