#!/usr/bin/env python3

#TEAM MEMBERS
#Anusha Lihala; https://github.com/anushalihala
#Lisa Liu; https://github.com/lisaisfabu
#Solange Umuhire Gasengayire; https://github.com/SolangeUG

import random
import time

class TrieNode(object):
    """
    This class represents a node in a trie
    """

    def __init__(self, text: str):
        """
        Constructor: initialize a trie node with a given text string
        :param text: text string at this trie node
        """
        self.__text = text
        self.__children = {}
        self.__ends_word = False

    def get_text(self):
        """
        Return the text at this trie node
        :return: text string stored at this node
        """
        return self.__text

    def get_ends_word(self):
        """
        Does this node end a word?
        :return: True if this node ends a word, False otherwise
        """
        return self.__ends_word

    def set_ends_word(self, ends_word: bool):
        """
        Set whether or not this node ends a word in a trie
        :param ends_word: value determining whether this node ends a word
        :return: None
        """
        self.__ends_word = ends_word

    def get_children(self):
        """
        Return a collection of this trie node's children
        :return: this node's children
        """
        return self.__children

    def get_child(self, char: str):
        """
        Return the child trie node that is found when you follow the link from the given character
        :param char: the character in the key
        :return: the trie node the given character links to, or None if that link is not in trie
        """
        if char in self.__children.keys():
            return self.__children[char]
        else:
            return None

    def insert(self, char: str):
        """
        Insert a character at this trie node
        :param char: the character to be inserted
        :return: the newly created trie node, or None if the character is already in the trie
        """
        if char not in self.__children:
            next_node = TrieNode(self.__text + char)
            self.__children[char] = next_node
            return next_node
        else:
            return None

            
class Dictionary(object):
    """
    This class implements a word dictionary using a trie as data structure.
    """

    def __init__(self, dictionary: str):
        """
        Constructor: initialize a dictionary object from a text file
        The root of our dictionary (trie) is an empty string trie node.
        :param dictionary: text file containing dictionary words
        """
        self.__dictionary = dictionary
        self.__root = TrieNode('')
        self.__load_dictionary()

    def is_word(self, text: str):
        """
        Determine whether a given text string corresponds to a word in our dictionary
        :param text: the text to be checked
        :return: True if the text is in our dictionary,
                 False otherwise
        """
        if not text:
            # return immediately if dealing with empty strings
            return False

        # start exploring from the root
        current = self.__root
        # let's assume the provided text does exist in our dictionary
        exists = True
        upper_case_text = text.upper()

        # check that for each character, there exists a child node link from our trie root
        for char in upper_case_text:
            child = current.get_child(char)
            if not child:
                # at this point, there's no link from the root to the current character
                # therefore, the provided text does not exist in our dictionary, and we can return early
                exists = False
                return exists
            # otherwise: if a link (child) is found, continue exploring
            current = child

        # when we reach this point, we've finished looping through the characters in the text
        if exists:
            exists = current and current.get_ends_word()
        return exists

    def is_path(self, prefix: str):
        """
        Determine whether a given string is a prefix to a word in the dictionary
        :param prefix: the text to check
        :return: True if the prefix exists in the dictionary
                 False otherwise
        """
        if not prefix:
            return False

        # start exploration from the root node
        current = self.__root
        upper_case_prefix = prefix.upper()

        # check that for each character, there exists a child node link from our trie root
        for char in upper_case_prefix:
            child = current.get_child(char)
            if not child:
                # at this point, there's no link from the root to the current character
                # therefore, the provided prefix does not exist in our dictionary, and we can return early
                return False
            # otherwise: if a link (child) is found, continue exploring
            current = child

        # when we reach this point, all characters in the prefix have been found in the trie
        return True

    def __load_dictionary(self):
        """
        Load a dictionary text file into our dictionary object (private method)
        :return: None
        """
        if self.__dictionary:
            try:
                dict_file = open(self.__dictionary, "r")
                for line in dict_file:
                    # make sure to only add non empty strings
                    if line:
                        self.__add_word(line.strip().upper())
                dict_file.close()
            except FileNotFoundError:
                print('EXCEPTION: No dictionary file with the name', self.__dictionary, 'was found!\n')
        else:
            print('EXCEPTION: No valid dictionary file was provided!\n')

    def __add_word(self, word: str):
        """
        Add a word to the dictionary (private method)
        :param word: the new word to be added
        :return: True if the word is successfully added to the trie,
                 False if it already exists in the trie
        """

        upper_case_word = word.upper()
        if self.is_word(upper_case_word):
            # if the word already exists in our dictionary, no need to add it again
            return False

        current = self.__root
        for char in upper_case_word:
            child = current.get_child(char)
            # a character is added ONLY if it doesn't exist already
            if not child:
                child = current.insert(char)
            current = child
        current.set_ends_word(True)
        return True


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


#STUB
def calc_score(word_list):
    return 100
    
    
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
    result['score']= calc_score(word_list)
    result['words']=sorted(word_list)
    
    print('\nResult object:')
    print(result)
    
    return result

if __name__ == '__main__':
    main()
