from base_class import Base


class Problem(Base):
    """
    Parent class for the different problems we will have to solve
    Function to create/override:
        __init__(self, **kwargs)
        create_individual(self)
        evaluate_fitness(self, individual)
        adapt(self, individual)
    """
    def __init__(self, maximize, **kwargs):
        """
        Creates a problem, only argument is used to choose whether the fitness score has to be maximized or not
        :type maximize: boolean
        """
        self.__maximize = maximize
        super(Problem, self).__init__(**kwargs)
        print('Problem initialized')

    def create_individual(self):
        """
        Creates a randomly generated individual for this problem
        :rtype: Individual
        """
        pass

    def evaluate_fitness(self, individual):
        """
        Compute the fitness of individual for this problem
        :type individual: Individual
        :rtype: float
        :UC: individual must be a valid individual for the problem
        """
        pass

    def evaluate_fitness_for_all(self, population):
        """
        Updates the score value for each individual in population
        :type population: list(Individual)
        :return: none
        :UC: none
        """
        for individual in population:
            individual.evaluate(self)

    def sort_population(self, population):
        self.evaluate_fitness_for_all(population)
        """
        Sort population from best fitted to worst fitted.
        Depending on the problem, it can corresponds to ascending or descending order
        :type population: list(Individual)
        :rtype: list(Individual)
        :UC: none
        """
        return sorted(population, key=lambda x: x.get_score(), reverse=self.__maximize)

    def tournament(self, first, second):
        """
        Performs a tournament between two individuals, returns the most fitted one
        :type first: Individual
        :type second: Individual
        :rtype: Individual
        :UC: none
        """
        self.evaluate_fitness_for_all([first, second])
        first_is_bigger = first.get_score() > second.get_score()
        if first_is_bigger and self.__maximize or not self.__maximize and not first_is_bigger:
            return first.copy()
        return second.copy()

    def adapt(self, individual):
        """
        Returns the value of the individual, based on the problem
        :type individual: Individual
        :rtype: depends on the problem
        :UC: none
        """
        pass

    def get_maximize(self):
        """
        Returns the value of maximize
        :rtype: boolean
        """
        return self.__maximize
