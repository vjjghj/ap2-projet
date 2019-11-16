from random import shuffle
from problem_interface import Problem
from individual_interface import Individual


class AlgoGen(object):
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
        :UC: population_size % 2 == 0 and population_size >= 5
        """
        if population_size % 2 == 1 or population_size < 5:
            raise ValueError('The population size must be even and greater than 4')
        self.population = [problem.create_individual() for _ in range(population_size)]
        self.size = population_size
        self.problem = problem
        self.mutation_probability = mutation_probability
        self.crossover_rate = crossover_rate

    def shuffle(self):
        """
        Randomly shuffles the population
        :return: none
        """
        shuffle(self.population)

    def iter_random_pairs(self):
        """
        Returns an zip object formed with pairs of individuals from population
        Each individual is taken exactly once unless self.size % 2 != 0
        :rtype: zip
        """
        return zip(self.population[:self.size // 2], self.population[self.size // 2:])

    def next_gen_creator(self, selection_method):
        """
        Creates a list of individuals from self.population using selection_method
        :type selection_method: function
        :rtype: list(Individual)
        :UC: selection must a valid function with shape [Individual, Individual] -> Individual
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

    def mutate(self):
        """
        Make all Individual from self.population mutate
        :return: none
        """
        self.population = [individual.mutate(self.mutation_probability) for individual in self.population]

    def iter_gen(self):
        """
        Iterates a round of adaptation to self.population
        :return: none
        """
        best_five = self.problem.sort_population(self.population)[:5]
        next_gen = self.next_gen()
        next_gen_best = self.problem.sort_population(next_gen)[:-5]
        self.population = best_five + next_gen_best

    def get_current_best(self):
        """
        Returns the current best fitted Individual in self.population and its fitness
        :rtype: Individual, float
        """
        if self.problem.maximize:
            current_best = max(self.population, key=lambda x: x.score)
        else:
            current_best = min(self.population, key=lambda x: x.score)
        return current_best, self.problem.adapt(current_best), current_best.score

    def average_fitness(self):
        return sum([individual.get_score() for individual in self.population]) / self.size

    def solve(self, iterations):
        """
        Runs the genetic algorithm to solve the given problem
        :param iterations: number of iterations to run to optimize the solution
        :type iterations: int
        :rtype: Individual
        :UC: iterations > 0
        """
        current_best = ()
        for i in range(iterations):
            self.iter_gen()
            current_best = self.get_current_best()
            average = self.average_fitness()
            print('Iteration {}: value:{}, fitness: {}, average: {}'.format(i, *current_best[1:], average))
        return current_best
