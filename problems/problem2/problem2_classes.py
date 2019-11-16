from problem_interface import Problem
from individual_interface import Individual
from random import choice, random


LETTERS = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [' ']


class SecretMessageProblem(Problem):
    def __init__(self, message_to_find):
        self.message_to_find = list(map(lambda x: LETTERS.index(x), list(message_to_find)))
        self.message_length = len(message_to_find)
        super(SecretMessageProblem, self).__init__(False)

    def create_individual(self):
        return SecretMessageIndividual(self.message_length)

    def evaluate_fitness(self, individual):
        return sum([abs(i - LETTERS.index(c)) for i, c in zip(self.message_to_find, individual.get_value())])

    def adapt(self, individual):
        return ''.join(individual.get_value())


class SecretMessageIndividual(Individual):
    def evaluate(self, problem):
        self.score = problem.evaluate_fitness(self)

    @staticmethod
    def get_random_gene():
        return choice(LETTERS)

    @staticmethod
    def mutate_once(gene, probability):
        return gene if probability < random() else SecretMessageIndividual.get_random_gene()
