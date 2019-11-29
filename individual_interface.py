from random import randint, choices, random


class Individual(object):
    """
    Parent class for the different individual we will use to solve problems
    Function to create/override:
        get_random_gene() <- static method
        mutate_once(gene, probability) <- static method
    """
    def __init__(self, size):
        self.__size = size
        self.__genome = list()
        self.__init_value()
        self.__score = 0

    def copy(self):
        """
        Returns a copy of self
        :rtype: Individual
        """
        other = type(self)(self.__size)  # Allows sub class objects to be copied into the same sub class
        # other.set_score(self.score)  # Copying score turned out to be unneeded during further development
        other.set_value(self.__genome)
        return other
    
    def cross_with(self, other, iterations=1):
        """
        Performs a iterations point(s) crossover between self and other, return two new individuals
        :type other: Individual
        :type iterations: int
        :rtype: Individual, Individual
        :UC: none
        """
        x1, x2 = self.copy(), other.copy()
        for i in range(iterations):
            n = randint(0, len(self.__genome) - 1)
            x1.set_value(x1.get_value()[:n] + x2.get_value()[n:])
            x2.set_value(x2.get_value()[:n] + x1.get_value()[n:])
        return x1, x2

    def evaluate(self, problem):
        """
        Set the fitness score with the fitness computed by problem for self
        :type problem: Problem
        :return: none
        :UC: none
        """
        self.__score = problem.evaluate_fitness(self)

    def get_score(self):
        """
        Returns the fitness score for self
        :rtype: int or float
        """
        return self.__score

    def get_size(self):
        """
        Returns the size of self's genome
        :rtype: int
        """
        return self.__size

    def get_value(self):
        """
        Returns the genome of self
        :rtype: list
        """
        return self.__genome

    @staticmethod
    def get_random_gene():
        """
        Returns a random value for a gene, depending on the problem
        Will be defined in sub classes, as genes used depend on the problem
        :rtype: depends on the problem
        """
        pass

    def __init_value(self):
        """
        Randomly initializes self's genome
        :return: none
        """
        self.__genome = [self.get_random_gene() for _ in range(self.__size)]

    @staticmethod
    def mutate_once(gene):
        """
        Returns the given gene, changed accordingly to the problem with a given probability
        :type gene: depends on the problem
        :rtype: same as gene
        :UC: none
        """
        pass

    def mutate(self, probability):
        """
        Apply mutation operation to self: each element of the genome sequence is randomly changed with given probability
        :type probability: float
        :return: none
        :UC: 0 <= probability < 1
        """
        number_of_mutations = sum([1 for _ in range(self.__size) if probability > random()])
        for i in choices(range(self.__size), k=number_of_mutations):
            self.__genome[i] = self.mutate_once(self.__genome[i])

    def set_score(self, new_score):
        """
        Changes the fitness score of self
        :type new_score: int or float
        :return: none
        :UC: none
        """
        self.__score = new_score

    def set_value(self, new_value, problem=None):
        """
        Changes the genome value of self
        If a problem is given, will actualize self.score accordingly
        :type new_value: list
        :type problem: Problem or NoneType
        :return: none
        :UC: new_value must be a valid genome for the problem
        """
        self.__genome = new_value.copy()  # Using copy prevents unwanted side effects (happened with mutations)
        if problem:
            self.evaluate(problem)

    def __str__(self):
        """
        Returns a str representing self's genome
        :rtype: str
        """
        return ''.join(map(str, self.__genome))
        # Most individual sub classes use list(str) as genome
        # this will prevent any error in case of new problem adding
        # (At the moment, only problem1 and problem2 uses list(int),
        # which could be changed into list(str) with few modifications)
