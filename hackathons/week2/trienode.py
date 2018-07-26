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
