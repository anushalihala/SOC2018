#!/usr/bin/env python3


def calculate_score(word_list):
    """
    Calculate the score of a boggle game from its word list
    :param word_list: list of all words on the board
    :return: the total score of the game
    """
    count = 0
    for x in word_list:
        x_length = len(x.strip())
        if(x_length < 3):
            continue
        else:
            count = count + (x_length - 2)
    return count
