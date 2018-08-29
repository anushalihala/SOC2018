'use strict';

const express = require('express');
const router = express.Router();
let Main = require('../solver/Main.js');

let time = 0;

/**
 * GET method endpoint for the BENCHMARK default page.
 */
router.get('/', function(req, res) {
    res.render(
        'pending', {
            title: 'Boggle Solver Benchmark'
        }
    );
});


/**
 * GET method endpoint for the BENCHMARK results page.
 */
router.get('/results', function(req, res) {
    benchmarking()
        .then(response => {
            time = Number.parseFloat(response).toFixed(4);
            console.log("response sent by benchmarking is:", response);

            let timeHtml = "<strong>" + time + "</strong> seconds per iteration";

            res.render(
                'benchmark', {
                    title: 'Boggle Solver Benchmark',
                    time: timeHtml
                }
            );
        }
    );
});

/**
 * Find average time taken to find all valid words (given by dictionary) in a standard Boggle board game
 * @return {Number} average time taken by the Boggle solver to compute all valid words and the total game score
 */
async function benchmarking() {

    let totalTime = 0;
    let computationsCount = 1000;

    for (let i = 0; i < computationsCount; i++) {
        let startTime = process.hrtime();

        let boggleGame = new Main();
        // run and wait for the Boggle game solver's algorithm
        await boggleGame.runSolver();

        let endTime = process.hrtime(startTime);
        totalTime += endTime[0] + (endTime[1] / 1000000);
    }

    return totalTime / computationsCount;
}

module.exports = router;
