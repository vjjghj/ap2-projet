from random import randint


class Individual(object):
    """
    Parent class for the different individual we will use to solve problems
    Function to create/override:
        get_random_gene() <- static method
        mutate_once(gene, probability) <- static method
    """
    def __init__(self, size):
        self.size = size
        self.genome = list()
        self.init_value()
        self.score = 0

    def copy(self):
        """
        Returns a copy of self
        :rtype: Individual
        """
        other = type(self)(self.size)  # Allows sub class objects to be copied into the same sub class
        # other.set_score(self.score)  # Copying score turned out to be unneeded during further development
        other.set_value(self.genome)
        return other
    
    def cross_with(self, other):
        """
        Performs a 1 point crossover between self and other, return two new individuals
        :type other: Individual
        :rtype: Individual, Individual
        """
        n = randint(0, len(self.genome) - 1)
        x1, x2 = self.copy(), other.copy()
        x1.set_value(self.genome[:n] + other.genome[n:])
        x2.set_value(other.genome[:n] + self.genome[n:])
        return x1, x2

    def evaluate(self, problem):
        """
        Set the fitness score with the fitness computed by problem for self
        :type problem: Problem
        :return: none
        """
        self.score = problem.evaluate_fitness(self)

    def get_score(self):
        """
        Returns the fitness score for self
        :rtype: int or float
        """
        return self.score

    def get_size(self):
        """
        Returns the size of self's genome
        :rtype: int
        """
        return self.size

    def get_value(self):
        """
        Returns the genome of self
        :rtype: list
        """
        return self.genome

    @staticmethod
    def get_random_gene():
        """
        Returns a random value for a gene, depending on the problem
        Will be defined in sub classes, as genes used depend on the problem
        :rtype: depends on the problem
        """
        pass

    def init_value(self):
        """
        Randomly initializes self's genome
        :return: none
        """
        self.genome = [self.get_random_gene() for _ in range(self.size)]

    @staticmethod
    def mutate_once(gene, probability):
        """
        Returns the given gene, changed accordingly to the problem with a given probability
        :type gene: depends on the problem
        :type probability: int or float
        :rtype: same as gene
        """
        pass

    def mutate(self, probability):
        """
        Apply mutation operation to self: each element of the genome sequence is randomly changed with given probability
        :type probability: float
        :return: none
        :UC: 0 <= probability < 1
        """
        # A different approach should be implemented later to decrease the time and memory needed
        self.genome = [self.mutate_once(gene, probability) for gene in self.genome]

    def set_score(self, new_score):
        """
        Changes the fitness score of self
        :type new_score: int or float
        :return: none
        """
        self.score = new_score

    def set_value(self, new_value, problem=None):
        """
        Changes the genome value of self
        If a problem is given, will actualize self.score accordingly
        :type new_value: list
        :type problem: Problem or NoneType
        :return: none
        """
        self.genome = new_value
        if problem:
            self.evaluate(problem)

    def __str__(self):
        """
        Returns a str representing self's genome
        :rtype: str
        """
        return ''.join(map(str, self.genome))
        # Most individual sub classes use list(str) as genome
        # this will prevent any error in case of new problem adding
        # (At the moment, only problem1 and problem2 uses list(int),
        # which could be changed into list(str) with few modifications)
