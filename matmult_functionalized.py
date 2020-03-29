#!/usr/bin/env python3

# Program to multiply two matrices using nested loops

import random

def matmult(X,Y):
    
    # result is Nx(N+1)
    result = []
    for i in range(len(X)):
        result.append([0] * (len(Y[0])))
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def get_X(N):
    """Return random NxN matrix
    """
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X


def get_Y(N):
    """Return random Nx(N+1) matrix
    """
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y


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

