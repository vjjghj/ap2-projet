import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from input_checker import *
from problems.problem3.problem3_classes import LabyrinthProblem
from algo_gen import AlgoGen


if __name__ == '__main__':
    pass
