#!/usr/bin/env python3

import random


def get_board(n=-1, distribution=None):
    """
    Generates a boggle board; 
    no arguments - with dimensions of 4x4, based on dice distribution of new boggle version
    arguments given - with dimensions of nxn, based on distribution obtained from with replacement sampling of list
    
    Arguments:
    n (optional) -- dimensions of board 
    distribution (optional) -- list of characters to be sampled from
    
    Returns:
    board -- 2d list of size n x n containing characters (where n=4 by default)
    """
    if(n==-1):
        die =  {0:'AAEEGN',
                1:"ELRTTY",
                2:"AOOTTW",
                3:"ABBJOO",
                4:"EHRTVW",
                5:"CIMOTU",
                6:"DISTTY",
                7:"EIOSST",
                8:"DELRVY",
                9:"ACHOPS",
                10:"HIMNQU",
                11:"EEINSU",
                12:"EEGHNW",
                13:"AFFKPS",
                14:"HLNNRZ",
                15:"DEILRX"}
        
        #initialise board
        board = [ ["" for j in range(4)] for i in range(4)]
        
        for i in range(16):
            row_no = i//4 #integer division
            col_no = i%4 
            dice_throw =  random.randint(0,5)
            board[row_no][col_no] = die[i][dice_throw]
    else:
        #initialise board
        board = [ ["" for j in range(n)] for i in range(n)]
        
        for i in range(n*n):
            row_no = i//n #integer division
            col_no = i%n 
            dice_throw =  random.randint(0,len(distribution)-1)
            board[row_no][col_no] = distribution[dice_throw]

    return board


def get_neighbours(idx, n):
    """
    Finds indices of neighbours of current index (including diagonals)

    Arguments:
    idx -- current index as 2-tuple representing row and column
    n -- dimension of corresponding square board

    Returns:
    neighbours -- list of indices of neighbouring tiles on board
    """
    neighbours = []
    row = idx[0]
    col = idx[1]

    adj_rows = [idx[0]]
    adj_cols = [idx[1]]

    n_range = set(range(n))

    if ((row - 1) in n_range):
        adj_rows.append(row - 1)
    if ((row + 1) in n_range):
        adj_rows.append(row + 1)
    if ((col - 1) in n_range):
        adj_cols.append(col - 1)
    if ((col + 1) in n_range):
        adj_cols.append(col + 1)

    for i in adj_rows:
        for j in adj_cols:
            neighbours.append((i, j))

    neighbours.remove(idx)
    return neighbours
