from problem_interface import Problem
from individual_interface import Individual
from random import choice
from problems.problem4.haunted_field import PlayerState, HauntedField


class HauntedFieldProblem(Problem):
    def __init__(self, **kwargs):
        height = kwargs['height']
        width = kwargs['width']
        nb_monsters = kwargs['nb_monsters']
        fields_to_cross = kwargs['fields_to_cross']
        self.fields = [HauntedField(height, width, nb_monsters) for _ in range(fields_to_cross)]
        super(HauntedFieldProblem, self).__init__(True, **kwargs)

    def create_individual(self):
        """
        Creates individual with genome length 3^5 = 243
        :rtype: Individual
        """
        return HauntedFieldIndividual(243)

    def evaluate_fitness(self, individual):
        score = 0
        for field in self.fields:
            line, used = field.cross(individual)
            score += used + line * field.get_height()
            state = individual.get_state()
            if state == PlayerState.success:
                score += (field.get_width() * field.get_height() - used) * 10
            elif state == PlayerState.blocked:
                score += (field.get_height() - line) * 2
            elif state == PlayerState.monster:
                score += (field.get_height() - line) * 20
        return score

    def adapt(self, individual):
        """
        Considering we cant print the field and the path of individual based on the commands on each iteration,
            adapt will only return the genome of individual as a str
        :type individual: Individual
        :rtype: str
        """
        return str(individual)


class HauntedFieldIndividual(Individual):
    """
    Individuals with list of directions as genome
    """
    def __init__(self, *args, **kwargs):
        """
        Creates an individual to solve the haunted field problem
        We use not kwarg but we leave it here in case of later modifications
        """
        self.__state = PlayerState.active
        super(HauntedFieldIndividual, self).__init__(*args, **kwargs)

    @staticmethod
    def get_random_gene():
        """
        Returns a random valid direction
        :rtype: str
        """
        return choice(['u', 'd', 'r', 'l'])

    @staticmethod
    def mutate_once(gene):
        """
        The gene takes the value of a random different valid direction
        :type gene: str
        :rtype: str
        """
        new_gene = HauntedFieldIndividual.get_random_gene()
        while gene == new_gene:
            new_gene = HauntedFieldIndividual.get_random_gene()
        return new_gene

    def get_state(self):
        return self.__state

    def active(self):
        self.__state = PlayerState.active

    def success(self):
        self.__state = PlayerState.success

    def monster(self):
        self.__state = PlayerState.monster

    def blocked(self):
        self.__state = PlayerState.blocked

    def alive(self):
        self.__state = PlayerState.alive


def tester(individual, width, height, nb_monsters, fields_to_cross):
    """
    Tests the number of fields the given individual can cross when trying fields_to_cross times
    :type individual: HauntedFieldIndividual
    :type width: int
    :type height: int
    :type nb_monsters: int
    :type fields_to_cross: int
    :rtype: int
    """
    fields = [HauntedField(height, width, nb_monsters) for _ in range(fields_to_cross)]
    crossed = 0
    for field in fields:
        field.cross(individual)
        if individual.get_state() is PlayerState.success:
            crossed += 1
    return crossed
