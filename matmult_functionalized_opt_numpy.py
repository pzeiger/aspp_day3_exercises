#!/usr/bin/env python3

# Program to multiply two matrices using nested loops

import numpy as np

def matmult(X,Y):
    return np.matmul(X, Y)


def get_X(N):
    """Return random NxN numpy matrix
    """
    return np.random.randint(low=0, high=100, size=(N, N))


def get_Y(N):
    """Return random Nx(N+1) numpy matrix
    """
    return np.random.randint(low=0, high=100, size=(N, N+1))


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


def main_fast(print_result=True):
    """Main function binding together the other functions.
    """
#    random.seed(314156345)
    N = 250
    np.matmul(np.random.randint(low=0, high=100, size=(N, N)), np.random.randint(low=0, high=100, size=(N, N+1)))
    return 0


if __name__ == "__main__":
    main()

