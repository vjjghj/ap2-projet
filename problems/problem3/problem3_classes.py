from problem_interface import Problem
from individual_interface import Individual


class LabyrinthProblem(Problem):
    def __init__(self):
        super(LabyrinthProblem, self).__init__(False)

    def create_individual(self):
        pass

    def evaluate_fitness(self, individual):
        pass

    def adapt(self, individual):
        pass


class LabyrinthIndividual(Individual):
    @staticmethod
    def get_random_gene():
        pass

    @staticmethod
    def mutate_once(gene, probability):
        pass
