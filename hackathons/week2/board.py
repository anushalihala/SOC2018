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