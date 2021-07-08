from matplotlib.pyplot import axis, grid, show, plot, scatter
from numpy import sqrt, array
from random import randint
from copy import deepcopy

DEPOT = [0, 0]
NB_INTER = 0
NB_2OPT = 0

def creer_client_alea(n=10):
    CLIENTS = []
    for _ in range(n):
        CLIENTS.append([randint(-100, 100), randint(-100, 100)])
    return CLIENTS

CLIENTS = creer_client_alea(20)