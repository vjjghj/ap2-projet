class Problem(object):
    def best_individual(self, population):
        """
        Returns the best fitted individual from population.
        Depending on the problem, it can corresponds to the individual with highest or lowest fitness value
        :param population: (list(Individual))
        :return: (Individual)
        """
        return max(population, key=lambda x: self.evaluate_fitness(x))

    def create_individual(self):
        """
        Creates a randomly generated individual for this problem
        :return: (Individual)
        """
        pass

    def evaluate_fitness(self, individual):
        """
        Compute the fitness of individual for this problem
        :param individual: (Individual)
        :return: (float)
        """
        pass

    def sort_population(self, population):
        """
        Sort population from best fitted to worst fitted.
        Depending on the problem, it can corresponds to ascending or descending order
        :param population:
        :return:
        """
        return sorted(population, key=lambda x: self.evaluate_fitness(x))

    def tournament(self, first, second):
        """
        Performs a tournament between two individuals, returns the most fitted one
        :param first: (Individual)
        :param second: (Individual)
        :return: (Individual)
        """
        if self.evaluate_fitness(first) > self.evaluate_fitness(second):
            return first
        return second
