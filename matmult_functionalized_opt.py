#!/usr/bin/env python3

# Program to multiply two matrices using nested loops

import random

def matmult(X,Y):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]


def get_X(N):
    """Return random NxN numpy matrix
    """
    return [[random.randint(0,100) for j in range(N) ] for i in range(N)]


def get_Y(N):
    """Return random Nx(N+1) numpy matrix
    """
    return [[random.randint(0,100) for j in range(N+1)] for i in range(N)]


def main(print_result=True):
    """Main function binding together the other functions.
    """
#    random.seed(314156345)
    N = 250
    X = get_X(N)
    Y = get_Y(N)
    result = matmult(X,Y)
    if print_result:
        for r in result:
            print(r)
    
    return 0

if __name__ == "__main__":
    main()

