from trienode import TrieNode


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
