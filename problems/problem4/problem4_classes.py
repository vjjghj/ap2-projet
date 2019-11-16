from problem_interface import Problem
from individual_interface import Individual


class HauntedTerrainProblem(Problem):
    def __init__(self):
        super(HauntedTerrainProblem, self).__init__(False)

    def create_individual(self):
        pass

    def evaluate_fitness(self, individual):
        pass

    def adapt(self, individual):
        pass


class HauntedTerrainIndividual(Individual):
    @staticmethod
    def get_random_gene():
        pass

    @staticmethod
    def mutate_once(gene, probability):
        pass
