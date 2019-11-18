from random import shuffle
from problem_interface import Problem


class AlgoGen(object):
    """
    This class is used to solve a given problem by using a genetic algorithm
    Handles the population, its evolution, and returns the best fitted individual for the given problem
    """
    def __init__(self, problem, population_size, mutation_probability, crossover_rate):
        """
        Creates a AlgoGen object
        :param problem: The problem the population is used to solve.
        :type problem: Problem
        :param population_size: The size of the population we want to create
        :type population_size: int
        :param mutation_probability: The probability a gene mutates
        :type mutation_probability: int or float
        :param crossover_rate:
        :UC: population_size % 2 == 0 and population_size >= 5 and 0 < mutation_probability < 1
        """
        self.population = [problem.create_individual() for _ in range(population_size)]
        self.size = population_size
        self.problem = problem
        self.mutation_probability = mutation_probability
        self.crossover_rate = crossover_rate
        print('Solver initialized')

    def shuffle(self):
        """
        Randomly shuffles the population
        :return: none
        """
        shuffle(self.population)

    def iter_random_pairs(self):
        """
        Returns a zip object formed with pairs of individuals from population
        Each individual is taken exactly once unless self.size % 2 != 0
        :rtype: zip
        :UC: self.size % 2 == 0 and len(self.population) == self.size
        """
        self.shuffle()
        return zip(self.population[:self.size // 2], self.population[self.size // 2:])

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
        next_gen1 = self.next_gen_creator(lambda x, y: self.problem.tournament(x, y))
        next_gen2 = self.next_gen_creator(lambda x, y: self.problem.tournament(*x.cross_with(y)))
        return next_gen1 + next_gen2

    def mutate(self, population):
        """
        Make all individuals from population mutate
        :type population: list(Individual)
        :return: none
        """
        for individual in population:
            individual.mutate(self.mutation_probability)

    def iter_gen(self):
        """
        Iterates a round of adaptation to self.population
        :return: none
        """
        best_five = self.problem.sort_population(self.population)[:5]
        next_gen = self.next_gen()
        self.mutate(next_gen)
        next_gen_best = self.problem.sort_population(next_gen)[:-5]
        self.population = best_five + next_gen_best

    def get_current_best(self):
        """
        Returns the current best fitted Individual in self.population and its fitness
        :rtype: Individual, depending on the problem, int or float
        """
        if self.problem.maximize:
            current_best = max(self.population, key=lambda x: x.score)
        else:
            current_best = min(self.population, key=lambda x: x.score)
        return current_best, self.problem.adapt(current_best), current_best.score

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
        return sum([individual.get_score() for individual in self.population]) / self.size

    def solve(self, iterations):
        """
        Runs the genetic algorithm to solve the given problem
        On each round, prints the current best element of population
        :param iterations: number of iterations to run to optimize the solution
        :type iterations: int
        :rtype: Individual, depending on the problem, int or float
        :UC: iterations > 0
        """
        current_best = ()
        for i in range(iterations):
            self.iter_gen()
            current_best = self.get_current_best()
            average = self.average_fitness()
            print('Iteration {}: value:{}, fitness: {}, average: {}'.format(i, *current_best[1:], average))
        return current_best
