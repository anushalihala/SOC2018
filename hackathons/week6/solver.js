'use strict';

class Solver {
    /**
     * Constructor: initializes a Boggle game solver
     * @param board: Boggle board to solve
     * @param dictionary: word dictionary to use
     */
    constructor(board, dictionary) {
        this.words = [];
        this.board = board;
        this.dictionary = dictionary;
    }

    /**
     * Return an array of valid words on the board
     * @return {Array} all valid words on the board
     */
    get validWords() {
        this.words = this.findWords();
        return this.words;
    }

    /**
     * Calculate the score of the current Boggle game
     * @return: {Number} the total score of the game
     */
    get score() {
        let score = 0;
        this.words.forEach((word) => {
           let wordSize = word.trim().length;
           if (wordSize > 2) {
               score += wordSize - 2;
           }
        });
        return score;
    }

    /**
     * Compute list of all legal words that can be formed from the distribution on the board
     * @return: {Array} valid words on the board
     */
    findWords() {
        let tilesInPrefix = {
            'stack': [],
            'set': new Set()
        };

        let size = this.board.boardSize;
        let validWords = [];

        for (let i = 0; i < this.board.boardSize; i++) {
            let row = Math.floor(i / size); // integer division
            let col = i % size;

            // add letter to prefix
            let prefix = this.board.distriBoard[row][col];
            // add tile to tiles in word
            let position = [row, col];
            tilesInPrefix['set'] = new Set().add(position);
            tilesInPrefix['stack'] = [position];

            // if the prefix exists in our dictionary, find its corresponding words
            if (this.dictionary.isPrefix(prefix)) {
                validWords.push(this.findNextWords(position, prefix, tilesInPrefix));
            }
        }
        return validWords;
    }

    /**
     * Find a list of all valid words on the board which correspond/complete to the given prefix
     * @param position: position of last character in the given prefix
     * @param prefix: prefix made up of letters from board tiles traversed so far
     * @param tilesInPrefix: stores positions of board tiles that make up the given prefix
     * @return: {Array} the list of valid words corresponding to the given prefix
     */
    findNextWords(position, prefix, tilesInPrefix) {

        let words = [];
        let neighbours = this.board.getNeighbours(position);
        for (let i = 0; i < neighbours.length; i++) {
            let ndx = tilesInPrefix['set'].indexOf();
            if (ndx < 0) {
                let x = position[0];
                let y = position[1];
                let currentLetter = this.board.distriBoard[x][y];
                let word = prefix + currentLetter;

                // is this word in the dictionary?
                if (this.dictionary.isWord(word)) {
                    words.push(word);
                }

                // is this word a prefix in the dictionary?
                if (this.dictionary.isPrefix(word)) {
                    tilesInPrefix['stack'].push(position);
                    tilesInPrefix['set'].add(position);
                    words.push(this.findNextWords(position, word, tilesInPrefix));

                    let visitedPosition = tilesInPrefix['stack'].pop();
                    tilesInPrefix['set'].delete(visitedPosition);
                }
            }
        }
        return words;
    }
}