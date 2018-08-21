'use strict';

/**
 * Main entry to get the Boggle solver started
 * @return {Object} Boggle game result
 */
function main() {
    let dictFileName = "dictionary.txt";
    let boggleDictionary = new Dictionary(dictFileName);

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

    // create and initialize our solver
    let boggleSolver = new Solver(boggleBoard, boggleDictionary);

    console.log('Boggle board after shuffle:');
    boggleBoard.distriBoard.forEach((element) => {
        let eleStr = "";
        element.forEach((subelement) => {
            eleStr += subelement + " ";
        });
        console.log(eleStr);
    });

    console.log('\nAll valid words found on the board:');
    let wordList = boggleSolver.validWords;
    wordList.forEach((word) => {
        console.log(word);
    });

    // create result object
    let result = {};
    result['score'] = boggleSolver.score;
    result['words'] = wordList.sort();
    let resultAsString = JSON.stringify(result);
    console.log('\nResult object:', resultAsString);

    // benchmarking
    console.log('\nAverage time taken to find words on a standard Boggle board is:');
    console.log(benchmarking(boardSize, distribution, boggleDictionary), 'seconds');
    return result;
}

/**
 * Find average time taken to find all valid (given by dictionary) in a standard Boggle board game
 * @param boardSize: size of the board
 * @param distribution: dice distribution
 * @param boggleDictionary: Boggle dictionary
 * @return {Number} average time taken by the Boggle solver to compute all valid words and the total game score
 */
function benchmarking(boardSize, distribution, boggleDictionary) {
    let totalTime = 0;
    let computationsCount = 100;

    for (let i = 0; i < computationsCount; i++) {
        // initialize a board and its solver
        let boggleBoard = new Board(boardSize, distribution);
        let boggleSolver = new Solver(boggleBoard, boggleDictionary);

        let algorithmRunCount = 10;
        let startTime = performance.now();

        // run the Boggle game solver's algorithm
        for (let j = 0; j < algorithmRunCount; j++) {
            boggleSolver.validWords;
        }

        let endTime = performance.now();
        let duration = endTime - startTime;
        // average time taken by the algorithm
        totalTime = totalTime + (duration / algorithmRunCount);
    }

    return totalTime / computationsCount;
}


