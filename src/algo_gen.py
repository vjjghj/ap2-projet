from random import shuffle
from problem_interface import Problem
from base_class import Base
import time
import matplotlib.pyplot as plt


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
        self.__crossover_iter = kwargs['crossover_iterations']
        self.__export = kwargs['export']

        # The three following attributes are used for graph representation of convergence
        self.__bests = list()
        self.__averages = list()
        self.__times = list()
        super(AlgoGen, self).__init__(**kwargs)
        print('Solver initialized')

    def __shuffle(self):
        """
        Randomly shuffles the population
        :return: none
        """
        shuffle(self.__population)

    def __iter_random_pairs(self):
        """
        Returns a zip object formed with pairs of individuals from population
        Each individual is taken exactly once unless self.size % 2 != 0
        :rtype: zip
        """
        self.__shuffle()
        return zip(self.__population[:self.__size // 2], self.__population[self.__size // 2:])

    def __next_gen_creator(self, selection_method):
        """
        Creates a list of individuals from self.population using selection_method
        :type selection_method: function
        :rtype: list(Individual)
        :UC: selection_method must a valid function with shape [Individual, Individual] -> Individual
        """
        return [selection_method(i1, i2) for i1, i2 in self.__iter_random_pairs()]

    def __next_gen(self):
        """
        Creates the next generation basis according to the problem
        :rtype: list(Individual)
        """
        next_gen1 = self.__next_gen_creator(self.__problem.tournament)
        next_gen2 = self.__next_gen_creator(
            lambda x, y: self.__problem.tournament(*x.cross_with(y, self.__crossover_iter)))
        return next_gen1 + next_gen2

    def __mutate(self, population):
        """
        Make all individuals from population mutate
        :type population: list(Individual)
        :return: none
        :UC: none
        """
        for individual in population:
            individual.mutate(self.__mutation_probability)

    def iter_gen(self):
        """
        Iterates a round of adaptation to self.population
        :return: none
        """
        best_five = self.__problem.sort_population(self.__population)[:5]
        next_gen = self.__next_gen()
        self.__mutate(next_gen)
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

    @staticmethod
    def display_pop(population):
        """
        Used for debugging purposes,
        Prints every individual's fitness from population
        :type population: list(Individual)
        :return: none
        :UC: none
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
        base_time = time.time()
        for i in range(iterations):
            self.iter_gen()
            average = self.average_fitness()
            best = self.get_current_best()
            best_str = 'value: {}, fitness: {}'.format(*best[1:])
            print('Iterations {}; {}; average {}'.format(i, best_str, average))
            self.__bests.append(best[2])
            self.__averages.append(average)
            self.__times.append(time.time() - base_time)
        if self.__export:
            self.export_best(iterations, time.time() - base_time)
        return self.get_current_best()

    def export_best(self, iterations, total_time):
        """
        Exports the best individual in a .txt file
        :type iterations: int
        :type total_time: float
        :return: none
        """
        problem = self.__problem
        target_file = 'call_examples/' + str(problem.get_init_values()['Class']) + '/'
        with open(target_file + 'final_best_individual.txt', 'w') as target:
            target.write(str(self) + '\n')
            target.write('iterations: ' + str(iterations) + ' | ' + 'time: ' + str(total_time) +
                         ' | ' + 'time per iteration: ' + str(total_time / iterations) + '\n')
            target.write('value: {}, fitness: {}'.format(*self.get_current_best()[1:]))
        self.plot(target_file)
        print('Exported')

    def get_bests(self):
        """
        Returns the list of the fitness of the best individuals through solving
        :rtype: list(float)
        """
        return self.__bests

    def get_averages(self):
        """
        Returns the list of the average fitness of individuals through solving
        :rtype: list(float)
        """
        return self.__averages

    def get_times(self):
        """
        Returns the list of time per iteration through solving
        :rtype: list(float)
        """
        return self.__times

    def plot(self, target_file):
        x1 = self.__bests
        x2 = self.__averages
        y = list(range(len(self.__averages)))
        y_times = self.__times

        # Generating plot based on iterations
        plt.plot(y, x1, label="best depending on the number of iterations", linewidth=0.5, color="r")
        plt.plot(y, x2, label="average depending on the number of iterations", linewidth=0.5, color="b")
        plt.title("Bests & Averages depending on the number of iterations")
        plt.legend()
        plt.savefig(target_file + 'value_over_iterations.png')
        plt.close()

        # Generating plot based on time
        plt.plot(y_times, x1, label="best depending on the time", linewidth=0.5, color="r")
        plt.plot(y_times, x2, label="average depending on the time", linewidth=0.5, color="b")
        plt.title(" Bests & Averages depending on the time ")
        plt.legend()
        plt.savefig(target_file + 'value_over_time.png')
        plt.close()
