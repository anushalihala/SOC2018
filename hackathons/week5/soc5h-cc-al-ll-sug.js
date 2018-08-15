'use strict';

/**
 * Generates a random world; a square board of size n x n containing 1s and 0s
 * @param n -- dimensions of board
 * @return Array randomBoard -- 2D array of size n x n containing 1s and 0s
 */
function randomWorldGenerator(n) {
    var randomBoard = [];
    for (var i = 0; i < n; i++) {
        var column = [];
        for (var j = 0; j < n; j++) {
            // generate a random integer between 0 and 1 included
            column[j] = Math.floor(Math.random() * 2);
        }
        randomBoard[i] = column[j];
    }
    return randomBoard;
}

/**
 * Returns a string representation of a 2D array in tabular form
 * @param world -- 2D array containing 1s and 0s
 * @return string worldStr -- 2D array as a string (in tabular form)
 */
function printWorld(world) {
    var worldStr = '[';
    var n = world.length;
    for (var i = 0; i < n; i++) {
        worldStr += '[';
        for (var j = 0; j < n; j++) {
            if (j !== n - 1) {
                worldStr += world[i][j] + ','
            } else {
                worldStr += world[i][j]
            }
        }
        worldStr += ']';
    }
    worldStr += ']';
    return worldStr;
}

/**
 * Counts the size of the continent containing the row indices[0] and column indices[1].
 * @param world -- 2D array containing 1s and 0s
 * @param indices -- position within continent whose area is to be counted
 * @return number area -- size of continent
 */
function continentCounter(world, indices) {
    var area = 0;
    var x = indices[0]; var y = indices[1];
    if (world[x][y] === 1) {
        // mark it as already counted
        world[x][y] = 0;
        area += 1;

        var n = world.length - 1;
        var xValues = []; var yValues = [];

        // calculate indices of neighbours
        if (x === 0) {
            xValues.push([x, x + 1]);
        } else if (x === n) {
            xValues.push([x - 1, x]);
        } else {
            xValues.push([x - 1, x + 1]);
        }

        if (y === 0) {
            yValues.push([y, y + 1]);
        } else if (y === n) {
            yValues.push([y - 1, y]);
        } else {
            yValues.push([y - 1, y + 1]);
        }

        for (var i = 0; i < xValues.length; i++) {
            for (var j = 0; j < yValues.length; j++) {
                var currentIndices = [xValues[i], yValues[j]];
                area += continentCounter(world, currentIndices);
            }
        }

    }
    return area;
}

/**
 * Checks if there is any land in the world, if there is a 1 in the 2D array.
 * @param world -- 2D array containing 1s and 0s
 * @return Array -- [-1, -1] if no land is found, or position of land there is land
 */
function findLand(world) {
    var ans = [-1, -1];
    var n = world.length;
    for (var i = 0; i < n; i ++) {
        var row = world[i];
        for (var j = 0; j < n; j++) {
            if (row[j] === 1) {
                ans = [i, j];
                return ans;
            }
        }
    }
    return ans;
}

/**
 * If coordinates given (not NaN), finds area of corresponding continent.
 * Else, finds areas of all continents in the world.
 * @param world -- 2D array containing 1s and 0s
 * @param coordinates -- coordinates of land inside the continent whose area is to be found
 * @return Array areas -- a map of sizes of continents
 */
function continentsCounter(world, coordinates) {
    var areas = [];
    if (isNaN(coordinates)) {
        var count = 1;
        var position = findLand(world);
        // while there is still land
        while (position[0] >= 0) {
            var currentArea = continentCounter(world, position);
            var currentName = 'continent' + count.toString();
            areas.push([currentName, currentArea]);
            count++;
            // find starting position for next continent
            position = findLand(world);
        }
    } else {
        var area = continentCounter(world, coordinates);
        areas.push(['continent', area]);
    }

    return areas;
}

/**
 * Find average time taken to find area of all continents in a world of size n x n
 * @param n -- size of world
 * @return number -- average running time
 */
function benchmarking(n) {
    var sum = 0;
    var iterations = 100;
    for (var i = 0; i < iterations; i++) {
        var periods = 10;
        var currentWorld = randomWorldGenerator(n);

        var start = performance.now();
        for (var j = 0; j < periods; j++) {
            continentsCounter(currentWorld, NaN);
        }
        var end = performance.now();
        var timeDiff = end - start;

        sum += timeDiff / periods;
    }
    return (sum / iterations);
}