from random import randint


class Individual(object):
    """
    Creates a parent class for the different individual we will use to solve problems
    Function to create/override:
        evaluate(self, problem)
        get_random_gene(self)
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
        :return: Individual
        """
        other = Individual(self.size)
        other.set_score(self.score)
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
        :param problem: (Problem)
        :return: none
        """
        pass

    def get_score(self):
        """
        Returns the fitness score for self
        :return: (int or float)
        """
        return self.score

    def get_size(self):
        """
        Returns the size of self's genome
        :return: (int)
        """
        return self.size

    def get_value(self):
        """
        Returns the genome of self
        :return: (list)
        """
        return self.genome

    @staticmethod
    def get_random_gene():
        """
        Returns a random value for a gene, depending on the problem
        :rtype: depends on the problem
        """
        pass

    def init_value(self):
        """
        Randomly intitializes self's genome
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
        :param probability: (float)
        :return: none
        :UC: 0 <= float < 1
        """
        self.genome = [self.mutate_once(gene, probability) for gene in self.genome]

    def set_score(self, new_score):
        """
        Changes the fitness score of self
        :param new_score: (int or float)
        :return: none
        """
        self.score = new_score

    def set_value(self, new_value, problem=None):
        """
        Changes the genome value of self
        If a problem is given, will actualize self.score accordingly
        :type new_value: list
        :type problem: Problem
        :return: none
        """
        self.genome = new_value
        if problem:
            self.evaluate(problem)

    def __str__(self):
        return ''.join(map(str, self.genome))
