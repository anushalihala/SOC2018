from dictionary import Dictionary


def main():
    filename = 'boggle-dictionary.txt'
    dictionary = Dictionary(filename)

    print('Is the word absinth part of the dictionary?', dictionary.is_word('absinth'))
    print('Is the prefix abs part of the dictionary?', dictionary.is_path('abs'))

    print('\nIs the empty string part of the dictionary?', dictionary.is_word(''))
    print('Is the empty prefix part of the dictionary?', dictionary.is_path(''))

    print('\nIs the word chair part of the dictionary?', dictionary.is_word('chair'))
    print('Is the word cha part of the dictionary?', dictionary.is_word('cha'))
    print('Is the prefix cha part of the dictionary?', dictionary.is_path('cha'))

    print('\nIs the word absolutives part of the dictionary?', dictionary.is_word('absolutives'))
    print('Is the word absolutive part of the dictionary?', dictionary.is_word('absolutive'))
    print('Is the word absolute part of the dictionary?', dictionary.is_word('absolute'))
    print('Is the prefix absolute part of the dictionary?', dictionary.is_path('absolute'))

    print('\nIs the word team part of the dictionary?', dictionary.is_word('team'))
    print('Is the word tea part of the dictionary?', dictionary.is_word('tea'))
    print('Is the prefix tea part of the dictionary?', dictionary.is_path('tea'))


if __name__ == '__main__':
    """
    Run dictionary API tests
    """
    main()
