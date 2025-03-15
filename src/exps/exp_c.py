import time

from point import Point
from quadTreeNode import QuadTreeNode
from invertedIndex import InvertedIndex
from power import POWER
from power_batch import POWER_batch, group_queries_by_proximity
from query import Query
from read_data import parse_files

X_MIN, X_MAX = -180, 180
Y_MIN, Y_MAX = -90, 90


def exp_c(path, query_num):
    print("Please do not run exp-c")
    raise NotImplementedError