class Problem(object):
    """
    Parent class for the different problems we will have to solve
    Function to create/override:
        __init__(self, *args)
        create_individual(self)
        evaluate_fitness(self, individual)
        adapt(self, individual)
    """
    def __init__(self, maximize):
        """
        Creates a problem, only argument is used to choose whether the fitness score has to be maximized or not
        :type maximize: boolean
        """
        self.maximize = maximize

    def best_individual(self, population):
        """
        Returns the best fitted individual from population.
        Depending on the problem, it can corresponds to the individual with highest or lowest fitness value
        :type population: list(Individual)
        :rtype: Individual
        """
        return max(population, key=lambda x: self.evaluate_fitness(x))

    def create_individual(self):
        """
        Creates a randomly generated individual for this problem
        :rtype: Individual
        """
        pass

    def evaluate_fitness(self, genome):
        """
        Compute the fitness of individual for this problem
        :type genome: list
        :rtype: float
        """
        pass

    def evaluate_fitness_for_all(self, population):
        """
        Updates the score value for each individual in population
        :type population: list(Individual)
        :return: none
        """
        for individual in population:
            individual.evaluate(self)

    def sort_population(self, population):
        """
        Sort population from best fitted to worst fitted.
        Depending on the problem, it can corresponds to ascending or descending order
        :type population: list(Individual)
        :rtype: list(Individual)
        """
        self.evaluate_fitness_for_all(population)
        return sorted(population, key=lambda x: x.score, reverse=self.maximize)

    def tournament(self, first, second):
        """
        Performs a tournament between two individuals, returns the most fitted one
        :type first: Individual
        :type second: Individual
        :rtype: Individual
        """
        self.evaluate_fitness_for_all([first, second])
        first_is_bigger = first.get_score() > second.get_score()
        if first_is_bigger and self.maximize or not self.maximize and not first_is_bigger:
            return first
        return second

    def adapt(self, genome):
        """
        Returns the value of the individual, based on the problem
        :type genome: list
        :rtype: depends on the problem
        """
        pass
