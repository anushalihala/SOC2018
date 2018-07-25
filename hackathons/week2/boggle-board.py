import random
import pdb

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
        
#STUB
def is_word(word):
    s = set(['MAD','HAD','HAM'])
    return word in s
#STUB
def is_path(word):
    s = set(['MAD','HAD','HAM','M','H','MA','HA'])
    return word in s
    
def get_neighbours(idx,n):
    """
    Finds indices of neighbours of current index (including diagonals)
    
    Arguments:
    idx -- current index as 2-tuple representing row and column
    n -- dimension of corresponding square board
    
    Returns:
    neighbours -- list of indices of neighbouring tiles on board
    """
    neighbours=[]
    row=idx[0]
    col=idx[1]
    
    adj_rows=[idx[0]]
    adj_cols=[idx[1]]
    
    n_range = set(range(n))
    
    if((row-1) in n_range):
        adj_rows.append(row-1)
    if((row+1) in n_range):
        adj_rows.append(row+1)
    if((col-1) in n_range):
        adj_cols.append(col-1)
    if((col+1) in n_range):
        adj_cols.append(col+1)
        
    for i in adj_rows:
        for j in adj_cols:
            neighbours.append((i,j))
    
    neighbours.remove(idx)
    return neighbours
    
def find_next_words(current_index,current_word,board,tiles_in_word):
    n=len(board)
    words=[]
    for n in get_neighbours(current_index,n):
        if(n in tiles_in_word['set']):
            continue
    
        current_ch=board[n[0]][n[1]]
        word = current_word + current_ch
        if(is_word(word)):
            words.append(word)
            
        if(is_path(word)): 
            tiles_in_word['stack'].append(n)
            tiles_in_word['set'].add(n)
            words += find_next_words(n,word,board,tiles_in_word)
            
            idx = tiles_in_word['stack'].pop()
            tiles_in_word['set'].remove(idx)
            
    return words

def find_words(board):
    """
    Finds a list of all valid words in given board
    
    Arguments:
    board -- 2d list representing square boggle board
    
    Returns:
    words -- list of valid words
    """
    tiles_in_word = {'stack':[],'set':set()}
    n=len(board)
    words=[]
    
    for i in range(n*n):
        row_no = i//n #integer division
        col_no = i%n 
        #add letter to word
        word=board[row_no][col_no]
        #add tile to tiles_in_word
        index = (row_no,col_no)
        tiles_in_word['stack']=[index]
        tiles_in_word['set']={index}

        if(is_path(word)):
            words += find_next_words(index,word,board,tiles_in_word)
            
    return words

    
#TESTING BOARD GENERATION    
# print(get_board(3,["a","e","i","o","u","b","c","d"]))
# print(get_board())
    
#TESTING WORD SEARCH
# t = {'stack':[(0,0)],'set':{(0,0)}}
# ans = find_next_words((0,0),'M',[['M','A'],['H','D']],t)

# ans=find_words([['M','A'],['H','D']])    
# for w in ans:
    # print(w)
    
# print(get_neighbours((0,0),4))
# print(get_neighbours((0,3),4))
# print(get_neighbours((3,0),4))
# print(get_neighbours((3,3),4))