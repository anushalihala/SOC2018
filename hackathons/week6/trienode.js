'use strict';

class TrieNode {
    /**
     * Constructor: initialize a trie node with a given text string
     * @param text: text string at this trie node
     */
    constructor(text) {
        this.text = text;
        this.endsWord = false;
        this.childNodes = new Map();
    }

    /**
     * Does this node end a word
     * @return {boolean|*} true if this node ends a word, false otherwise
     */
    get endsWorld() {
        return this.endsWord;
    }

    /**
     * Set whether or not this node ends a word in a trie
     * @param worldEnd: value determining whether this node ends a word
     */
    set endsWorld(worldEnd) {
        this.endsWord = worldEnd;
    }

    /**
     * Return the child trie node that is found when you follow the link from the given character
     * @param character: the trie node the given character links to, or null if that link is not in trie
     */
    getChild(character) {
        if (character in this.childNodes.keys()) {
            return this.childNodes.get(character);
        }
        return null;
    }

    /**
     * Insert a character at this trie node
     * @param character: the character to be inserted
     * @return TrieNode: newly created trie node, or null if the character is already in the trie
     */
    doInsert(character) {
        if (character in this.childNodes.keys()) {
            return null;
        }
        let nextNode = new TrieNode(this.text + character);
        this.childNodes.set(character, nextNode);
        return nextNode;
    }
}