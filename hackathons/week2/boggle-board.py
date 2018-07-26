#!/usr/bin/env python3

import time
from dictionary import Dictionary
from score import calculate_score
from board import get_board
    
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
    
def find_next_words(current_index, current_word, tiles_in_word, board, dictionary):
    """
    Finds a list of all valid words in given board for which current_word is a prefix
    
    Arguments:
    current_index -- index of last character in current_word
    current_word -- word consisting of all tiles traversed so far
    tiles_in_word -- stores the indices of the tiles that make up current_word. 
                     uses a dictionary to store both the list representation (accessible by 'stack') and set representation (accessible by 'set')
    board -- 2d list representing square boggle board   
    dictionary -- object of Dictionary class; API for methods is_path and is_word

    Returns:
    words -- list of valid words for which current_word is a prefix
    """
    n=len(board)
    words=[]
    for n in get_neighbours(current_index,n):
        if(n in tiles_in_word['set']):
            continue
    
        current_ch=board[n[0]][n[1]]
        word = current_word + current_ch
        if(dictionary.is_word(word)):
            words.append(word)
            
        if(dictionary.is_path(word)): 
            tiles_in_word['stack'].append(n)
            tiles_in_word['set'].add(n)
            words += find_next_words(n, word, tiles_in_word, board, dictionary)
            
            idx = tiles_in_word['stack'].pop()
            tiles_in_word['set'].remove(idx)
            
    return words

def find_words(board, dictionary):
    """
    Finds a list of all valid words in given board
    
    Arguments:
    board -- 2d list representing square boggle board
    dictionary -- object of Dictionary class; API for methods is_path and is_word
    
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

        if(dictionary.is_path(word)):
            words += find_next_words(index, word, tiles_in_word, board, dictionary)
            
    return words

    
def benchmarking(dictionary):
    """
    Find average time taken to find all valid (given by dictionary) in a standard boggle board of size 4x4
    
    Arguments:
    dictionary -- object of Dictionary class; API for methods is_path and is_word
    """
    sum=0
    for i in range(100):
        boggle_board = get_board()
        
        time_before=time.time()
        for j in range(10):
            find_words(boggle_board,dictionary)
        time_after=time.time()
        time_diff=time_after - time_before
        
        sum=sum+(time_diff/10)
        
    avg=sum/100
    return avg
   
   
def main():
    filename = 'boggle-dictionary.txt'
    dictionary = Dictionary(filename)
    boggle_board = get_board()
    
    print("Boggle board after shuffle:")
    for row in boggle_board:
        print(row)
    
    print("\nWords found in board:")    
    word_list = find_words(boggle_board,dictionary)    
    for word in word_list:
        print(word)
    
    #benchmarking
    print('\nAverage time taken to find words in standard 4x4 boggle board =')
    print(benchmarking(dictionary),'seconds')
    
    #Create result object
    result=dict()
    result['score']= calculate_score(word_list)
    result['words']=sorted(word_list)
    
    print('\nResult object:')
    print(result)
    
    return result

if __name__ == '__main__':
    main()
