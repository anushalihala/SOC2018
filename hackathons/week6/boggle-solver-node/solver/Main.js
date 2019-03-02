'use strict';

let Board = require('./Board');
let Solver = require('./Solver');
let Dictionary = require('./Dictionary');

class Main {
    constructor() {
        this.board = [];
        this.wordList = [];
        this.result = {};
    }

    /**
     * Get the Boggle solver started
     * @return {Object} Boggle game result
     */
     async runSolver() {
         // initialize a standard 4x4 Boggle board
        let boardSize = 4;
        let distribution = {
            0: 'AAEEGN',
            1: 'ELRTTY',
            2: 'AOOTTW',
            3: 'ABBJOO',
            4: 'EHRTVW',
            5: 'CIMOTU',
            6: 'DISTTY',
            7: 'EIOSST',
            8: 'DELRVY',
            9: 'ACHOPS',
            10: 'HIMNQU',
            11: 'EEINSU',
            12: 'EEGHNW',
            13: 'AFFKPS',
            14: 'HLNNRZ',
            15: 'DEILRX'
        };

        // create and initialize our board
        let boggleBoard = new Board(boardSize, distribution);

        let dictFileName = "./solver/dictionary.txt";
        let boggleDictionary = new Dictionary(dictFileName);

        // wait for the dictionary file to be loaded into memory:
        boggleDictionary.loadDictionary()
            .then(() => {

                // create and initialize our solver
                let boggleSolver = new Solver(boggleBoard, boggleDictionary);
                this.board = boggleBoard.distriBoard;

                // compute all valid words on the board
                let words = boggleSolver.validWords;
                this.wordList = words;

                // create result object
                this.result = {};
                this.result['score'] = boggleSolver.score;
                this.result['words'] = words.sort();

                console.log("\nwordList is", words.join(' '));
                console.log("board is", boggleBoard.distriBoard);
                console.log("result is", JSON.stringify(this.result));

            })
            .catch((error) => {
                console.error("An error occurred!");
                console.error(JSON.stringify(error));
        });
     }

    /**
     * Return this Boggle game solver application results as a map
     * @return {Promise<Map>}
     */
    async getResultsMap() {
        let resultsMap = new Map();
        resultsMap.set('board', this.board);
        resultsMap.set('words', this.wordList);
        resultsMap.set('result', this.result);
        return resultsMap;
    }
}

module.exports = Main;
