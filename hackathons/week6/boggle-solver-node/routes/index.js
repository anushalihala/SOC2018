'use strict';

const express = require('express');
const router = express.Router();
let Main = require('../solver/Main.js');

let gameMain = undefined;
let board = [];
let words = [];
let result = {};

/**
 * GET method endpoint for the INDEX (default) page.
 */
router.get('/', function(req, res) {

    gameMain = new Main();

    gameMain.runSolver()
        .then(() => {
            gameMain.getResultsMap()
                .then((response) => {
                    board = response.get('board');
                    words = response.get('words');
                    result = response.get('result');

                    let boardHtml = "";
                    board.forEach(element => {
                        boardHtml += element.join('  ');
                        boardHtml += "<br/>";
                    });

                    let wordsHtml = words.join(', ');

                    // let resultHtml = JSON.stringify(result, null, 4);
                    let resultHtml = "{<br/>";
                    resultHtml += "score: " + result['score'] + ", <br/>";
                    resultHtml += "words: " + result['words'].join(', ');
                    resultHtml += "<br/>}";

                    res.render(
                        'index', {
                            title: 'Boggle Solver Challenge',
                            board: boardHtml,
                            words: wordsHtml,
                            result: resultHtml
                        }
                    );
                }
            );
        }
    );
});

module.exports = router;
